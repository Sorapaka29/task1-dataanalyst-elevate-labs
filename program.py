import pandas as pd

# Load the CSV file
df = pd.read_csv('netflix_titles.csv')

# Drop columns where all values are NaN
df = df.dropna(axis=1, how='all')

# Drop rows with any NaN values
df = df.dropna()

# Drop duplicate rows
df = df.drop_duplicates()

# Optional: Save the cleaned data to a new file
df.to_csv('netflix_titles_cleaned.csv', index=False)

# Print the shape of the cleaned DataFrame
print("Cleaned data shape:", df.shape)
