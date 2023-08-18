import requests
import json
from enum import Enum
from pydantic import BaseModel
from services.first.Lemmatizer import lemmatizer
from services.first.RemoveStopWords import removeStopWords
from services.first.Stemmer import stemmer
from services.first.ToLowerCase import toLowerCase
from services.first.Tokenizer import tokenizer
from services.second.GetInvertedIndex import getInvertedIndex
from services.second.CosineSimilarity import getSimilarity



# initialling connection
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(CORSMiddleware , allow_origins=["*"] , allow_credentials=True , allow_methods=["*"] , allow_headers=["*"])

f = open('config.json')
config = json.load(f)
f.close()

class datasets(str, Enum):
    courses    = "courses"

class Request (BaseModel):
    dataset: datasets
    query:   str


def textHandler(request : Request): 
    result = {}
    result['query'] = request.query
    result = toLowerCase(result)
    result = tokenizer(result)
    result = removeStopWords(result)
    result = stemmer(result)
    result = lemmatizer(result)

    # join results 
    for course_id ,clean_course_title in result.items():
        result[course_id] = " ".join(clean_course_title)

    return result



@app.post("/search")
def search(request: Request):

    # text handling
    textHandling = textHandler(request)
    query_index = getInvertedIndex(textHandling ,"online" ,request.dataset)

    # results by similarity
    results = getSimilarity(query_index ,request.dataset)

    return results



