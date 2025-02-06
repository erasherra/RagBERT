### TLDR Description

This project introduces RAG concept with BRRT model.

The simplefied cycle of the RagBERT is as follows:

1. choose document(s)
2. split them to chunks
3. select LLM model and generate X amount of data (e.g. questions).
4. formate the data with labels (path to chunk).
5. split the dataset to train, test, validate
6. train bert model
7. use it to pick the chunk which is given it the dataset to train, test, validate
6. train bert model
7. use it to pick the chunk which is given as a context to LLM model.


The syntetic data in this project is questuons but could be conversations between models, summary of the chunk, or something different. This could ne something to test.

The project utilizes quantization of Llama 3.1 via Ollama. Choosed BERT model is TurkuNLP FinBERT. 

Staged problem is to find a correct chunk.

## Evaluation
