# RAG. Question answering bot.
![](https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNXZyaTM1anczcGE0cDliYWZkNXhvY3ZrOGRzeTJ5a3EwcXl3aGVnZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/12xDxBbj7CPAOI/giphy.gif)

### Topics
  - [Data source](#data-source) ✔️
  - [Chunking](#chunking) ✔️
  - [LLM](#llm) ✔️
  - [Retriever](#retriever) ✔️
  - [Reranker](#reranker) ✔️
  - [Citation](#citation) ❌
  - [Web UI and deployment](#web-ui-and-deployment) ✔️


## Data source

I used documents found on the Internet. You can find them in **docs**  directory, and you can ask questions based on that context. There also is possibility to upload your txt file and use it as a context.

## Chunking
Chunking was performed using the same method explained in live-coding session. No other libraries were involved.

## LLM
As LLM I used pretrained model [llama3-70b-8192](https://huggingface.co/Groq/Llama-3-Groq-70B-Tool-Use).

## Retriever
Retrieving can be performed in three different ways. You can either use BM25 retriever or a dense retriever by calculating semantic scores. Using both of them in hybrid approach is also an option.

Dense retriever used in this lab - sentence-transformers/all-distilroberta-v1.

#### Here's an example when dense retriever works better than BM25:
![image_2024-12-08_21-59-16](https://github.com/user-attachments/assets/50e2b14a-dc28-4e4b-8752-90ab46d2d883)
![image_2024-12-08_22-00-02](https://github.com/user-attachments/assets/eec3f618-99f0-4b43-b6a5-573ef612ae3e)


## Reranker

As a reranker there was used cross encoder cross-encoder/stsb-roberta-base.
## Citation
## Web UI and deployment
I used gradio lib for demo and hosting.

