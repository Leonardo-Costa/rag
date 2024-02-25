# Overview
This repository is dedicated to studying and implementing Retrieval-Augmented Generation (RAG), a powerful approach that combines the benefits of retrieval-based and generative models for natural language processing tasks. RAG models retrieve documents from a knowledge base to provide context for generating responses, enabling more informed and accurate outputs.

# What is RAG?
Retrieval-Augmented Generation (RAG) is a methodology that enhances the capabilities of language generation models by incorporating external information. It works by first retrieving relevant documents or text snippets from a large corpus based on the input query and then feeding this information into a generative model to produce an output that is informed by the retrieved data. This approach allows RAG models to generate more accurate, contextually relevant, and detailed responses than traditional generative models, especially in domains where specific knowledge is crucial.

# How to Use This Code
This repository contains Python code designed to create a database and perform queries using the RAG approach. The process is divided into two main scripts:

# 1. Data Store Generation
The first part of the code is responsible for generating a data store that will serve as the knowledge base for the RAG model. It involves loading documents, splitting the text into manageable chunks, and saving them into a Chroma vector store for efficient retrieval.

## Steps to Create a Database:
Document Loading: Use the DirectoryLoader class to load documents from a specified directory. In this case, we're loading Markdown files from the "data/books" directory.

## Text Splitting: The RecursiveCharacterTextSplitter is used to split the loaded documents into smaller chunks. These chunks are then processed to ensure they are of a manageable size for the model.

## Saving to Chroma: After splitting, the chunks are saved into a Chroma vector store. This involves embedding the chunks using the OpenAIEmbeddings and persisting the data in a specified directory for later retrieval.

# 2. Querying the Data Store
The second script enables querying the generated data store. It retrieves relevant document chunks based on a query and uses them as context for generating a response.

## Steps to Perform a Query:
Query Input: The script accepts a query text as input through command-line arguments.

Retrieving Relevant Chunks: It uses the Chroma vector store to find document chunks that are most relevant to the input query.

## Generating Response: 
The retrieved chunks are used as context to generate a response to the query. This step leverages the ChatOpenAI model to produce a contextually informed answer.

## Generate the Data Store:

Place your documents (in Markdown format) in the "data/books" directory.
Run the first script to load, split, and save the documents into the Chroma vector store.
Query the Data Store:

Use the second script to perform queries. Pass your query text as a command-line argument to the script.
The script will retrieve relevant document chunks and use them to generate a response.