import pandas as pd

# Load the raw dataset
raw_data_path = '/Users/ashraf96/Desktop/mldemo/project-name/data/raw/sample_raw_data.csv'
raw_data = pd.read_csv(raw_data_path)

# Process the data (example: removing missing values and normalizing)
processed_data = raw_data.dropna()  # Remove rows with missing values
processed_data = (processed_data - processed_data.mean()) / processed_data.std()  # Normalize the data

# Save the processed data to a new CSV file
processed_data_path = '/Users/ashraf96/Desktop/mldemo/project-name/data/processed/sample_processed_data.csv'
processed_data.to_csv(processed_data_path, index=False)

print(f"Processed data saved to {processed_data_path}")