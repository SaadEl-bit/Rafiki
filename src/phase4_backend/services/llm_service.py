import os
from huggingface_hub import InferenceClient
import logging

logger = logging.getLogger(__name__)

HF_TOKEN = os.getenv("HF_TOKEN")
HF_MODEL_ID = os.getenv("HF_MODEL_ID", "Saad-Elouakate/rafiki-qwen-2.5-finetune")

if not HF_TOKEN:
    logger.warning("HF_TOKEN environment variable is not set. Inference API calls might fail.")

client = InferenceClient(token=HF_TOKEN)

def generate_answer(context: str, question: str) -> str:
    system_prompt = (
        "Vous êtes Rafiki, un tuteur IA pour les étudiants marocains (2ème Bac).\n"
        "Utilisez le contexte fourni pour répondre à la question de manière pédagogique.\n"
        "Si le contexte ne contient pas l'information, dites-le.\n"
        f"Contexte:\n{context}"
    )

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": question}
    ]

    response = client.chat_completion(
        model=HF_MODEL_ID,
        messages=messages,
        max_tokens=1500,
        temperature=0.3,
    )

    return response.choices[0].message.content

def correct_exercise(context: str, exercise_text: str) -> str:
    system_prompt = (
        "Vous êtes Rafiki, un tuteur IA pour les étudiants marocains (2ème Bac).\n"
        "Voici un exercice (et peut-être la réponse de l'étudiant). "
        "Corrigez-le étape par étape comme un professeur.\n"
        f"Contexte:\n{context}"
    )

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": exercise_text}
    ]

    response = client.chat_completion(
        model=HF_MODEL_ID,
        messages=messages,
        max_tokens=2000,
        temperature=0.3,
    )

    return response.choices[0].message.content
