from nltk.tokenize import word_tokenize

def tokenizer(corpus):
    for course_id, clean_course_title in corpus.items():
        corpus[course_id] = word_tokenize(clean_course_title)
     
    return corpus        

