import os
import logging
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv(override=True)  # Force .env file to override old terminal variables

logger = logging.getLogger(__name__)

HF_TOKEN = os.getenv("HF_TOKEN")
# Hardcoded to bypass any Windows/terminal environment caching issues
HF_MODEL_ID = "Qwen/Qwen2.5-7B-Instruct"

if not HF_TOKEN:
    logger.warning("HF_TOKEN environment variable is not set. Inference API calls might fail.")

client = InferenceClient(token=HF_TOKEN)

def generate_answer(context: str, question: str, history: list = None) -> str:
    system_prompt = (
        "Vous êtes Rafiki, un tuteur IA pour les étudiants marocains (2ème Bac).\n"
        "Utilisez le contexte fourni pour répondre à la question de manière pédagogique.\n"
        "Si le contexte ne contient pas l'information, dites-le.\n"
        "Vous avez une conversation avec l'étudiant. Utilisez l'historique pour suivre le fil.\n"
        f"Contexte du cours:\n{context}"
    )

    messages = [{"role": "system", "content": system_prompt}]
    if history:
        messages.extend(history)
    messages.append({"role": "user", "content": question})

    logger.info(f"===> Calling HuggingFace API with model: {HF_MODEL_ID} <===")

    response = client.chat_completion(
        model=HF_MODEL_ID,
        messages=messages,
        max_tokens=1500,
        temperature=0.3,
    )

    return response.choices[0].message.content

def generate_content(context: str, instruction: str, system_prompt: str, max_tokens: int = 2000, temperature: float = 0.3) -> str:
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Contexte du cours:\n{context}\n\n{instruction}"}
    ]
    response = client.chat_completion(
        model=HF_MODEL_ID,
        messages=messages,
        max_tokens=max_tokens,
        temperature=temperature,
    )
    return response.choices[0].message.content

def correct_exercise(context: str, exercise_text: str) -> str:
    system_prompt = (
        "Vous êtes Rafiki, un professeur de Maths/Physique pour le Bac marocain (2ème Bac).\n\n"
        "L'étudiant vous soumet un exercice. Vous devez le RÉSOUDRE complètement "
        "étape par étape, comme un professeur au tableau.\n\n"
        "RÈGLES:\n"
        "1. Résolvez l'exercice immédiatement - ne dites PAS ce que vous allez faire.\n"
        "2. Détaillez chaque étape avec des explications claires.\n"
        "3. Utilisez LaTeX ($$...$$) pour toutes les formules mathématiques.\n"
        "4. Soulignez la réponse finale.\n"
        "5. Si l'étudiant a écrit une réponse, dites si elle est correcte ou pas.\n"
        "6. Ne mentionnez JAMAIS l'extraction, l'OCR, l'image, ou le document.\n"
        "7. Ne décrivez PAS la structure du document - résolvez l'exercice.\n"
        f"\nContexte du cours:\n{context}"
    )

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": exercise_text}
    ]

    response = client.chat_completion(
        model=HF_MODEL_ID,
        messages=messages,
        max_tokens=2500,
        temperature=0.2,
    )

    return response.choices[0].message.content
