import webbrowser

class Movie():
    """File - media.py
    class Movie
    This file used to create the movie blueprint.
    There are 5 constructors for the movie object.These are: title,
    poster_image_url, trailer_youtube_url, rating and movie storyline.
    File - entertainment_center.py
    In this file objects called Movie are instantiated. This file also
    creates a list of the movie objects and passes them to the fresh_tomatoes.py
    """

    #static list available to make it possible to show standard ratings
    VALID_RATINGS = ["G","PG","PG-13","R"]

    #init intantiates the container housing all the components for the webpage
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, rating):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.rating = rating

    #play_trailer open webbrowser and plays youtube_url        
    def play_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
