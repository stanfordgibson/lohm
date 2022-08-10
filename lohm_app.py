import streamlit as st
from PIL import Image # Load images

st.markdown('# LOHM')
st.markdown('## Land Of Milk and Honey')
st.markdown('''
Affordable skincare for everyone
''')

with st.container():
    image_col, text_col = st.columns(1,2)
    with image_col:
        st.image(image)
    with text_col:
        st.write(text)

with st.container():
    image_col, text_col = st.columns(1,2)
    with image_col:
        st.image(image2)
    with text_col:
        st.write(text2)



