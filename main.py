import streamlit as st
import cv2
import numpy as np
from PIL import Image
import pandas as pd

st.set_page_config(page_title="AI Skin Analyzer Ultra", layout="wide")


st.sidebar.title("⚙️ Settings")
show_gray = st.sidebar.checkbox("Show Grayscale Image", True)

st.title("🧴 AI Skin Analyzer Ultra")
st.markdown("Advanced AI-based skin analysis system")

uploaded_file = st.file_uploader("Upload a face image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    img = np.array(image)


    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)


    brightness = np.mean(gray)
    texture = np.std(gray)

    oil = min(max((brightness / 255) * 100, 20), 95)
    hydration = 100 - oil
    health = int((hydration + (100 - abs(texture - 50))) / 2)
    confidence = min(max((brightness / 255) * 100, 60), 95)


    if brightness > 170:
        skin_type = "Oily"
    elif brightness < 100:
        skin_type = "Dry"
    else:
        skin_type = "Normal"

    condition = "Healthy ✅" if health > 70 else "Moderate ⚠️" if health > 50 else "Poor ❌"

   )
    _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
    acne_count = np.sum(thresh == 255) // 500


    tab1, tab2, tab3 = st.tabs(["📊 Report", "🧠 Details", "🖼 Image"])

    
    with tab1:
        col1, col2, col3 = st.columns(3)
        col1.metric("Skin Type", skin_type)
        col2.metric("Health Score", health)
        col3.metric("Condition", condition)

        st.progress(health / 100)

        st.markdown("### 📈 Metrics")
        st.write(f"Oil Level: {oil:.2f}%")
        st.progress(oil / 100)

        st.write(f"Hydration: {hydration:.2f}%")
        st.progress(hydration / 100)

        st.write(f"Confidence: {confidence:.2f}%")
        st.progress(confidence / 100)

        st.write(f"Acne Spots Detected: {acne_count}")

 
    with tab2:
        st.subheader("🧠 AI Insights")
        st.write("• Brightness indicates oil/dry levels")
        st.write("• Texture shows smoothness of skin")
        st.write("• Acne detection based on bright pixel clusters")

        st.subheader("💡 Recommendations")

        if skin_type == "Oily":
            tips = ["Use oil-free products", "Wash face twice daily"]
        elif skin_type == "Dry":
            tips = ["Use moisturizer", "Drink more water"]
        else:
            tips = ["Maintain skincare routine", "Stay hydrated"]

        for tip in tips:
            st.write(f"- {tip}")

   
    with tab3:
        st.image(img, caption="Detected Face", use_column_width=True)

        if show_gray:
            st.image(gray, caption="Grayscale", use_column_width=True)

   
    report = pd.DataFrame({
        "Metric": ["Skin Type", "Health", "Condition", "Oil", "Hydration", "Confidence", "Acne"],
        "Value": [skin_type, health, condition, oil, hydration, confidence, acne_count]
    })

    st.download_button("📥 Download Report", report.to_csv(index=False), "skin_report.csv")

    st.info("⚠️ This is a simulated AI system for educational purposes.")
