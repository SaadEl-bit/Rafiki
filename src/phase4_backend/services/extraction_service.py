import os
import io
import base64
import logging
from typing import List, Optional
import fitz  # PyMuPDF
from PIL import Image
from fastapi import UploadFile
from huggingface_hub import InferenceClient

logger = logging.getLogger(__name__)

HF_TOKEN = os.getenv("HF_TOKEN")
VL_MODEL_ID = os.getenv("VL_MODEL_ID", "meta-llama/Llama-3.2-11B-Vision-Instruct")

client = InferenceClient(token=HF_TOKEN)

def file_to_base64_images(file_bytes: bytes, filename: str) -> List[str]:
    """
    Converts a PDF or an Image file into a list of base64 encoded strings.
    """
    base64_images = []
    
    if filename.lower().endswith('.pdf'):
        # Open PDF with PyMuPDF
        doc = fitz.open(stream=file_bytes, filetype="pdf")
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            # Render page to an image (pixmap) with a good resolution
            pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
            img_bytes = pix.tobytes("png")
            
            # Convert to base64
            b64 = base64.b64encode(img_bytes).decode('utf-8')
            base64_images.append(b64)
    else:
        # Assume it's an image (PNG, JPG, etc.)
        try:
            img = Image.open(io.BytesIO(file_bytes))
            # Convert to RGB if needed
            if img.mode != 'RGB':
                img = img.convert('RGB')
            buffered = io.BytesIO()
            img.save(buffered, format="JPEG")
            b64 = base64.b64encode(buffered.getvalue()).decode('utf-8')
            base64_images.append(b64)
        except Exception as e:
            logger.error(f"Failed to process image: {e}")
            
    return base64_images

def extract_text_via_vl(base64_images: List[str]) -> str:
    """
    Sends base64 images to the Hugging Face Serverless Vision API to extract text.
    """
    if not base64_images:
        return ""
        
    extracted_text = ""
    
    for idx, b64_img in enumerate(base64_images):
        logger.info(f"Extracting text from page/image {idx+1}/{len(base64_images)}")
        
        messages = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{b64_img}"}
                    },
                    {
                        "type": "text", 
                        "text": "Extract ONLY the raw text and mathematical formulas from this image. Do NOT describe the image, do NOT mention page numbers, do NOT use markdown headings. Output only the content text. Use LaTeX $$...$$ for math. No explanations or descriptions."
                    }
                ]
            }
        ]
        
        try:
            response = client.chat_completion(
                model=VL_MODEL_ID,
                messages=messages,
                max_tokens=2000,
                temperature=0.1
            )
            extracted_text += response.choices[0].message.content
        except Exception as e:
            logger.error(f"Error calling Vision API for image {idx+1}: {e}")
            extracted_text += f"\n\n[Error extracting text from page {idx+1}]\n"
            
    return extracted_text.strip()
