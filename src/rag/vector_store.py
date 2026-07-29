"""
FAISS Vector Store
"""

from pathlib import Path

from langchain_community.vectorstores import FAISS

from src.rag.loader import DocumentLoader
from src.rag.splitter import DocumentSplitter
from src.rag.embeddings import EmbeddingModel


VECTOR_DB_PATH = "data/vector_store"


class VectorStore:
    """
    Build and save the FAISS vector database.
    """

    def __init__(self):
        self.loader = DocumentLoader()
        self.splitter = DocumentSplitter()
        self.embedding_model = EmbeddingModel()

    def build_vector_store(self):
        """
        Create FAISS vector database.
        """

        print("Loading documents...")

        documents = self.loader.load_documents()

        print(f"Loaded {len(documents)} documents.")

        print("Splitting documents...")

        chunks = self.splitter.split_documents(documents)

        print(f"Created {len(chunks)} chunks.")

        print("Creating embeddings...")

        embeddings = self.embedding_model.get_embeddings()

        print("Building FAISS index...")

        vector_db = FAISS.from_documents(
            documents=chunks,
            embedding=embeddings,
        )

        Path(VECTOR_DB_PATH).mkdir(
            parents=True,
            exist_ok=True,
        )

        vector_db.save_local(VECTOR_DB_PATH)

        print(f"Vector database saved to: {VECTOR_DB_PATH}")

        return vector_db
