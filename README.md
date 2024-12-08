# RAG. Question answering bot.

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

Dense retriever used in this lab - sentence-transformers/all-distilroberta-v1

## Reranker

As a reranker there was used cross encoder cross-encoder/stsb-roberta-base.
## Citation
## Web UI and deployment
I used gradio lib for demo and hosting.

<iframe src="https://giphy.com/embed/hrvRc3sDrlwRQdkubT" width="270" height="480" style="" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/justviralnet-kitten-aww-cutest-hrvRc3sDrlwRQdkubT">via GIPHY</a></p>