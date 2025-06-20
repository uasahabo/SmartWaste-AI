import streamlit as st
from PIL import Image
import numpy as np

st.set_page_config(page_title="SmartWaste AI Classifier")

st.title("♻️ SmartWaste: AI-Powered Waste Classifier")
st.write("Upload an image and get a simulated AI classification… Demo version in action.")

uploaded_file = st.file_uploader("📷 Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, use_column_width=True)
    pred = np.random.choice(["Recyclable", "Organic", "Hazardous"])
    st.success(f"✅ Category: {pred}")
