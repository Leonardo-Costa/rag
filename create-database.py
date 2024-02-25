import os
import shutil
from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from shared.constants.constants import CHROMA_PATH

DATA_PATH = "data/books"


def main():
    generateDataStore()


def generateDataStore():
    documents = loadDocuments()
    chunks = splitText(documents)
    saveToChroma(chunks)


def loadDocuments():
    loader = DirectoryLoader(DATA_PATH, glob="*.md")
    documents = loader.load()
    return documents


def splitText(documents):
    textSplitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, chunk_overlap=100, length_function=len, add_start_index=True
    )
    chunks = textSplitter.split_documents(documents)
    print(f"Quebrando {len(documents)} documentos em {len(chunks)} chunks")
    return chunks


def saveToChroma(chunks):
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)

    db = Chroma.from_documents(
        chunks, OpenAIEmbeddings(), persist_directory=CHROMA_PATH
    )

    db.persist()
    print(f"Chroma gerado em {CHROMA_PATH}")


if __name__ == "__main__":
    main()
