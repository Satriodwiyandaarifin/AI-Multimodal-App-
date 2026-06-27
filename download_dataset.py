from datasets import load_dataset
import pandas as pd

dataset = load_dataset("roneneldan/TinyStories")

df = pd.DataFrame(dataset["train"])

df.to_csv("dataset/stories.csv", index=False)

print("Dataset berhasil disimpan!")
print(df.head())