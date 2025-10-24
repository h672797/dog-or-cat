import streamlit as st
from PIL import Image

st.title("Dog or Cat??")
st.write(
    "Upload an image here!"
)

# --- Load pretrained model ---

#@st.cache_resource
#def load_model():
#    model = 
#    return model

#model = load_model()

# --- Upload file ---
uploaded_file = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])

#(for now) Show picture when button clicked
if uploaded_file is not None:
    if st.button("Show Image"):
        image = Image.open(uploaded_file)
        st.image(image, caption="yup", use_column_width=True)
    