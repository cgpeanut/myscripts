from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA

prompt = "What is the difference between an adverb and an adjective?"
llm = Ollama(model="mistral")
qa = RetrievalQA.from_chain_type(
   llm=llm,
   chain_type="stuff",
   retriever=retriever,
   return_source_documents=True,
                        )
response = qa(prompt)
