import cv2
import streamlit as st
from PIL import Image
import numpy as np
import io

st.header("🖼️ Image Resizer and Flipper")

img = st.file_uploader("Upload your image", type=["jpg", "jpeg", "png"])

if img:
    img = Image.open(img)
    img_array = np.array(img)
    st.image(img_array, caption="Original Image", width=200)

    # Default values (width, height)
    height = st.number_input("Enter the height", min_value=1, value=img_array.shape[0])
    width = st.number_input("Enter the width", min_value=1, value=img_array.shape[1])

    # Flip options
    flip_option = st.selectbox("Flip Direction", ["None", "Vertical", "Horizontal"])

    if flip_option == "Vertical":
        flipped_img = cv2.flip(img_array, 0)
        st.image(flipped_img, caption="Vertically Flipped Image", width=200)
        img_array = flipped_img  # Update image array if needed for resizing

    elif flip_option == "Horizontal":
        flipped_img = cv2.flip(img_array, 1)
        st.image(flipped_img, caption="Horizontally Flipped Image", width=200)
        img_array = flipped_img

    if st.button("Resize"):
        resized_img = cv2.resize(img_array, (int(width), int(height)))
        st.image(resized_img, caption="Resized Image", width=200)

        resized_pil = Image.fromarray(resized_img)
        buff = io.BytesIO()
        resized_pil.save(buff, format="JPEG")

        st.download_button(
            "Download Image",
            data=buff.getvalue(),
            mime="image/jpeg",
            file_name="resized_image.jpg"
        )
