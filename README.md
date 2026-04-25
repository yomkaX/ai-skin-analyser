# 🧴 AI Skin Analyzer Ultra

An advanced **AI-powered skin analysis web application** that leverages computer vision techniques to detect skin type, analyze texture, estimate skin health, and provide actionable skincare insights.

---

## 🚀 Key Features

* 📸 Upload face/skin image for analysis
* 👤 Face detection using OpenCV
* 🔴 Basic acne and spot detection
* 🧠 Skin type classification (Oily / Dry / Normal)
* 📊 Skin health metrics:

  * Oil Level
  * Hydration Level
  * Skin Health Score
  * Confidence Score
* 📈 Visual indicators and progress bars
* 🧾 Downloadable report (CSV format)
* 🖥 Interactive UI with tabs (Streamlit)

---

## 🛠️ Tech Stack

* **Language:** Python
* **Framework:** Streamlit
* **Libraries:**

  * OpenCV
  * NumPy
  * Pandas
  * Pillow

---

## ⚙️ How It Works

1. Upload a face or skin image
2. The system processes the image using computer vision techniques
3. Detects facial regions using OpenCV
4. Extracts features such as:

   * Brightness
   * Texture
   * Pixel distribution
5. Performs:

   * Skin type classification
   * Acne/spot estimation
   * Health scoring
6. Generates:

   * Skin metrics
   * Confidence score
   * Personalized suggestions

---

## 📊 Output Metrics

The system evaluates multiple parameters:

* Skin Type (Oily / Dry / Normal)
* Oil Level (%)
* Hydration Level (%)
* Skin Health Score (0–100)
* Confidence Score (%)
* Acne / Spot Detection (Basic)

---

## 💻 Installation & Setup

### 1️⃣ Clone the Repository

git clone https://github.com/yomkaX/ai-skin-analyser.git
cd ai-skin-analyser

---

### 2️⃣ Create Virtual Environment

python -m venv myenv

#### Activate:

Windows:
myenv\Scripts\activate

Mac/Linux:
source myenv/bin/activate

---

### 3️⃣ Install Dependencies

pip install --upgrade pip
pip install -r requirements.txt

---

### 4️⃣ Run the Application

streamlit run main.py

---

### 5️⃣ Open in Browser

http://localhost:8501

---

## ⚡ Customization Options

* Improve acne detection using ML models
* Replace rule-based logic with deep learning (CNN)
* Enhance scoring logic with real datasets
* Improve UI with better charts and themes
* Add real-time camera input

---

## 🚀 Future Improvements

* Deep learning-based skin classification (CNN / ResNet)
* Real-time skin analysis using webcam
* AI-based skincare recommendations
* Product recommendation engine
* Skin history tracking dashboard
* Integration with dermatology datasets

---

## ⚠️ Disclaimer

This project is intended for **educational purposes only** and does not replace professional dermatological advice.

---

## 🏁 Conclusion

This project demonstrates how **Computer Vision + AI + Web Development** can be combined to build a practical system for **skin analysis and personalized insights**.
