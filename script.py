import openai
import PyPDF2

openai.api_key = "YOUR-API-KEY"
pdf_path = r"/YOUR/PDF/PATH"
prompts = []

# Read the book pages and create prompts
with open(pdf_path, "rb") as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    num_pages = len(pdf_reader.pages)

    for page_number in range(num_pages):
        page = pdf_reader.pages[page_number]
        text = page.extract_text()
        prompts.append(text)

# Start the conversation with the first prompt
conversation = prompts[0]

while True:
    print("Enter your question (enter '.' on a new line to finish):")
    lines = []
    while True:
        line = input()
        if line == ".":
            break
        lines.append(line)

    if not lines:  # No question entered
        break

    question = " ".join(lines)

    # Extend the conversation with the question
    conversation += f"\nQ: {question}\nA:"

    # Generate response using the extended conversation
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=conversation,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # Retrieve and print the generated answer
    generated_answer = response.choices[0].text.strip()
    print("Generated Answer:", generated_answer)
