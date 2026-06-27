from transformers import pipeline

print("Loading model...")

generator = pipeline(
    "text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0"
)

print("Model loaded!")

prompt = """
You are a creative storyteller.

Write a short story about a kind dragon.
"""

result = generator(
    prompt,
    max_new_tokens=200,
    temperature=0.8,
    do_sample=True,
    return_full_text=False
)

print("\n=== OUTPUT ===\n")
print(result[0]["generated_text"])