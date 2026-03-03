# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 18:48:19 2023

@author: zeb
"""

import pandas as pd
import matplotlib.pyplot as plt
# Load the dataset from CSV
df = pd.read_csv(r"D:\programs\PYTHON\recommended_movies.csv")
# Ask the user for preferences
age_pref = input("Enter preferred age group (e.g., 13+): ")
min_imdb = float(input("Enter minimum IMDb rating (e.g., 6.0): "))
min_rotten_tomatoes = int(input("Enter minimum Rotten Tomatoes rating (e.g., 70): "))
min_runtime = int(input("Enter minimum runtime in minutes (e.g., 100): "))
max_runtime = int(input("Enter maximum runtime in minutes (e.g., 150): "))
# Filter movies based on user preferences
filtered_movies = df[
(df['Age'] == age_pref if age_pref else True) &
(df['IMDb'] >= min_imdb) &
(df['Rotten Tomatoes'].str.rstrip('%').astype(float) >= min_rotten_tomatoes) &
(df['Runtime'] >= min_runtime) &
(df['Runtime'] <= max_runtime)
]
# Display recommended movies
if len(filtered_movies) == 0:
  print("No movies found matching your criteria.")
else:
  print("\nRecommended Movies:")
  print(filtered_movies[["Title", "Year", "Age", "IMDb", "Rotten Tomatoes", "Runtime"]])
# Save recommendations to a file (optional)
  x=filtered_movies['IMDb']
  filtered_movies.to_csv("recommended_movies.csv", index=False)
  plt.figure(figsize=(10, 5))
  plt.hist(x)
  plt.xlabel('Rating')
  
  plt.title('Movie Ratings Based on User Preferences')

  plt.show()
