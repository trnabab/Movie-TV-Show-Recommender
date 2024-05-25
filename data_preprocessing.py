import pandas as pd

# Load the dataset
file_path = 'netflix_titles.csv'
netflix_df = pd.read_csv(file_path)

# Display the first few rows of the dataframe
print("Initial data:")
print(netflix_df.head())

# Handling missing values
# Display columns with missing values
print("\nMissing values before cleaning:")
print(netflix_df.isnull().sum())

# Fill missing values for categorical columns with a placeholder
netflix_df['director'].fillna('No Director', inplace=True)
netflix_df['cast'].fillna('No Cast', inplace=True)
netflix_df['country'].fillna('Unknown', inplace=True)
netflix_df['duration'].fillna('Unknown', inplace=True)
netflix_df['rating'].fillna('Unknown', inplace=True)

# Fill missing values for date columns with the mode (most frequent value)
most_frequent_date = netflix_df['date_added'].mode()[0]
netflix_df['date_added'].fillna(most_frequent_date, inplace=True)

# Standardize data formats
# Convert 'date_added' to datetime format
netflix_df['date_added'] = pd.to_datetime(netflix_df['date_added'], errors='coerce')

# Handle duplicates
netflix_df.drop_duplicates(inplace=True)

# Feature Engineering
# Extract year from date_added
netflix_df['year_added'] = netflix_df['date_added'].dt.year

# Categorize duration
def convert_duration(duration):
    if 'Season' in duration:
        return 'TV Show'
    else:
        return 'Movie'
    
netflix_df['duration_type'] = netflix_df['duration'].apply(convert_duration)

# Display data after feature engineering
print("\nData after feature engineering:")
print(netflix_df.head())

# Display missing values after feature engineering
print("\nMissing values after feature engineering:")
print(netflix_df.isnull().sum())

# Save the cleaned dataset
cleaned_file_path = 'cleaned_netflix_titles.csv'
netflix_df.to_csv(cleaned_file_path, index=False)