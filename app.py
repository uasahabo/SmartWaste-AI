import streamlit as st
from PIL import Image
import numpy as np

# Uncomment below if you have a trained model
# from tensorflow.keras.models import load_model

# Set page configuration
st.set_page_config(page_title="SmartWaste - AI Waste Classifier", layout="centered")

# Tabs for navigation
tab1, tab2 = st.tabs(["📋 About", "🔍 Classifier"])

# 📋 About Tab
with tab1:
    st.title("♻️ SmartWaste - AI-Powered Waste Classifier")
    st.markdown("""
**SmartWaste** is an AI-powered web app that helps users classify waste items into categories such as **Recyclable**, **Organic**, and **Hazardous**.  
It promotes proper waste management and sustainability practices.

---

### 🚀 Features
- 📤 Upload image of a waste item  
- 🧠 Get AI-based classification  
- 📱 Simple, mobile-friendly UI  

---

### 🛠️ Technologies Used
- Streamlit (for web interface)  
- TensorFlow/Keras (for AI model - placeholder)  
- Python  

---

### ▶️ How to Run Locally
```bash
pip install -r requirements.txt  
streamlit run app.py
