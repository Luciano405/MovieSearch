import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("TMDB_API_KEY")

movie_id = "1234731"
api_url = f"https://api.themoviedb.org/3/movie/{movie_id}"

params = {"api_key": API_KEY, 
          "language": "pt-BR"}

response = requests.get(api_url, params=params)
data = response.json()
poster_path = data.get("poster_path")

if poster_path:
    poster_url = "https://image.tmdb.org/t/p/w500" + poster_path
else:
    poster_url = "Poster não disponível"

print("Titulo:", data["original_title"])
print("Nota dos usuarios:", data["vote_average"])
print("Sinopse:", data["overview"])
print("Data de lançamento:", data["release_date"])
print("Poster:", poster_url)
