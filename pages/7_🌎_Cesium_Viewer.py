import streamlit as st
from common import cesium_to_streamlit

def main():
    st.title("Interactive Cesium Globe Viewer")

    st.write("Welcome to the Cesium Globe Viewer! You can interact with the globe below.")

    cesium_to_streamlit('https://charm-tortoiseshell-croissant.glitch.me/')

    st.write("Use your mouse to interact with the globe:")
    st.write("- Left-click and drag to rotate")
    st.write("- Right-click and drag to zoom")
    st.write("- Middle-click and drag to pan")

if __name__ == "__main__":
    main()
