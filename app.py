import streamlit as st
import random
import numpy as np
from PIL import Image

# Class names
class_names = ['Organic', 'Recyclable', 'Hazardous']

# App title and sidebar
st.set_page_config(page_title="SmartWaste AI", layout="centered")
st.title("♻️ SmartWaste - AI Waste Classifier")

# Tabs for sections
tab1, tab2, tab3, tab4 = st.tabs(["🏠 Home", "📷 Classify Waste", "ℹ️ About", "📞 Contact"])

with tab1:
    st.subheader("Welcome to SmartWaste 🌍")
    st.markdown("""
        **SmartWaste** is an AI-powered web app that helps users identify and classify waste items into:

        - ♻️ Recyclable  
        - 🌿 Organic  
        - ☣️ Hazardous  

        Our goal is to **promote sustainability** and **support proper waste management** through technology.

        ---
        **🚀 How it Works:**
        1. Upload a photo of a waste item
        2. The app classifies it
        3. Take action based on the result ✅
    """)

with tab2:
    st.header("Upload a Waste Image 🧾")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Waste Image", use_container_width=True)

        # Simulate image preprocessing (even though no real model is used)
        img = image.resize((224, 224))
        img_array = np.array(img) / 255.0
        img_array = img_array.reshape(1, 224, 224, 3)

        # Random prediction (demo mode without TensorFlow)
        predicted_class = random.choice(class_names)

        st.success(f"🧠 Predicted Category: **{predicted_class}**")

with tab3:
    st.header("ℹ️ About SmartWaste")
    st.markdown("""
        **SmartWaste** is a capstone project developed as part of the **3MTT Learning Community** in Nigeria.

        It uses artificial intelligence to support environmental sustainability by helping users sort waste responsibly.

        ---
        **🔧 Technologies Used:**
        - `Streamlit` for web interface
        - `Pillow` for image handling
        - `Python` as core language

        ---
        **🛠 How to Run Locally:**
        ```bash
        pip install -r requirements.txt
        streamlit run app.py
        ```

        **Developer:** Usman Abubakar Sahabo  
        **Fellow ID:** FE/23/97913892  
        #3MTTLearningCommunity #My3MTT
    """)

with tab4:
    st.header("📞 Contact Developer")

    st.markdown("""
    **👤 Name:** Usman Abubakar Sahabo  
    **🆔 Fellow ID:** FE/23/97913892  

    **📧 Email:** [uasahabo@gmail.com](mailto:uasahabo@gmail.com)  
    **🔗 LinkedIn:** [linkedin.com/in/uasahabo](https://www.linkedin.com/in/uasahabo)  
    **🐦 X (Twitter):** [@uasahabo](https://twitter.com/uasahabo)  

    _Built with ❤️ for the #3MTTLearningCommunity & 🇳🇬 Nigeria_
    """)

# Footer
st.markdown("---")
st.markdown("<center>© 2025 SmartWaste AI | Powered by Usman A. Sahabo</center>", unsafe_allow_html=True)
