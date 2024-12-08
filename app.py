import gradio as gr
from rag import QuestionAnsweringBot
from rag import read_docs, dir_path


def answer_question(query, score):
    docs = read_docs(dir_path=dir_path)

    match score:
        case 'BM25': bot = QuestionAnsweringBot(docs, 0)
        case 'Semantic': bot = QuestionAnsweringBot(docs, 1)
        case 'Both': bot = QuestionAnsweringBot(docs, 2)

    answer = bot.answer_question(question=query)
    return answer


with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown(
        """
        # Question Answering Bot
        This bot uses your provided documents \
        to answer questions based on their content.\n
        You can select either you want to use bm25 scores \
        or semantic scores for retreiving the context.\n
        There also is a possibility to use the hybrid approach \
        - bm25 and semantic scores, both.\n
        Enter a query below to see the bot's response.
        """
    )

    query = gr.Textbox(
        label='Query',
        placeholder="Ask a question. \
            Ex: Does a slavery still exist? Tell me about it.")

    score = gr.Radio(
        choices=["BM25", "Semantic", "Both"],
        label="Select Scoring Method",
        value="Both"
        )

    outp = gr.Textbox(label='Answer', lines=6)
    button = gr.Button(value='Submit', variant='primary', key='enter')
    button.click(answer_question, inputs=[query, score], outputs=outp, show_progress=True)


demo.launch(debug=True)
