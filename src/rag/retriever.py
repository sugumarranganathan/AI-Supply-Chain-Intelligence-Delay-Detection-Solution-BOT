"""
Document Retriever
"""

from langchain_community.vectorstores import FAISS

from src.rag.embeddings import EmbeddingModel


VECTOR_DB_PATH = "data/vector_store"


class DocumentRetriever:
    """
    Retrieve relevant documents from the FAISS vector database.
    """

    def __init__(self):

        self.embeddings = EmbeddingModel().get_embeddings()

        self.vector_db = FAISS.load_local(
            VECTOR_DB_PATH,
            self.embeddings,
            allow_dangerous_deserialization=True,
        )

        self.retriever = self.vector_db.as_retriever(
            search_type="similarity",
            search_kwargs={
                "k": 3,
            },
        )

    def retrieve(self, query: str):
        """
        Retrieve the top matching document chunks.
        """

        documents = self.retriever.invoke(query)

        return documents
