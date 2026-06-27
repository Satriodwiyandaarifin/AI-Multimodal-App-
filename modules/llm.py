from transformers import pipeline
from modules.retrieval import retrieve_context

print("Loading local LLM...")

generator = pipeline(
    "text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0"
)

def generate_text(prompt):

    # ambil contoh cerita dari dataset
    context = retrieve_context()

    final_prompt = f"""
You are a creative storyteller.

Below is an example fairy tale:

{context}

Create a NEW fairy tale in Indonesian.

User idea:
{prompt}

Story:
"""

    result = generator(
        final_prompt,
        max_new_tokens=250,
        temperature=0.8,
        do_sample=True,
        return_full_text=False
    )

    return result[0]["generated_text"]