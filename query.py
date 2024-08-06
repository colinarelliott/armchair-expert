from basicRAG import basic_rag_pipeline

# INPUT QUESTION HERE ______________________________________
question = "Who's Zeus' father?"
#___________________________________________________________

#structure data and run the pipeline
input_data = {
    "text_embedder": {"text": question},
    "prompt_builder": {"question": question}
}
response = basic_rag_pipeline.run(input_data)

# Ensure the output structure is accessed correctly
if "llm" in response and "replies" in response["llm"] and len(response["llm"]["replies"]) > 0:
    print(response["llm"]["replies"][0])
else:
    print("Unexpected response structure:", response)