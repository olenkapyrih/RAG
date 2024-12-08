from groq import Client
from retriever import Retriever
from typing import List
import glob

dir_path = 'docs'
groq_api_key = "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"

client = Client(
    api_key=groq_api_key
)


class QuestionAnsweringBot:

    PROMPT = """
        You are a helpful assistant that answers the questions.

        Rules:
        - Reply with answer only and nothing but answer.
        - Say 'I don`t know' if you don`t know the answer.
        - Use the provided context.
    """

    def __init__(self, docs: List[str], score: int) -> None:
        self.retriever = Retriever(docs=docs, score=score)

    def answer_question(self, question: str) -> str:
        context = self.retriever.get_docs(query=question)
        messages = [
            {
                "role": "system",
                "content": self.PROMPT
                },
            {
                "role": "user",
                "content": f"Context: {context}\nQuestion: {question}"
                }
            ]
        chat_completion = client.chat.completions.create(
            messages=messages,
            model="llama3-70b-8192"
            )

        return chat_completion.choices[0].message.content


def read_docs(dir_path) -> List[str]:
    docs = []
    for path in glob.glob(f'{dir_path}/*.txt'):
        with open(path, 'r', encoding='utf-8') as file:
            text = file.read()
            docs.append(text)
    return docs
