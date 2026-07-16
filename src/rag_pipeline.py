from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

class RAGPipeline:

    def __init__(self):

        self.llm = ChatGroq(
            model="llama-3.3-70b-versatile",
            temperature=0,
            max_tokens=1024
        )

    def generate_answer(self, query, docs):

        context = "\n\n".join(
            [doc.page_content for doc in docs]
        )

        prompt = f"""
You are an expert document assistant.

Use ONLY the provided context.

Answer the user's question in a clear and concise manner.

Do not copy sentences directly unless necessary.

If the answer is not found in the context, say:
'I could not find that information in the document.'

Context:
{context}

Question:
{query}

Detailed Answer:
"""

        response = self.llm.invoke(prompt)

        return response.content