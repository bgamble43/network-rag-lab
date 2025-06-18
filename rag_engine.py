import os
from dotenv import load_dotenv
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_community.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.chains import RetrievalQA
from langchain_community.llms import OpenAI

def build_rag_chain(docs_path="./docs", chunk_size=500):
    load_dotenv()
    loader = DirectoryLoader(
        "./docs",
        glob="**/*.md",
        loader_cls=TextLoader,
        use_multithreading=True
    )

    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=50)
    chunks = splitter.split_documents(docs)

    vectorstore = FAISS.from_documents(chunks, OpenAIEmbeddings())
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    return RetrievalQA.from_chain_type(
        llm=OpenAI(temperature=0),
        retriever=retriever,
        return_source_documents=True
    )
