"""
Document Splitter
"""

from langchain.text_splitter import RecursiveCharacterTextSplitter


class DocumentSplitter:
    """
    Split documents into smaller chunks for RAG.
    """

    def __init__(
        self,
        chunk_size: int = 1000,
        chunk_overlap: int = 200,
    ):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
        )

    def split_documents(self, documents):
        """
        Split loaded documents into chunks.
        """

        chunks = self.text_splitter.split_documents(documents)

        print(f"Created {len(chunks)} chunks.")

        return chunks
