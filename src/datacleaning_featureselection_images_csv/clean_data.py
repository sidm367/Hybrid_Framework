import pandas as pd

# Load the dataset
df = pd.read_csv("Crop_recommendation.csv")

# Clean column names (standard lowercase + strip whitespace)
df.columns = [col.strip().lower() for col in df.columns]

# Drop nulls and duplicates
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

# Convert to numeric types
numeric_cols = ['n', 'p', 'k', 'temperature', 'humidity', 'ph', 'rainfall']
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')

# Remove invalid values
df = df[df['rainfall'] >= 0]
df = df[df['ph'].between(0, 14)]

# Clean categorical label column
df['label'] = df['label'].astype(str).str.strip().str.lower()

# Save cleaned dataset
df.to_csv("cleaned_dataset.csv", index=False)
print("✅ Cleaning complete. Saved as cleaned_dataset.csv")
