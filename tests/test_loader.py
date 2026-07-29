from src.rag.loader import DocumentLoader

loader = DocumentLoader()

docs = loader.load_documents()

print(f"Total Documents: {len(docs)}")

for doc in docs:
    print("=" * 50)
    print(doc.metadata)
    print(doc.page_content[:200])
