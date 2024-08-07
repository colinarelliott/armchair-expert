from haystack.components.writers import DocumentWriter
from haystack.components.converters import MarkdownToDocument, PyPDFToDocument, TextFileToDocument
from haystack.components.preprocessors import DocumentSplitter, DocumentCleaner
from haystack.components.routers import FileTypeRouter
from haystack.components.joiners import DocumentJoiner
from haystack.components.embedders import SentenceTransformersDocumentEmbedder
from haystack import Pipeline
from haystack.document_stores.in_memory import InMemoryDocumentStore

output_dir = "processing"

# pass off between the two functions for modularity
pipe = Pipeline()

def preload(loaded = False):
    # create a pipeline to index documents
    document_store = InMemoryDocumentStore()
    file_type_router = FileTypeRouter(mime_types=["text/plain", "application/pdf", "text/markdown"])
    text_file_converter = TextFileToDocument()
    markdown_converter = MarkdownToDocument()
    pdf_converter = PyPDFToDocument()
    document_joiner = DocumentJoiner()

    # DocumentCleaner removes whitespace. Then this DocumentSplitter breaks them into chunks of 150 words
    document_cleaner = DocumentCleaner()
    document_splitter = DocumentSplitter(split_by="word", split_length=150, split_overlap=50)

    # add a SentenceTransformersDocumentEmbedder to create embeddings from the documents
    document_embedder = SentenceTransformersDocumentEmbedder(model="sentence-transformers/all-MiniLM-L6-v2")
    document_writer = DocumentWriter(document_store)

    # add components to the indexing pipeline
    preprocessing_pipeline = Pipeline()
    preprocessing_pipeline.add_component(instance=file_type_router, name="file_type_router")
    preprocessing_pipeline.add_component(instance=text_file_converter, name="text_file_converter")
    preprocessing_pipeline.add_component(instance=markdown_converter, name="markdown_converter")
    preprocessing_pipeline.add_component(instance=pdf_converter, name="pypdf_converter")
    preprocessing_pipeline.add_component(instance=document_joiner, name="document_joiner")
    preprocessing_pipeline.add_component(instance=document_cleaner, name="document_cleaner")
    preprocessing_pipeline.add_component(instance=document_splitter, name="document_splitter")
    preprocessing_pipeline.add_component(instance=document_embedder, name="document_embedder")
    preprocessing_pipeline.add_component(instance=document_writer, name="document_writer")

    # connect components
    preprocessing_pipeline.connect("file_type_router.text/plain", "text_file_converter.sources")
    preprocessing_pipeline.connect("file_type_router.application/pdf", "pypdf_converter.sources")
    preprocessing_pipeline.connect("file_type_router.text/markdown", "markdown_converter.sources")
    preprocessing_pipeline.connect("text_file_converter", "document_joiner")
    preprocessing_pipeline.connect("pypdf_converter", "document_joiner")
    preprocessing_pipeline.connect("markdown_converter", "document_joiner")
    preprocessing_pipeline.connect("document_joiner", "document_cleaner")
    preprocessing_pipeline.connect("document_cleaner", "document_splitter")
    preprocessing_pipeline.connect("document_splitter", "document_embedder")
    preprocessing_pipeline.connect("document_embedder", "document_writer")

    from pathlib import Path
    preprocessing_pipeline.run({"file_type_router": {"sources": list(Path(output_dir).glob("**/*"))}})

    import os
    from dotenv import load_dotenv

    # grab the OpenAI API key from the environment if it exists
    dotenv = load_dotenv() if load_dotenv() else None

    # Get token from environment variable or .env file
    if "HF_API_TOKEN" not in os.environ:
        if dotenv is None or "HF_API_TOKEN" not in dotenv:
            raise ValueError("You need to set your Hugging Face API token in the environment variable OPENAI_API_KEY or in a file called '.env'")
        else:
            os.environ["HF_API_TOKEN"] = dotenv["HF_API_TOKEN"]

    from haystack.components.embedders import SentenceTransformersTextEmbedder
    from haystack.components.retrievers.in_memory import InMemoryEmbeddingRetriever
    from haystack.components.builders import PromptBuilder
    from haystack.components.generators import HuggingFaceAPIGenerator

    template = """
    You are a professional in the related field, you are asked to answer the following question.

    Context:
    {% for document in documents %}
        {{ document.content }}
    {% endfor %}

    Question: {{ question }}
    Answer:
    """
    pipe.add_component("embedder", SentenceTransformersTextEmbedder(model="sentence-transformers/all-MiniLM-L6-v2"))
    pipe.add_component("retriever", InMemoryEmbeddingRetriever(document_store=document_store))
    pipe.add_component("prompt_builder", PromptBuilder(template=template))
    pipe.add_component(
        "llm",
        HuggingFaceAPIGenerator(api_type="serverless_inference_api", api_params={"model": "HuggingFaceH4/zephyr-7b-beta"}),
    )

    pipe.connect("embedder.embedding", "retriever.query_embedding")
    pipe.connect("retriever", "prompt_builder.documents")
    pipe.connect("prompt_builder", "llm")

    print("Welcome to Armchair Expert. You loaded the following files:\n")
    for file in list(Path(output_dir).glob("**/*")):
        print(file)
    loaded = True

    return loaded

def ask(message):
    print("Loading...")
    response = pipe.run(
        {
            "embedder": {"text": message},
            "prompt_builder": {"question": message},
            "llm": {"generation_kwargs": {"max_new_tokens": 350}},
        }
    )

    if "llm" in response and "replies" in response["llm"] and len(response["llm"]["replies"]) > 0:
        print(response["llm"]["replies"][0])
        return response["llm"]["replies"][0]
