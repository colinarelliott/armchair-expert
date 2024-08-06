from basicRAG import basic_rag_pipeline

question = "What is Dracula about? Who dies?"

response = basic_rag_pipeline.run({"text_embedder": {"text": question}, "prompt_builder": {"question": question}})
print(response["llm"]["replies"][0])
