# 🏥 Med Chat – Medical Chatbot for Symptom Analysis

**Med Chat** is an AI-powered medical assistant chatbot built using **LangChain**, **Google's Gemini (Generative AI)**, and **Streamlit**. It helps users determine which medical department to consult based on their symptoms in a professional and empathetic manner.

---

## 🚀 Features

- Symptom-based department recommendation
- Context-aware conversation memory
- Professional tone with clarifying questions
- Emergency alerts for critical symptoms
- Clean, interactive UI with department guide


---

## 🧠 Built With

- [Streamlit](https://streamlit.io/)
- [LangChain](https://www.langchain.com/)
- [Google Generative AI (Gemini)](https://ai.google/discover/gemini/)
- [Python-dotenv](https://pypi.org/project/python-dotenv/)

---

## 📦 Requirements

Install all required Python packages using:

```bash
pip install -r requirements.txt
```

### `requirements.txt`

```
streamlit
langchain
langchain-google-genai
langchain-community
google-generativeai
python-dotenv
```

---

## 🔐 Setup

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/med-chat.git
cd med-chat
```

2. **Create a `.env` file**

Add your Google API key:

```
GOOGLE_API_KEY=your_google_api_key_here
```

> 🔑 You need access to Gemini via Google Generative AI for this chatbot to work.

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 👨‍💻 Author

**Soumyadip Chakrabarti**  
IBM GENAI Project – Medical Chatbot

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).

---

## 💡 Disclaimer

This chatbot is **not a replacement for professional medical advice**. Always consult a licensed medical practitioner in case of health concerns.
