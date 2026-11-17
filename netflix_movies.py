# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

netflix_movies = netflix_df[netflix_df["type"] == "Movie"]

# Start coding here! Use as many cells as you like
netflix_subset = netflix_movies[["title", "country", "genre", "release_year", "duration"]]

#1 Filter the data for movies released in the 1990s
movies_in_90s = netflix_movies[netflix_movies["release_year"].between(1990, 1999)]

#2 Find the most frequent movie duration
duration = int(movies_in_90s["duration"].mode().iloc[0])
most_frequent_duration = movies_in_90s["duration"].mode().iloc[0]

#3  Count the number of short action movies from the 1990s
short_action_movies = movies_in_90s[(movies_in_90s["genre"] == "Action") & (movies_in_90s["duration"] < 90)]
short_movie_count = len(short_action_movies)

#0 Visualisation
colors = []
for lab, row in netflix_subset.iterrows():
    if row["genre"] == "Children":
        colors.append("red")
    elif row["genre"] == "Documentaries":
        colors.append("green")
    elif row["genre"] == "Stand-Up":
        colors.append("blue")
    else:
        colors.append("black")

fig = plt.figure(figsize=(12, 8))
plt.scatter(netflix_subset["release_year"], netflix_subset["duration"], c=colors)
plt.xlabel("Release year")
plt.ylabel("Duration (min)")
plt.title("Movie Duration by Year of Release")
plt.show()
