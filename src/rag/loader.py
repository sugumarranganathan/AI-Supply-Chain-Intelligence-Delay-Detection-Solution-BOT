"""
Document Loader for RAG
"""

from pathlib import Path

from langchain_community.document_loaders import (
    CSVLoader,
    PyPDFLoader,
    TextLoader,
)


class DocumentLoader:
    """
    Load all supported documents from the documents folder.
    """

    def __init__(self, documents_path: str = "documents"):
        self.documents_path = Path(documents_path)

    def load_documents(self):
        """
        Load PDF, TXT and CSV documents.
        """

        documents = []

        if not self.documents_path.exists():
            raise FileNotFoundError(
                f"Documents folder not found: {self.documents_path}"
            )

        for file in self.documents_path.iterdir():

            suffix = file.suffix.lower()

            if suffix == ".pdf":
                loader = PyPDFLoader(str(file))
                documents.extend(loader.load())

            elif suffix == ".txt":
                loader = TextLoader(
                    str(file),
                    encoding="utf-8",
                )
                documents.extend(loader.load())

            elif suffix == ".csv":
                loader = CSVLoader(str(file))
                documents.extend(loader.load())

        return documents
