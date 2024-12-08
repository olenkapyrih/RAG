import gradio as gr
from rag import QuestionAnsweringBot
from rag import read_docs, dir_path


def answer_question(query: str, score: str, api_key):
    if not api_key:
        return "API key needed to proceed."
    
    docs = read_docs(dir_path=dir_path)

    match score:
        case 'BM25': bot = QuestionAnsweringBot(docs, 0, api_key)
        case 'Semantic': bot = QuestionAnsweringBot(docs, 1, api_key)
        case 'Both': bot = QuestionAnsweringBot(docs, 2, api_key)

    answer = bot.answer_question(question=query)
    return answer


with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown(
        """
        # Question Answering Bot

        This bot uses your provided documents to answer questions based on their content.  
        You can select from the following scoring methods for retrieving the context:  
        - **BM25 scores**  
        - **Semantic scores**  
        - **Hybrid approach** (both BM25 and semantic scores combined).  

        ## Instructions  
        - Enter your **Groq API Key** in the textbox below.  
        - The API key can be generated using [this link](https://console.groq.com/keys).  
        - Input your query and select the scoring method to receive an answer.  
        """
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
        choices=["BM25", "Semantic", "Both"],
        label="Select Scoring Method",
        value="Both"
        )

    outp = gr.Textbox(label='Answer', lines=6)
    button = gr.Button(value='Submit', variant='primary', key='enter')
    button.click(answer_question, inputs=[query, score, api_key], outputs=outp, show_progress=True)


demo.launch(debug=True)
