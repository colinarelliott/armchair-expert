# RAG PIPELINE TUTORIAL
# https://haystack.deepset.ai/tutorials/27_first_rag_pipeline

# Basic Imports.
import os
from dotenv import load_dotenv

## Step 1: Install Haystack

# Initialize a DocumentStore to index documents
from haystack.document_stores.in_memory import InMemoryDocumentStore
document_store = InMemoryDocumentStore()

# Fetch the data and convert it into Haystack Documents:
from datasets import load_dataset
from haystack import Document


# ORIGINAL DATASET: "bilgeyucel/seven-wonders"
dataset = load_dataset("pszemraj/booksum-short", split="train")
docs = [Document(content=doc["summary"], meta=doc["book_id"]) for doc in dataset]


# Initialize document embedder "SentenceTransformersDocumentEmbedder"
from haystack.components.embedders import SentenceTransformersDocumentEmbedder

doc_embedder = SentenceTransformersDocumentEmbedder(model="sentence-transformers/all-MiniLM-L6-v2")
doc_embedder.warm_up()

# Run doc_embedder and write documents to DocumentStore
docs_with_embeddings = doc_embedder.run(docs)
document_store.write_documents(docs_with_embeddings["documents"])

## Build RAG (Retrieval Augmented Generation) pipeline

# Initialize a text embedder to create embedding for user query
from haystack.components.embedders import SentenceTransformersTextEmbedder
text_embedder = SentenceTransformersTextEmbedder(model="sentence-transformers/all-MiniLM-L6-v2")

# initialize the retriever
from haystack.components.retrievers.in_memory import InMemoryEmbeddingRetriever
retriever = InMemoryEmbeddingRetriever(document_store)

# Define template prompt
from haystack.components.builders import PromptBuilder
template = """
Given the following information, answer the question.

Context:
{% for document in documents %}
    {{ document.content }}
{% endfor %}

Question: {{question}}
Answer:
"""
prompt_builder = PromptBuilder(template=template)

# Initialize the RAG generator
from haystack.components.generators import OpenAIGenerator

# grab the OpenAI API key from the environment if it exists
dotenv = load_dotenv() if load_dotenv() else None

# GET THIS OUTTA HERE LATER
if "OPENAI_API_KEY" not in os.environ:
    if dotenv is None or "OPENAI_API_KEY" not in dotenv:
        raise ValueError("You need to set your OpenAI API key in the environment variable OPENAI_API_KEY or in a file called '.env'")
    else:
        os.environ["OPENAI_API_KEY"] = dotenv["OPENAI_API_KEY"]
generator = OpenAIGenerator(model="gpt-3.5-turbo")

# Build the pipeline
from haystack import Pipeline
basic_rag_pipeline = Pipeline()

# Add components to pipeline
basic_rag_pipeline.add_component("text_embedder", text_embedder)
basic_rag_pipeline.add_component("retriever", retriever)
basic_rag_pipeline.add_component("prompt_builder", prompt_builder)
basic_rag_pipeline.add_component("llm", generator)

# Connect the components to each other
basic_rag_pipeline.connect("text_embedder.embedding", "retriever.query_embedding")
basic_rag_pipeline.connect("retriever", "prompt_builder.documents")
basic_rag_pipeline.connect("prompt_builder", "llm")