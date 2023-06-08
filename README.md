# OpenAI-GPT3-PDF-Question-Answering

This repository contains a Python script that implements a Question Answering (QA) system. It is powered by OpenAI's GPT-3 and PyPDF2 for PDF manipulation. 

## Description

The script reads a PDF file, extracts the text, and uses this extracted text as a knowledge base for the GPT-3 model. Users can then interact with the model by asking questions related to the contents of the PDF file. The script leverages the `text-davinci-003` engine from OpenAI for generating responses. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need Python 3.x and the following packages installed:
- `openai`
- `PyPDF2`

### Installation

1. Clone the repository: 
    ```
    git clone https://github.com/atef1995/OpenAI-GPT3-PDF-Question-Answering.git
    ```
2. Navigate into the directory:
    ```
    cd OpenAI-GPT3-PDF-Question-Answering
    ```
3. Install the required packages: 
    ```
    pip install -r requirements.txt
    ```
4. Place your PDF file in the same directory as the script.

5. Run the script and interact with the model by asking questions in the command line:
    ```
    python script.py
    ```

## Usage

While the script is running, enter your questions one at a time in the console. To end the question session, simply input a single period character (`.`) and press Enter.

### Example

```shell
Enter your question (enter '.' on a new line to finish):
Who is the author of the document?
