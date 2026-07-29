"""
RAG Chain
"""

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from src.models.llm import LLMFactory
from src.rag.retriever import DocumentRetriever


class RAGChain:
    """
    Retrieval-Augmented Generation Chain.
    """

    def __init__(self):

        self.llm = LLMFactory.create()

        self.retriever = DocumentRetriever()

        self.prompt = ChatPromptTemplate.from_template(
            """
You are an AI Supply Chain Assistant.

Answer the user's question ONLY using the supplied context.

If the answer is not available in the context,
reply:

"I don't have enough information in the knowledge base."

Context:
{context}

Question:
{question}
"""
        )

        self.parser = StrOutputParser()

        self.chain = (
            self.prompt
            | self.llm
            | self.parser
        )

    def invoke(self, question: str):

        docs = self.retriever.retrieve(question)

        context = "\n\n".join(
            doc.page_content
            for doc in docs
        )

        return self.chain.invoke(
            {
                "context": context,
                "question": question,
            }
        )
