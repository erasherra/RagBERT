import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

def ollama_query(template="", model="llama3:8b-instruct-q4_0", query=""):
    
    template = """{question}"""

    prompt = ChatPromptTemplate.from_template(template)

    model = OllamaLLM(model="llama3:8b-instruct-q4_0")

    chain = prompt | model

    response = chain.invoke({"question": query})

    #print(response)
    return response

def get_highest_scores(input_list, topk=2):
    highest_scores = sorted(input_list, key=lambda x: x['score'], reverse=True)[:topk]
    return highest_scores



def get_chunk(label, chunk_map=[], source="chunks"):
    # Find the matching chunk files for the given label
    matching_chunks = [chunk for chunk in chunk_map if chunk['label'] == label]
    print(label, matching_chunks)
    print(chunk_map)
    # Extract the file name from the first matching chunk (assuming there is only one)
    file_name = matching_chunks[0]['file']

    # Construct the full path of the file
    file_path = os.path.join(source, file_name)

    # Read the content of the file
    with open(file_path, 'r') as f:
        content = f.read()

    return content

def RagBERT(classifier, topk=2, query="", chunk_map=[], source="chunks"):
    
    preds = classifier(query, return_all_scores=True)
    print(preds)
    highest_scores = get_highest_scores(preds[0], topk)
    context = ""
    sources = []
    for label in highest_scores:
        c = get_chunk(label['label'], chunk_map=chunk_map, source=source)
        sources.append(c)
        context += f"""
        {c}
        
        """

    fina_qury = f"""
    {context}

    {query}
    """

    print("final_query: ", fina_qury)
    response = ollama_query(template="", model="llama3:8b-instruct-q4_0", query=fina_qury)

    return response, sources, query
