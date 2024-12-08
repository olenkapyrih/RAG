import torch
import numpy as np

from typing import List
from rank_bm25 import BM25Okapi
from sentence_transformers import SentenceTransformer, CrossEncoder

from chunker import chunk_documents



class Retriever:
    def __init__(self, docs: List[str], score: int) -> None:
        self.docs = chunk_documents(docs=docs)
        self.score = score
        tokenized_docs = [doc.lower().split(" ") for doc in self.docs]
        self.bm25 = BM25Okapi(tokenized_docs)
        self.sbert = SentenceTransformer(
            'sentence-transformers/all-distilroberta-v1'
            )
        self.doc_embeddings = self.sbert.encode(
            self.docs, show_progress_bar=True
            )
        self.cross_encoder = CrossEncoder("cross-encoder/stsb-roberta-base")


    def get_docs(self, query: str, n: int = 5, score: int = 2) -> List[str]:
        match score:
            case 0:
                bm25_scores = self._get_bm25_scores(query=query)
                sorted_indices = torch.Tensor.tolist(
                    np.argsort(bm25_scores)
                    )[::-1]
            case 1:
                semantic_scores = self._get_semantic_scores(query=query)
                sorted_indices = torch.Tensor.tolist(
                    np.argsort(semantic_scores)
                    )[::-1]
            case 2:
                bm25_scores = self._get_bm25_scores(query=query)
                semantic_scores = self._get_semantic_scores(query=query)
                scores = torch.tensor(0.3 * bm25_scores) + 0.7 * semantic_scores
                sorted_indices = torch.Tensor.tolist(np.argsort(scores))[::-1]

        preselected_docs = [self.docs[i] for i in sorted_indices][:n]
        result = self.rerank(query=query, docs=preselected_docs)

        return result

    def _get_bm25_scores(self, query: str) -> np.ndarray[float]:
        tokenized_query = query.lower().split(" ")
        bm25_scores = self.bm25.get_scores(tokenized_query)

        return bm25_scores

    def _get_semantic_scores(self, query: str) -> torch.Tensor:
        query_embeddings = self.sbert.encode(query)
        semantic_scores = self.sbert.similarity(
            query_embeddings, self.doc_embeddings
            )

        return semantic_scores[0]

    def rerank(self, query: str, docs: List[str]) -> List[str]:
        pairs = [(query, doc) for doc in docs]
        rerank_scores = self.cross_encoder.predict(pairs)
        reranked_docs = [doc for _, doc in sorted(zip(rerank_scores, docs), reverse=True)]

        return reranked_docs