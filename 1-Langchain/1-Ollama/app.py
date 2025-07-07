import os 
from dotenv import load_dotenv
from langchain_ollama import OllamaLLM
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# Langsmith Tracking 
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")


# Prompt Template
prompt = ChatPromptTemplate(
    [
        ("system", "You are a helpful assistant. Please respond to the question asked"),
        ("user" , "Question : {question}")
    ]
)


# Streamlit framework
st.title("Langchain Demo with LLAMA2")
input_text = st.text_input("What's on your mind??")

# Ollama LLAMA2 model
llm = OllamaLLM(model="llama2")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question" : input_text}))


