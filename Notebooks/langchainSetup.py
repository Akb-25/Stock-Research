import os
import google.generativeai as palm
from langchain.document_loaders import UnstructuredURLLoader,UnstructuredFileLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import pickle 
import faiss
from langchain.vectorstores import faiss
from langchain.embeddings import GooglePalmEmbeddings
from langchain.chains.question_answering import load_qa_chain
from langchain.indexes import VectorstoreIndexCreator
from langchain.chains import RetrievalQA
from langchain.llms import google_palm
from website_data_collection import website_information
from url_obtainer import get_url

google_api_key=os.environ["GOOGLE_API_KEY"]="AIzaSyCEXDkHy_D1HcgADqkeCBQWOIqsz1GiFPA"
llm=google_palm.GooglePalm()
llm.temperature=0.2
def query_data(company):
    loaders=[UnstructuredFileLoader("./company_data.txt")]
    index=VectorstoreIndexCreator(
        embedding=GooglePalmEmbeddings(),
        text_splitter=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=50)
    ).from_loaders(loaders)
    chain=RetrievalQA.from_chain_type(llm=llm,
                                  chain_type="stuff",
                                  retriever=index.vectorstore.as_retriever(),
                                  input_key="question")
    query=input("Tell me a query \n")
    answer=chain.run(query)
    print(answer)
# data=loaders.load()
# embeddings=GooglePalmEmbeddings()
# text_splitter=RecursiveCharacterTextSplitter(separators='\n',
                                            #  chunk_size=450,
                                            #  chunk_overlap=50)
# docs=text_splitter.split_documents(data)

# vectorStore_palm=GooglePalmEmbeddings.embed_documents(docs,embeddings)
# with open("faiss_store_palm.pkl","wb") as f:
    # vectorStore=pickle.dump(vectorStore_palm,f)
    print("......Successfully Completed......")

if __name__ == "__main__":
    company="RELIANCE"
    url=get_url(company)
    data=website_information(url)
    with open("company_data.txt","w",encoding="utf-8") as f:
        for p in data:
            f.write(p)
    query_data(company)