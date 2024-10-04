# PDF Analyzer

![PDF Analyzer](https://img.shields.io/badge/License-MIT-green.svg)  

## Overview

PDF Analyzer is a web application built using Streamlit that allows users to upload PDF documents, extract text, and interactively ask questions about the content of those documents. Leveraging natural language processing (NLP) capabilities, this application provides answers based on the context derived from the uploaded PDF files.

## Features

- **PDF Upload**: Upload multiple PDF files for analysis.
- **Text Extraction**: Automatically extracts text from PDF files using the `PyPDF2` library.
- **Natural Language Processing**: Uses the Google Generative AI to answer questions about the extracted text.
- **Vector Store**: Utilizes FAISS for efficient similarity searches against the extracted text chunks.

## Technologies Used

- **Streamlit**: For building the web application.
- **PyPDF2**: For reading and extracting text from PDF files.
- **Langchain**: For creating embeddings and handling question-answering chains.
- **Google Generative AI**: For generating answers to user questions.
- **FAISS**: For efficient similarity search and retrieval of text embeddings.

## Installation

To run the application locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/keshav-kh/PDF-Analyzer.git
   cd PDF-Analyzer
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up your Google API key. Create a `.env` file in the project root and add your API key:

   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

## Usage

1. Run the application:

   ```bash
   streamlit run app.py
   ```

2. Open your web browser and navigate to `http://localhost:8501`.

3. Upload one or more PDF files and use the input field to ask questions about the content.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any improvements or bugs you find.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

- Thanks to the developers of Streamlit, Langchain, and Google Generative AI for providing the tools that made this project possible.
- Inspiration for the project came from the need to analyze and extract information from PDF documents easily.

---

Feel free to modify any sections, add more details, or customize the formatting to better suit your project's identity!