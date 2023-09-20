# Step 1: Import necessary libraries
import pandas as pd
import numpy as np

# Step 2: Load the dataset
df = pd.read_csv('dataset-netflix.csv')

# Step 3: Check for missing values in all columns
missing_values = data.isnull().sum()
print("Missing Values:")
print(missing_values)

# Step 4: Handle missing values
# For 'director' column, replace missing values with 'Not Given'
data['director'].fillna('Not Given', inplace=True)

# For 'country' and 'listed_in' columns, replace missing values with 'NULL'
data['country'].fillna('NULL', inplace=True)
data['listed_in'].fillna('NULL', inplace=True)

# Step 5: Check and standardize data formats
data['date_added'] = pd.to_datetime(data['date_added'], errors='coerce').dt.strftime('%d/%m/%Y')

#Step 6:# Checking and standardizing other formats
data['release_year'] = data['release_year'].astype(str)  # Convert release_year to string format

# Extract numeric part of duration and convert to minutes
data['duration'] = data['duration'].str.extract('(\d+)').fillna(0).astype(int)
data['duration'] = data['duration'].apply(lambda x: x*10 if 'Season' in str(x) else x)  # Assuming 10 episodes per season

# Step 7: Outlier check for 'release_year'
# Since release year is a numeric value, we performed an outlier check using the IQR method.
Q1 = df['release_year'].quantile(0.25)
Q3 = df['release_year'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers_release_year = df[(df['release_year'] < lower_bound) | (df['release_year'] > upper_bound)]

# Display the outliers
print(outliers_release_year)

# Step 8: Outlier check for 'duration'
# Duration includes both movies (in minutes) and TV shows (in seasons). We performed an outlier check separately for each.
# For movies, we considered an IQR of around 30-60 minutes.
# For TV shows, we considered an IQR of around 2-5 seasons.

# First, handle movies
movies_duration = df[df['duration'].str.contains('min', na=False)]
movies_duration['duration'] = movies_duration['duration'].str.replace(' min', '').astype(int)

Q1_movies = movies_duration['duration'].quantile(0.25)
Q3_movies = movies_duration['duration'].quantile(0.75)
IQR_movies = Q3_movies - Q1_movies
lower_bound_movies = Q1_movies - 1.5 * IQR_movies
upper_bound_movies = Q3_movies + 1.5 * IQR_movies
outliers_movies_duration = movies_duration[(movies_duration['duration'] < lower_bound_movies) | (movies_duration['duration'] > upper_bound_movies)]

# Display the outliers for movies
print(outliers_movies_duration)

# Step 9: Handle outliers for movies' duration
# We decided to cap the outliers to the upper bound value.
movies_duration['duration'] = np.where(movies_duration['duration'] > upper_bound_movies, upper_bound_movies, movies_duration['duration'])

#Step 10: Outlier check for 'TV shows'
Q1_tv_shows = tv_shows_duration['duration'].quantile(0.25)
Q3_tv_shows = tv_shows_duration['duration'].quantile(0.75)
IQR_tv_shows = Q3_tv_shows - Q1_tv_shows
lower_bound_tv_shows = Q1_tv_shows - 1.5 * IQR_tv_shows
upper_bound_tv_shows = Q3_tv_shows + 1.5 * IQR_tv_shows
outliers_tv_shows_duration = tv_shows_duration[(tv_shows_duration['duration'] < lower_bound_tv_shows) | (tv_shows_duration['duration'] > upper_bound_tv_shows)]

# Display the outliers for TV shows
print(outliers_tv_shows_duration)

# Step 11: Handle outliers for 'TV shows' seasons
# We decided to cap the outliers to the upper bound value.
tv_shows_duration['duration'] = np.where(tv_shows_duration['duration'] > upper_bound_tv_shows, upper_bound_tv_shows, tv_shows_duration['duration'])

# Combine the cleaned movie and TV show dataframes
cleaned_duration_df = pd.concat([movies_duration, tv_shows_duration])

# Step 12: Outlier check for date_added
# (You can use statistical methods like IQR, or domain-specific knowledge)
# For date_added, we can calculate IQR and remove entries outside the range

Q1 = data['date_added'].quantile(0.25)
Q3 = data['date_added'].quantile(0.75)
IQR = Q3 - Q1

# Define upper and lower bounds
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filter out outliers
data = data[~((data['date_added'] < lower_bound) | (data['date_added'] > upper_bound))]

# Step 13: Save the cleaned dataset to a new CSV file
data.to_csv('cleaned_dataset.csv', index=False)
