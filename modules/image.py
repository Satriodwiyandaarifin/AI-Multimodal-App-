import urllib.parse

def generate_image(prompt):
    encoded_prompt = urllib.parse.quote(prompt)
    return f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=512&height=512"