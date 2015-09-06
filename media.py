import webbrowser


class Movie():
    """ Stores the Movie details like title, rating, image url and
    trailer url and plays the youtube trailer of the movie."""

    # Initializes the object with the movie data.
    def __init__(self, title, poster_image, trailer_url, rating):
        self.title = title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_url
        self.movie_rating = rating

    def view_trailer(self):
        """ Plays the trailer of the movie in the browser. """
        webbrowser.open(self.trailer_youtube_url)
