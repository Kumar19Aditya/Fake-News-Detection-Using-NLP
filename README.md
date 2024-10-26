
# 📰 Fake News Detection System  

An **NLP Project** that detects and classifies news articles as **real or fake** using **Natural Language Processing (NLP)** techniques. This project aims to address the growing problem of misinformation by providing an automated tool to identify deceptive news articles.  

---

## 🚀 Project Overview  

The Fake News Detection System processes news content, extracts features using NLP, and classifies the content using machine learning models. Users can access the tool through an intuitive **web application** to input news articles or headlines and get predictions.  

---

## 🎯 Features  

- **Automated News Classification** – Detects whether a news article is real or fake.  
- **Text Preprocessing** – Handles text cleaning (removing URLs, hashtags, punctuation, etc.).  
- **Machine Learning Models** – Uses algorithms like **Logistic Regression**, **Decision Trees**, or **Random Forest**.  
- **Interactive Web Interface** – Built with **Streamlit** for easy access.  
- **Model Feedback System** – Enhances model performance with continuous data and feedback.  

---

## 🛠️ Tech Stack  

- **NLP Libraries:** NLTK, SpaCy, Scikit-learn  
- **Web Framework:** Streamlit  
- **Models:** Logistic Regression, Decision Trees ,Random Forest 
- **Database (optional):** SQLite  
- **Language:** Python  

---

## 📂 Project Structure  

```
Fake-News-Detection-System/
│
├── Models/                # Pre-trained ML models (e.g., Logistic Regression, DT)
├── Dataset/               # True and Fake Datasets
├── Application.py         # Main Streamlit web application
├── requirements.txt       # List of dependencies
├── README.md              # Project documentation
└── Data Cleaning & Preprocessing.ipynb                 #Clean the data and modelling
    
```

---

## ⚙️ Setup Instructions  

1. **Clone the Repository:**  
   ```bash
   git clone https://github.com/Kumar19Aditya/Fake-News-Detection-System.git
   cd Fake-News-Detection-System
   ```

2. **Create a Virtual Environment:**  
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # For Linux/macOS  
   .venv\Scripts\activate     # For Windows  
   ```

3. **Install Dependencies:**  
   ```bash
   pip install -r Requirements.txt
   ```

4. **Run the Application:**  
   ```bash
   streamlit run Application.py
   ```

---

## 📝 Usage  

1. **Launch the Web Application.**  
2. **Input a news headline or article.**  
3. Click **"Predict"** to get the classification (Real or Fake).  
4. **Optional:** Provide feedback to improve the model.  

---

## 📊 Example Screenshots  

### Home Page  
![Home Page](https://via.placeholder.com/600x300?text=Screenshot+Home+Page)

### Fake News Prediction  
![Prediction](https://via.placeholder.com/600x300?text=Prediction+Example)

---

## 🧠 How It Works  

1. **Text Preprocessing:**  
   - Removes URLs, punctuation, hashtags, and special characters.
   - Converts text to lowercase and tokenizes it.

2. **Feature Extraction:**  
   - Uses **TF-IDF vectorization** to extract numerical features from text.

3. **Model Training:**  
   - Trains machine learning models like **Logistic Regression** and **Decision Trees** on labeled datasets.

4. **Prediction:**  
   - The model predicts whether a news article is **Real** or **Fake** based on the input.

---

## 🔗 Resources  

- [Scikit-learn Documentation](https://scikit-learn.org/)  
- [Streamlit Documentation](https://docs.streamlit.io/)  

---

## 🚀 Future Enhancements  

- **Add Deep Learning Models:** Use LSTM or BERT for better accuracy.  
- **API Integration:** Enable API-based predictions for broader use.  
- **User Authentication:** Add login features to track user feedback.  

---


## 🛡️ License  

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.  

---

## 👤 Author  

**Kumar Aditya**  
GitHub: [Kumar19Aditya](https://github.com/Kumar19Aditya)  

---

## 📧 Contact  

Feel free to reach out for any questions or suggestions:  
📧 Email: adityapupun535@gmail.com

---

This README provides all necessary information for your **Fake News Detection System** and ensures it's easy for users to set up and contribute. Let me know if you need any changes! 🚀
