import pandas as pd

FILE_NAME = 'GooglePlay.csv'
# Assuming the dataset is in a CSV file named 'dataset.csv'
df = pd.read_csv(FILE_NAME)

# Remove non-numeric characters from the 'Installs' column
df['Installs'] = df['Installs'].str.replace(',', '').str.replace('+', '')
df['Installs'] = pd.to_numeric(df['Installs'], errors='coerce')

# Drop rows with NaN values in the 'Installs' column
df = df.dropna(subset=['Installs'])

# Remove non-numeric characters from the 'Reviews' column
df['Reviews'] = pd.to_numeric(df['Reviews'].str.replace(',', ''), errors='coerce')

# Store the cleaned dataset in a new file named 'cleaned_dataset.csv'
df.to_csv('cleaned_dataset.csv', index=False)

# Display a message to indicate the file has been saved
print("The cleaned dataset has been saved to 'cleaned_dataset.csv'.")




# Function to calculate characteristics
def calculate_characteristics(df, column_name):
    characteristics = {
        'Outlier': None, # Outlier calculation depends on the context
        'Median': df[column_name].median(),
        'Mode': df[column_name].mode()[0] if df[column_name].mode().size > 0 else None,
        'Mean': df[column_name].mean(),
        'Max': df[column_name].max(),
        'Min': df[column_name].min(),
        'Range': df[column_name].max() - df[column_name].min(),
        'Type': 'Discrete' if df[column_name].dtype == 'int64' else 'Continuous',
        'Feature Name': column_name
    }
    return characteristics

# Calculate characteristics for each numerical column
numerical_columns = ['Rating', 'Reviews' , 'Installs']
for column in numerical_columns:
    characteristics = calculate_characteristics(df, column)
    print(f"Characteristics for {column}:")
    print(characteristics)
    print("\n")
