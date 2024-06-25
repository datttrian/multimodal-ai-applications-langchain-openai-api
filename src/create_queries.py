import os

import openai
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import DocArrayInMemorySearch
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA

load_dotenv()
openai.api_key = os.environ["OPENAI_API_KEY"]

# Create a new instance of the TextLoader class, specifying the directory
# containing the text files
loader = TextLoader("./files/transcripts/transcript.txt")  # added/edited

# Load the documents from the specified directory using the TextLoader instance

docs = loader.load()

# Create a new DocArrayInMemorySearch instance from the specified documents
# and embeddings
db = DocArrayInMemorySearch.from_documents(
    docs,
    OpenAIEmbeddings()
)

# Convert the DocArrayInMemorySearch instance to a retriever
retriever = db.as_retriever()

# Create a new ChatOpenAI instance with a temperature of 0.0
llm = ChatOpenAI(temperature=0.0)

# Create a new RetrievalQA instance with the specified parameters
qa_stuff = RetrievalQA.from_chain_type(
    # The ChatOpenAI instance to use for generating responses
    llm=llm,
    # The type of chain to use for the QA system
    chain_type="stuff",
    # The retriever to use for retrieving relevant documents
    retriever=retriever,
    # Whether to print verbose output during retrieval and generation
    verbose=True
)

# Set the query to be used for the QA system
query = "What is this tutorial about?"

# Run the query through the RetrievalQA instance and store the response
response = qa_stuff.run(query)

# Print the response to the console
print(response)

# Set the query to be used for the QA system
query = "What is the difference between a training set and test set?"

# Run the query through the RetrievalQA instance and store the response
response = qa_stuff.run(query)

# Print the response to the console
print(response)

# Set the query to be used for the QA system
query = "Who should watch this lesson?"

# Run the query through the RetrievalQA instance and store the response
response = qa_stuff.run(query)

# Print the response to the console
print(response)

# Set the query to be used for the QA system
query = "Who is the greatest football team on earth?"

# Run the query through the RetrievalQA instance and store the response
response = qa_stuff.run(query)

# Print the response to the console
print(response)

# Set the query to be used for the QA system
query = "How long is the circumference of the earth?"

# Run the query through the RetrievalQA instance and store the response
response = qa_stuff.run(query)

# Print the response to the console
print(response)
