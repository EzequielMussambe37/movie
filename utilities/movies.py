import streamlit as st

from streamlit_card import card 
from PIL import Image


def movieList():
    
    
    movies = {"move1":{"title":"start war","rate":5,"date":2014},"move3":{"title":"start1 war","rate":5,"date":2014},"move2":{"title":"starts war","rate":5,"date":2014}}
    
    cols = st.columns(len(movies))
    image="./assets/ezequiel_NY_1.png"
    image_movie = Image.open(image)
    heart = ":white_heart:"
    n=0
    for index,(movie, description) in enumerate(movies.items()):
        with cols[index]:
            #image="http://placekitten.com/200/300",
            st.image(image_movie)
            st.markdown("### Movie Description")
            st.markdown("###### new move")
            ss = st.button(heart, on_click=hello, key=index)
            print(st.session_state)
            st.write("data",ss)
            if ss:
                heart = ":heart:"
            else :
               heart = ":white_heart:" 
               print(ss)

def hello():
    pass