class Movie:
    def __init__(self, title: str = '', overview: str = '', language: str = '', movie_ratings: str = '', release_date: str = '') -> None:
        self.title = title
        self.overview = overview
        self.language = language
        self.movie_ratings = movie_ratings
        self.release_date = release_date
