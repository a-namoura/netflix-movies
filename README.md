# Investigating Netflix Movies

An exploratory data analysis project that uses **Python, pandas, and Matplotlib** to investigate Netflix movies, with a particular focus on films released during the **1990s**.

Completed as part of DataCamp's **Investigating Netflix Movies** project.

## Project Overview

The analysis explores movie duration, release year, and genre in a Netflix dataset. It answers two main questions:

1. What is the most frequent duration of Netflix movies released between **1990 and 1999**?
2. How many **Action** movies from that decade are shorter than **90 minutes**?

It also creates a scatter plot showing how movie duration varies by release year, with colors distinguishing selected genres.

## Tools and Libraries

- **Python 3** — programming language
- **pandas** — loading, filtering, and analyzing the dataset
- **Matplotlib** — creating the scatter plot

## Dataset

The script reads a CSV file named **`netflix_data.csv`**:

```python
netflix_df = pd.read_csv("netflix_data.csv")
```

**Important:** This CSV is **not included in the current GitHub repository**. To run the analysis locally, obtain the dataset from the original DataCamp project environment (or provide a compatible CSV) and place it beside `netflix_movies.py`.

The code expects at least these columns:

| Column | Description |
| --- | --- |
| `type` | Content type; used to select records marked `Movie` |
| `title` | Movie title |
| `country` | Country associated with the movie |
| `genre` | Genre label, such as `Action` or `Documentaries` |
| `release_year` | Year the movie was released |
| `duration` | Movie duration in minutes |

The analysis assumes the column names and genre labels match those used in the original exercise.

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/a-namoura/netflix-movies.git
cd netflix-movies
```

### 2. Install Dependencies

```bash
python3 -m pip install pandas matplotlib
```

On Windows, substitute `python` for `python3` if needed.

### 3. Add the Dataset

Place `netflix_data.csv` in the repository directory:

```text
netflix-movies/
├── README.md
├── netflix_movies.py
└── netflix_data.csv   # Required locally; not included in this repository
```

### 4. Run the Analysis

```bash
python3 netflix_movies.py
```

The script calculates the requested values and displays a Matplotlib scatter plot. It does **not** print the two numeric answers or save the chart to a file by default.

## Analysis Workflow

### 1. Select Movies

The program removes non-movie records and keeps a subset of relevant columns:

```python
netflix_movies = netflix_df[netflix_df["type"] == "Movie"]
netflix_subset = netflix_movies[
    ["title", "country", "genre", "release_year", "duration"]
]
```

### 2. Analyze 1990s Movies

Movies released from 1990 through 1999 (inclusive) are selected:

```python
movies_in_90s = netflix_movies[
    netflix_movies["release_year"].between(1990, 1999)
]
```

The most common movie duration is stored in `duration` (and also in `most_frequent_duration`) using the statistical **mode**:

```python
duration = int(movies_in_90s["duration"].mode().iloc[0])
```

### 3. Count Short Action Movies

The program identifies 1990s movies that satisfy **both** conditions:

- Genre is exactly `Action`.
- Duration is strictly less than `90` minutes.

The number of matching movies is stored in `short_movie_count`.

### 4. Visualize Movie Durations

The scatter plot uses:

- **X-axis:** release year
- **Y-axis:** movie duration (minutes)
- **Data:** all records filtered to `Movie`, not only those from the 1990s

Points are colored by genre:

| Genre | Color |
| --- | --- |
| Children | Red |
| Documentaries | Green |
| Stand-Up | Blue |
| All other genres | Black |

The chart is titled **Movie Duration by Year of Release** and is displayed with `plt.show()`.

## Viewing the Numeric Results

The script computes `duration` and `short_movie_count` but does not print them. To display the answers in a normal terminal run, add the following lines after their assignments:

```python
print(f"Most frequent 1990s movie duration: {duration} minutes")
print(f"Short action movies from the 1990s: {short_movie_count}")
```

The actual values depend on the contents of your `netflix_data.csv` file. No fixed result is claimed here because that dataset is not included in the repository.

## Repository Contents

| File | Description |
| --- | --- |
| [`netflix_movies.py`](netflix_movies.py) | Data filtering, 1990s analysis, short-action-movie count, and scatter plot. |
| `README.md` | Project overview, setup, and analysis documentation. |
| `netflix_data.csv` (required locally) | Input dataset expected by the script; not currently tracked in this repository. |

## Scope and Limitations

This is a focused educational analysis rather than a complete Netflix analytics application.

- The input CSV must have the expected column names and compatible data types.
- The code does not currently handle missing files or validate malformed input.
- The chart is shown interactively; it is not automatically exported.
- The project does not contain an included dataset, automated tests, or a command-line interface.

## Acknowledgment

Based on the **Investigating Netflix Movies** project from [DataCamp](https://www.datacamp.com/). This repository contains the author's Python analysis and is not an official Netflix project.
