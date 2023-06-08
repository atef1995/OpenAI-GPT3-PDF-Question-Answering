# pdf-to-chatgpt

PDF Question Answering System with OpenAI's GPT-3
This Python script is a Question Answering system, powered by OpenAI's GPT-3 language model. It reads a PDF file, extracts the text, and uses the text as a basis for answering questions about the content of the file.

Features
PDF Parsing: It uses PyPDF2 to read the PDF file and extract the text content.

Question Answering: It utilizes OpenAI's GPT-3 model to answer questions about the text content. The user can ask questions via the command line.

How to Use
PDF File: Update the pdf_path variable with the path to the PDF file you want to use.

Ask Questions: Run the script and enter your questions. Each question is handled line by line. When you are finished with your question, enter '.' on a new line and press enter to finish.

Review Answers: The generated answer from the GPT-3 model will be printed to the console.

Please note, to use this script you will need to install the openai and PyPDF2 packages, and also you will need to provide your own OpenAI API key.

Requirements
PyPDF2
openai
Please remember to respect OpenAI's use-case policy while using this script.

This code is provided as-is, and it is free to be used and modified. The author holds no responsibility for how it is used.
