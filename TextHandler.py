from services.first.RemoveStopWords import removeStopWords
from services.first.Lemmatizer import lemmatizer
from services.first.Stemmer import stemmer
from services.first.ToLowerCase import toLowerCase
from services.first.Tokenizer import tokenizer
from pydantic import BaseModel


# initialling connection
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(CORSMiddleware , allow_origins=["*"] , allow_credentials=True , allow_methods=["*"] , allow_headers=["*"])


class Request (BaseModel):
    query:   str


@app.post("/textHandler")
async def textHandler(request : Request): 
    corpus = {}
    corpus['query'] = request.query
    corpus = toLowerCase(corpus)
    corpus = tokenizer(corpus)
    corpus = removeStopWords(corpus)
    corpus = stemmer(corpus)
    corpus = lemmatizer(corpus)

    # join results 
    for course_id ,clean_course_title in corpus.items():
        corpus[course_id] = " ".join(clean_course_title)

    return corpus