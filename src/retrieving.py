from dotenv import load_dotenv
from google import genai

class Retrieve:
    def __init__(self, vector_db, gemini_api, gemini_model):
        self.top_k = 3
        self.vector_db = vector_db
        self.gemini_api = gemini_api
        self.gemini_model = gemini_model

    def data_retrieve(self, question):
        retriever = self.vector_db.as_retriever(search_kwargs= {"k": self.top_k})
        client = genai.Client(api_key= self.gemini_api)

        while True:
            print("Ask question...")
            question = input()
            if question.lower() in ['exit', 'quit', 'stop']:
                print('Stopped')
                break

            retrieved_docs = retriever.invoke(question)

            context = '\n\n'.join(doc.page_content for doc in retrieved_docs)

            prompt = f"""
                You are a senior Real Estate Advisor chatbot.

                Your ONLY area of knowledge is:
                - Company profile
                - Company overview
                - Real estate knowledge
                - Project portfolio

                Context:
                {context}

                User Question:
                {question}

                Answer the question using the context above.
                If the context doesn't contain the answer, say so.
            """

            response = client.models.generate_content(
                model= self.gemini_model,
                contents= prompt
            )

            return response.text