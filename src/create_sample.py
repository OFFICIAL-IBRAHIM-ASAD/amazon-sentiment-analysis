import pandas as pd

file_path = "amazon_reviews_multilingual_US_v1_00.tsv"
sample_path = "amazon_reviews_sample.csv"

# Read only the first 50,000 rows using nrows
df = pd.read_csv(file_path, sep='\t', nrows=50000)

# Save the sample as a CSV
df.to_csv(sample_path, index=False)
print(f"Sample saved successfully to {sample_path}")