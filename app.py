
import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf

st.set_page_config(page_title="SmartWaste AI Classifier")

st.title("SmartWaste: AI-Powered Waste Classifier")
st.write("Upload an image of a waste item, and the AI will classify it as Recyclable, Organic, or Hazardous.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Waste Image.', use_column_width=True)

    st.write("Classifying...")
    # Simulated prediction
    predictions = ["Recyclable", "Organic", "Hazardous"]
    pred = np.random.choice(predictions)
    st.success(f"Predicted Waste Category: **{pred}**")
