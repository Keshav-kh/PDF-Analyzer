import streamlit as st
from PyPDF2 import PdfReader
import random
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=google_api_key)

st.set_page_config(
    page_title="PDF Analyzer",
    page_icon="💬",
)

def typewriter_effect(text):
    html_code = f"""
    <style>
        @keyframes type {{
            from {{ width: 0; }}
            to {{ width: 100%; }}
        }}

        .typewriter-text {{
            white-space: nowrap;
            overflow: hidden;
            display: inline-block;
            font-size: 3vw;
            margin-bottom: 10px;
            margin-top: 125px
        }}
    </style>
    <div class="typewriter-text">{text}</div>
    """
    st.markdown(html_code, unsafe_allow_html=True)

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text)
    return chunks


def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")  
    
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")


    
    
    return vector_store

def get_conversational_chain():
    prompt_template = """
    Context:\n {context}?\n
    Question: \n{question}\n
    Answer:
    """
    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)
    return chain

def user_input(user_question, chain):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    docs = new_db.similarity_search(user_question)

    response = chain(
        {"input_documents": docs, "question": user_question},
        return_only_outputs=True
    )
    st.write("Reply: ", response["output_text"])

def main():
    page_bg_img = """
    <style>
    [data-testid="stAppViewContainer"]{
        background: url('');
        background-repeat: no-repeat;
        background-size: cover;
    }
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

    typewriter_effect("PDF Analyzer")

    user_question = st.text_input("Ask a Question from the uploaded PDF")

    if user_question:
        user_input(user_question, chain)

    processing_words = ["Unveiling the Data...", "Parsing the Prose...", "Data Detectives in Action...", "Stirring the Data Pot...", "Baking up your Bits and Bytes...", "Brewing your Files...", "Cooking those Codes...", "Bytes on the Boil...", "File Fusion in Action..."]

    with st.sidebar:
        st.title("Upload:")
        pdf_docs = st.file_uploader("Drop your PDF files and click on the \"Submit and Process\" button below (multiple files supported)", accept_multiple_files=True)
        if st.button("Submit & Process"):
            with st.spinner(processing_words[(random.randint(0, 8))]):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                get_vector_store(text_chunks)
                st.success("File Uploaded Successfully!")

    st.markdown("<br><br><br><br><br><br><br>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("Made with ❤️ by Keshav Khandelwal")

if __name__ == "__main__":
    chain = get_conversational_chain()
    main()
