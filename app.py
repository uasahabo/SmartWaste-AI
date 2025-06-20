import streamlit as st
from PIL import Image
import numpy as np

# Set page config
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
    pip install -r requirements.txt
    streamlit run app.py

---

### 👨‍💻 Author
**Usman Abubakar Sahabo**  
Fellow ID: `FE/23/97913892`  
#3MTTLearningCommunity #My3MTT
""")

# 🔍 Classifier Tab
with tab2:
    st.title("🧠 Waste Image Classifier")
    st.write("Upload an image of a waste item to classify it as Recyclable, Organic, or Hazardous.")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)

        st.write("Classifying...")

        # Dummy prediction
        classes = ["Recyclable", "Organic", "Hazardous"]
        prediction = np.random.choice(classes)

        st.success(f"🧠 Predicted Class: **{prediction}**")

        # Uncomment when using real model
        # model = load_model("model.h5")
        # preprocessed_image = preprocess(image)
        # prediction = model.predict(preprocessed_image)
