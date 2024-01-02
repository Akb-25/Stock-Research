import os
import google.generativeai as palm
from langchain.document_loaders import UnstructuredURLLoader,UnstructuredFileLoader,UnstructuredCSVLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import pickle 
import faiss
from langchain.vectorstores import faiss
from langchain.embeddings import GooglePalmEmbeddings
from langchain.chains.question_answering import load_qa_chain
from langchain.indexes import VectorstoreIndexCreator
from langchain.chains import RetrievalQA
from langchain.llms import google_palm
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.chains.summarize import load_summarize_chain
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

# def csv_query(file):
#     # loaders=CSVLoader(f"./{file}")
#     # data=loaders.load()
#     loaders=[UnstructuredCSVLoader(f"./{file}")]
#     index=VectorstoreIndexCreator(
#         embedding=GooglePalmEmbeddings(),
#         text_splitter=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=50)
#     ).from_loaders(loaders)
#     chain=RetrievalQA.from_chain_type(llm=llm,
#                                   chain_type="stuff",
#                                   retriever=index.vectorstore.as_retriever(),
#                                   input_key="question")
#     query=input("Tell me a query \n")
#     answer=chain.run(query)
#     print(answer)
def csv_query(file, context=None):
    # Load data and create index (unchanged)
    loaders = [UnstructuredCSVLoader(f"./{file}")]
    index = VectorstoreIndexCreator(
        embedding=GooglePalmEmbeddings(),
        text_splitter=RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    ).from_loaders(loaders)
    chain = RetrievalQA.from_chain_type(llm=llm,
                                         chain_type="stuff",
                                         retriever=index.vectorstore.as_retriever(),
                                         input_key="question")

    while True:  # Create a continuous loop
        # Handle query and context
        # if context:
            # query = input(f"Anything else related to this? {context} \n")  # Prompt based on context
        # else:
        query = input("Tell me a query \n")  # Initial query

        if query.lower() in ["quit", "stop", "exit"]:  # Allow for exit
            break

        # Append context to query if available
        # if context:
            # query = f"{context} {query}"

        # Run the retrieval model and update context
        answer = chain.run(query)
        # context = f"{query} {answer}" 

        print(answer)

    # return context  # Return updated context for potential future use

def summarize(file):
    loaders=UnstructuredCSVLoader(f"./{file}")
    docs=loaders.load()
    chain=load_summarize_chain(llm,chain_type="stuff")
    print(chain.run(docs))
    
def random():
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
    # company="RELIANCE"
    # url=get_url(company)
    # data=website_information(url)
    # with open("company_data.txt","w",encoding="utf-8") as f:
    #     for p in data:
    #         f.write(p)
    # query_data(company)
    file = "article_urls_information.csv"
    csv_query(file,None)
    # summarize(file)