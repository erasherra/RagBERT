The following project is research conducted by the SipeAI team.


# TLDR Description (Standard RAG vs RAGBERT)

The staged problem is to find the correct chunk without using a standard vector database.


### Data 

The used data is from Finland's social administration guide/rule. 

(https://vakehyva.fi/fi/lakisaateiset-asiakirjat)

Only a few pages were used for the chunking process which were done manually. There were 6 chunks which both the RagBERT and Embedchain used.

### Models

The RagBERT project utilizes quantization of Llama 3.1 via Ollama. Choosed BERT model is TurkuNLP FinBERT (https://github.com/TurkuNLP/FinBERT).

It is evaluated against embedchain (using default settings, OpenAI API).


## Concept

This project introduces the RAG concept with the BRRT model.
The simplified cycle of the RagBERT is as follows:
choose document(s)
split them to chunks (so far you have to do it manually)
select the LLM model and generate X amount of data (e.g. questions that point to the correct chunk)
format the data with labels (e.g. path to chunk)
split the dataset to train, test, validate
train bert model
use it to pick the chunk based on the query which is given


## Evaluation

Deepeval was used for evaluating the context relevance of the both systems. The average context relevance results were as follows:


### Embedchain with standard settings (RAG + VectorDB)

#### 15%


### RagBERT (RAG + BERT)

#### 70%

The evaluation for this simple test scenario shows increase when using RagBERT method instead of the classic vector DB approach (in the context of the Finnish legal guide for administration).

## Discussion

For both approaches neither one was fully optimized and tested. No extra configuration was done for embedchain. However, the RagBERT was able to increase the context relevance by an average of +55%.

The synthetic data in this project is questions but could be conversations between models, summary of the chunk, or something different. This area could require more testing. Also, the limit for chunk size. However, the RagBERT could be scaled by utilizing more BERT models in theory.

The RagBERT solution requires more resources when compared against RAG that utilizes vector databases.


