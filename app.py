import gradio as gr
from rag import QuestionAnsweringBot
from rag import read_docs, dir_path
from typing import List


def upload_file(files) -> List[str]:
    file_paths = [file.name for file in files]
    return file_paths


def read_uploaded_docs(uploaded_docs: List[str]) -> List[str]:
    docs = []
    for path in uploaded_docs:
        with open(path, 'r', encoding='utf-8') as file:
            text = file.read()
            docs.append(text)
    return docs


def answer_question(docs, query: str, score: str, api_key):
    if not api_key:
        return "API key needed to proceed."
    
    docs = read_uploaded_docs(docs) if docs else read_docs(dir_path=dir_path)

    match score:
        case 'BM25': bot = QuestionAnsweringBot(docs, 0, api_key)
        case 'Dense': bot = QuestionAnsweringBot(docs, 1, api_key)
        case 'Both': bot = QuestionAnsweringBot(docs, 2, api_key)

    answer = bot.answer_question(question=query)
    return answer


with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown(
        """
        # Question Answering Bot

        This bot uses default doucuments or those you provided to answer questions based on their content.  
        You can select from the following scoring methods for retrieving the context:  
        - **BM25 scores**  
        - **Dense retriever**  
        - **Hybrid approach** (both BM25 and dense retriever combined).  

        ## Instructions  
        - Enter your **Groq API Key** in the textbox below.  
        - The API key can be generated using [this link](https://console.groq.com/keys).  
        - Input your query and select the scoring method to receive an answer.  
        - Ask questions directly based on files given in **docs** directory in my [github repository](https://github.com/olenkapyrih/RAG/tree/master) 
        - Or upload your files and use them as context. Just remember that the only allowed format is **.txt**
        """
    )

    uploaded_docs = gr.File(
        label="Upload Documents",
        file_types=[".txt"],
        file_count="multiple"
    )
    
    api_key = gr.Textbox(
        label='Groq API Key',
        placeholder="Enter your Groq API Key securely here.",
        type="password"
        )

    query = gr.Textbox(
        label='Query',
        placeholder="Ask a question. \
            Ex: Does a slavery still exist? Tell me about it."
        )

    score = gr.Radio(
        choices=["BM25", "Dense", "Both"],
        label="Select Scoring Method",
        value="Both"
        )
    

    outp = gr.Textbox(label='Answer', lines=6)
    button = gr.Button(value='Submit', variant='primary', key='enter')
    button.click(answer_question, inputs=[uploaded_docs, query, score, api_key], outputs=outp, show_progress=True)


demo.launch(share=True)
