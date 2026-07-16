import os
import streamlit as st

from src.document_loader import load_document
from src.chunker import chunk_documents
from src.vectorstore import FaissVectorStore
from src.rag_pipeline import RAGPipeline

st.set_page_config(
    page_title="RAG Document Assistant",
    page_icon="📚"
)

st.title("📚 RAG Document Assistant")

uploaded_file = st.file_uploader(
    "Upload PDF, DOCX, TXT",
    type=["pdf", "docx", "txt"]
)

if uploaded_file:

    os.makedirs("uploads", exist_ok=True)

    file_path = os.path.join(
        "uploads",
        uploaded_file.name
    )

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("✅ Document Uploaded!")

    docs = load_document(file_path)

    chunks = chunk_documents(docs)

    vector_db = FaissVectorStore()

    db = vector_db.create_vectorstore(chunks)

    st.success("✅ Embeddings Generated!")

    query = st.text_input(
        "Ask a question about the document"
    )

    if query:

        retrieved_docs = db.similarity_search(
            query,
            k=4
        )

        rag = RAGPipeline()

        answer = rag.generate_answer(
            query,
            retrieved_docs
        )

        st.subheader("📌 Answer")

        st.write(answer)

        st.subheader("📚 Sources")

        for i, doc in enumerate(retrieved_docs):

            st.markdown(f"### Source {i+1}")

            # Document name
            source_file = os.path.basename(
                doc.metadata.get("source", "Unknown")
            )

            st.write(
                f"📄 Document: {source_file}"
            )

            # Page number
            st.write(
                f"📍 Page: {doc.metadata.get('page_label', 'N/A')}"
            )

            # Relevant chunk preview
            st.markdown("**Relevant Excerpt:**")

            st.info(
                doc.page_content[:500] + "..."
            )

            # Expandable metadata
            with st.expander("View Metadata"):

                st.json(doc.metadata)

            st.divider()