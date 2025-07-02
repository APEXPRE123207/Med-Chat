import os
import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain

# Load environment variables from .env file
load_dotenv()

# Configure Streamlit page
st.set_page_config(page_title="MediBot", page_icon="🏥")
st.title("🏥 Medical Chatbot for Symptom Analysis")
st.write("Describe your symptoms and we'll recommend which medical department to consult.")

# Function to initialize LangChain chat system
def initialize_chatbot_chain():
    llm_model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.3)

    system_template = SystemMessagePromptTemplate.from_template(
        """You are a medical assistant chatbot designed to help patients identify which medical department 
        they should consult based on their symptoms. Your task is to:
        
        1. Ask clarifying questions if symptoms are vague
        2. Analyze the described symptoms
        3. Recommend the most appropriate medical department(s)
        4. Briefly explain your reasoning
        
        Departments include:
        - Cardiology (heart)
        - Dermatology (skin)
        - Endocrinology (hormones)
        - Gastroenterology (digestive)
        - Neurology (nervous system)
        - Ophthalmology (eyes)
        - Orthopedics (bones)
        - ENT (ears, nose, throat)
        - Pediatrics (children)
        - Pulmonology (lungs)
        - Rheumatology (joints)
        - Urology (urinary)
        
        Be professional and empathetic. If symptoms suggest an emergency, advise immediate medical attention.
        """
    )

    human_template = HumanMessagePromptTemplate.from_template("{user_query}")

    chat_prompt = ChatPromptTemplate.from_messages([
        system_template,
        MessagesPlaceholder(variable_name="chat_history"),
        human_template
    ])

    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    chat_chain = LLMChain(
        llm=llm_model,
        prompt=chat_prompt,
        memory=memory,
        verbose=False
    )

    return chat_chain

# Session initialization
if "chat_chain" not in st.session_state:
    st.session_state.chat_chain = initialize_chatbot_chain()
    st.session_state.chat_log = [
        {
            "role": "assistant",
            "content": "Hello! I'm here to help you determine which medical department you should consult based on your symptoms. Could you please describe how you're feeling?"
        }
    ]

# Display past messages
for entry in st.session_state.chat_log:
    with st.chat_message(entry["role"]):
        st.markdown(entry["content"])

# User input and assistant response
if user_input := st.chat_input("Describe your symptoms..."):
    st.session_state.chat_log.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.spinner("Analyzing symptoms..."):
        try:
            bot_reply = st.session_state.chat_chain.run(user_query=user_input)
        except Exception as err:
            st.error(f"An error occurred: {str(err)}")
            bot_reply = "I'm having trouble processing your request. Please try again later."

    st.session_state.chat_log.append({"role": "assistant", "content": bot_reply})
    with st.chat_message("assistant"):
        st.markdown(bot_reply)

# Sidebar - Project Info
st.sidebar.markdown("""
    **IBM GENAI Project** - Medical Chatbot for Symptom Analysis  
    **Soumyadip Chakrabarti**
""")

# Sidebar - Medical Departments Reference
st.sidebar.markdown("""
**Medical Departments Guide:**
- **Cardiology**: Heart and cardiovascular system  
- **Dermatology**: Skin, hair, nails  
- **Endocrinology**: Hormones and metabolism  
- **Gastroenterology**: Digestive system  
- **Neurology**: Brain and nervous system  
- **Ophthalmology**: Eyes and vision  
- **Orthopedics**: Bones, joints, muscles  
- **ENT**: Ears, nose, throat  
- **Pediatrics**: Children's health  
- **Pulmonology**: Lungs and breathing  
- **Rheumatology**: Joints and autoimmune diseases  
- **Urology**: Urinary system
""")
