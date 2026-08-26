'''
Write a program that displays information about a given movie. 
Prompt for a search query and display the title, year, rating, running time, and a synopsis, if one exists.
Then, if the audience score is above 80%, recommend that the user watch this movie right now.
If the score is below 50%, recommend that the user avoid the movie at all costs.

Example Output
Enter the name of a movie: Guardians of the Galaxy
Title: Guardians of the Galaxy
Year: 2014
Rating: PG-13
Running Time: 121 minutes
Description: From Marvel...
You should watch this movie right now!
'''


#using omdb api to get the movie information and recommendation as rottentomatos is not available
import requests

'''
movie_title = input("Type the movie title: ")
movie_year = input("Type the year of movie release: ")
url = "https://www.omdbapi.com/"
api_key = "dfd3e318"

params = {
    "apikey": api_key,
    "t": movie_title,
    "y": movie_year,
    "plot": "full",
    "r": "json"
    }

response = requests.get(url, params=params)
data = response.json()

movie_name = data['Title']
year = data['Year']
release_date = data['Released']
runtime = data['Runtime']
description = data['Plot']
rating = data['Rated']
imdb_rating = data['imdbRating']

print(f"Tile: {movie_name}")
print(f"Movie Year: {year}")
print(f"Release Data: {release_date}")
print(f"Movie Runtime: {runtime}")
print(f"OMDb Rating: {rating}")
print(f"iMBD Rating: {imdb_rating}")
print(f"Movie description: {description}")
'''

# same program using function

def movie_recom(movie_title, movie_year):
    url = "https://www.omdbapi.com/"
    api_key = "dfd3e318"

    params = {
        "apikey": api_key,
        "t": movie_title,
        "y": movie_year,
        "plot": "full",
        "r": "json"
        }

    response = requests.get(url, params=params)
    data = response.json()

    movie_name = data['Title']
    year = data['Year']
    release_date = data['Released']
    runtime = data['Runtime']
    description = data['Plot']
    rating = data['Rated']
    imdb_rating = data['imdbRating']

    print(f"Tile: {movie_name}")
    print(f"Movie Year: {year}")
    print(f"Release Data: {release_date}")
    print(f"Movie Runtime: {runtime}")
    print(f"OMDb Rating: {rating}")
    print(f"iMBD Rating: {imdb_rating}")
    print(f"Movie description: {description}")

movie_title = input("Type the movie title: ")
movie_year = input("Type the year of movie release: ")

movie_recom(movie_title, movie_year)