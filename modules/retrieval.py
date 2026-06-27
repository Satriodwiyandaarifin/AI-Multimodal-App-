import pandas as pd
import random

print("Loading TinyStories dataset...")

df = pd.read_csv("dataset/stories.csv")

print("Dataset loaded!")

def retrieve_context():

    story = random.choice(
        df["text"].dropna().tolist()
    )

    return story[:1000]