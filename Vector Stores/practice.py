# ================================
# 1️⃣ Install required packages
# ================================
# Run these in Colab or Jupyter

# !pip install langchain chromadb sentence-transformers faiss-cpu

# ================================
# 2️⃣ Imports
# ================================

from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma, FAISS

# ================================
# 3️⃣ Create embedding model
# ================================

embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# ================================
# 4️⃣ Sample documents
# ================================

documents = [
    "Vector databases store embeddings efficiently.",
    "Embeddings help machines understand semantic meaning.",
    "FAISS is a library for similarity search at scale.",
    "Chroma is an open-source vector store.",
    "Retriever fetches relevant documents from a vector database."
]

# ================================
# 5️⃣ Create a Chroma vector store
# ================================

print("\n🟢 Creating Chroma store...")
chroma_store = Chroma.from_texts(documents, embedding_model)
print("Chroma store created!")

# ================================
# 6️⃣ Similarity search with Chroma
# ================================

query = "How do you store embeddings?"
results = chroma_store.similarity_search(query, k=2)
print("\n🔍 Chroma similarity search results:")
for r in results:
    print("-", r.page_content)

# ================================
# 7️⃣ Create a FAISS vector store
# ================================

print("\n🟢 Creating FAISS store...")
faiss_store = FAISS.from_texts(documents, embedding_model)
print("FAISS store created!")

# ================================
# 8️⃣ Similarity search with FAISS
# ================================

results = faiss_store.similarity_search(query, k=2)
print("\n🔍 FAISS similarity search results:")
for r in results:
    print("-", r.page_content)

# ================================
# 9️⃣ Use retriever abstraction
# ================================

chroma_retriever = chroma_store.as_retriever()
faiss_retriever = faiss_store.as_retriever()

print("\n✅ Using retriever with Chroma:")
print(chroma_retriever.get_relevant_documents(query))

print("\n✅ Using retriever with FAISS:")
print(faiss_retriever.get_relevant_documents(query))
