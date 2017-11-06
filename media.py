class Movie():

    """
    This class initializes the movie title, movie poster image,
    and movie trailer youtube url.
    These arguments must be passed when instantiating this class

    """

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
