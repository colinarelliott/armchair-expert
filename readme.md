# Armchair Expert (Haystack AI Vector Database LLM)
- Simple implementation of a RAG (Retrieval Augmented Generator) model LLM that reads from Hugging Face models (`basicRAG.py`)
- OpenAI API Key Input Required in `.env` file or `$PATH`
- `query.py` contains a simple call to the RAG model using a customizable query string

## Installation
1. Install the Python Requirements
- Windows / Linux: `pip install -r requirements.txt`
- MacOS: `python3 pip install -r requirements.txt`
2. Add a file called '.env' and input your OpenAI API Key as shown:
- `OPENAI_API_KEY="your_key"`
3. _Set your question_ and dataset (optional) (dataset in `basicRAG.py`, question in `query.py`)
4. Run the app
- Windows / Linux: `python query.py`
- MacOS: `python3 query.py`
