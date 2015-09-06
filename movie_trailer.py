#!/usr/bin/python
import fresh_tomatoes
import media
from imdb import IMDb
""" Fetches details of blockbuster movies from IMDB and stores them
    as Movie objects. A list containing all such movie objects is
    sent as argument to open_movies_page method of fresh_tomatoes module."""
# Creating an imdb object for accessing the IMDB module's methods.
imdb = IMDb()

# Creating an empty array
all_favorite_movies = []
# Storing the movie names and corresponding Youtube trailer
# urls in a dictionary object as key-value pairs.
favorite_movies = {
    "The Pursuit of Happyness": "https://www.youtube.com/watch?v=89Kq8SDyvfg",
    "The WhistleBlower": "https://www.youtube.com/watch?v=al3anBiHwmI",
    "Fight Club": "https://www.youtube.com/watch?v=SUXWAEX2jlg",
    "Toy Story 2": "https://www.youtube.com/watch?v=Lu0sotERXhI"
}

# Looping through each item in the dictionary object and retrieving
# the key and value pair of each item.
for movie_name, trailer_url in favorite_movies.items():
    # Fetching the list of movies that match the given name.
    movies_list = imdb.search_movie(movie_name)
    # Fetching the movie details of first movie in the list.
    movie = imdb.get_movie(movies_list[0].movieID)
    # Instantiating a movie object.
    movie_details = media.Movie(movie['title'], movie['full-size cover url'],
                                trailer_url, movie['rating'])
    # Appending the movies_details object to array.
    all_favorite_movies.append(movie_details)

# Calling the open_movies_page method with an array as argument
# that contains all the movie objects in it.
fresh_tomatoes.open_movies_page(all_favorite_movies)
