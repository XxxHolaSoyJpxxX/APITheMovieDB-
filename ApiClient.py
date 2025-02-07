import requests
from Movie import Movie
import json


class ApiClient :
    
    def __init__(self, api_token: str):
        self.api_token = api_token
    
    def parseJson(self, response: dict) -> list[Movie]:
        movies = []
        if not results:
            return movies
        results = response.get("results", [])
        for movie_data in results:
            movie = Movie(
                title=movie_data.get("title", ""),
                overview=movie_data.get("overview", ""),
                lenguage=movie_data.get("original_language", ""),
                movieRatings=str(movie_data.get("vote_average", "")),
                releaseDate=movie_data.get("release_date", ""),
            )
            movies.append(movie)
        return movies
        
    def makeRequest(self, url: str) -> list[Movie]:
        url = "https://api.themoviedb.org/3/search/movie?query=terminator&include_adult=true&language=en-US&page=1"
        self.api_token="eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0ZGVjMzVjM2JjYmMwZDlmZWM5NDUxY2I3YWY4OWQxOSIsIm5iZiI6MTczODY3NzE5My43NjQ5OTk5LCJzdWIiOiI2N2EyMWJjOWE0NTI4N2I3ZmRlMmUwMjkiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.wenJn8-xgMERXKo1hN_48uA1qaRTS4DKAQ_MQcG555s"
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {self.api_token}",
        }
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            response_data = response.json()
            return self.parseJson(response_data)
        else:
            print(f"Error en la solicitud: {response.status_code}")
            print(response.text)
            return []