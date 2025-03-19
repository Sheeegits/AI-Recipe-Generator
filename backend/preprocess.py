import pandas as pd
import os

# Path to the dataset
dataset_path = r"C:\Users\Singh\.cache\kagglehub\datasets\paultimothymooney\recipenlg\versions\1\RecipeNLG_dataset.csv"

# Load the dataset
df = pd.read_csv(dataset_path)

# Select only required columns
df = df[["title", "ingredients", "directions"]]

# Rename columns for consistency
df.rename(columns={"directions": "instructions"}, inplace=True)

# Create the output directory if it doesn't exist
output_dir = "data"
os.makedirs(output_dir, exist_ok=True)

# Save the preprocessed dataset
output_path = os.path.join(output_dir, "recipes.csv")
df.to_csv(output_path, index=False, encoding="utf-8")

print(f"Preprocessed dataset saved at: {output_path}")
