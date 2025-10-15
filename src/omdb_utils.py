# omdb_utils.py
import requests

def get_movie_details(title, 65f95272 ):

    url = f"http://www.omdbapi.com/?t={title}&plot=full&apikey={65f95272}"
    res = requests.get(url).json()
    if res.get("Response") == "True":
        result = res.get("Plot", "N/A"), res.get("Poster", "N/A")
        plot = result[0]
        poster = result[1]
        return plot, poster

    return "N/A", "N/A"
