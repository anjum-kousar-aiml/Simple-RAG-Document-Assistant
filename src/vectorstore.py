from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings


class FaissVectorStore:

    def __init__(self):

        self.embedding_model = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

    def create_vectorstore(self, chunks):

        db = FAISS.from_documents(
            chunks,
            self.embedding_model
        )

        db.save_local("faiss_store")

        return db

    def load_vectorstore(self):

        return FAISS.load_local(
            "faiss_store",
            self.embedding_model,
            allow_dangerous_deserialization=True
        )