import streamlit as st
import re
import pickle


# Function to clean the news text
def cleanNews(txt):
    cleanText = re.sub(r'http\S+\s', ' ', txt)
    cleanText = re.sub(r'RT|cc', ' ', cleanText)
    cleanText = re.sub(r'#\S+\s', ' ', cleanText)
    cleanText = re.sub(r'@\S+', ' ', cleanText)
    cleanText = re.sub(r'[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', cleanText)
    cleanText = re.sub(r'[^\x00-\x7f]', ' ', cleanText)
    cleanText = re.sub(r'\s+', ' ', cleanText).strip()
    return cleanText


# Load models and vectorizer directly
tfidf = pickle.load(open('Models/tfidf.pkl', 'rb'))
model = pickle.load(open('Models/DT.pkl', 'rb'))

# Streamlit app
st.title("📰 Fake News Detection App")

# Input from the user
st.markdown("Enter the news article below to check if it's fake or real:")
user_input = st.text_area("News Text", height=200)

if st.button("Check for Fake News"):
    if user_input.strip():
        # Clean and transform input text
        cleaned_news = cleanNews(user_input)
        input_features = tfidf.transform([cleaned_news])

        # Make prediction
        prediction = model.predict(input_features)[0]

        # Display result with appropriate feedback
        if prediction == 0:
            st.error("⚠️ This news is likely **FAKE**.")
        else:
            st.success("✅ This news is likely **REAL**.")
    else:
        st.warning("⚠️ Please enter some text to check.")

# Footer
st.markdown(
    """
    <style>
    footer {visibility: hidden;}
    .reportview-container .main .block-container {padding-top: 2rem;}
    </style>
    """, unsafe_allow_html=True
)
