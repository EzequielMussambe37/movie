import streamlit as st
from config import streamlitConfig

from utilities import movies 


class MovieRecommendation:
    
    def __init__(self):
        
        self.movieName = ""

    def app():
        streamlitConfig.mainConfig()
        movies.movieList()
    
    
    
if __name__ == "__main__":
    
    app = MovieRecommendation
    app.app()