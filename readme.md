# Armchair Expert 
**A ReactPy App for chatting with an AI about specific provided documents, uses Haystack AI as a lightweight LLM Vector Database Builder**
- Simple implementation of a RAG (Retrieval Augmented Generator) model LLM that reads from Hugging Face models (`basicRAG.py`)
- OpenAI API Key Input Required in `.env` file or `$PATH`
- `query.py` contains a simple call to the RAG model using a customizable query string

## Installation
1. Install the Python Requirements
- Windows / Linux: `pip install -r requirements.txt`
- MacOS: `python3 pip install -r requirements.txt`
2. Add a file called '.env' and input your OpenAI API Key & HF Token as shown:
- `OPENAI_API_KEY="your_key"`
- `HF_API_TOKEN="your_token"`
3. Run the app
- Windows / Linux: `python reactApp.py`
- MacOS: `python3 reactApp.py`
4. Navigate to `http://127.0.0.1:8000`
