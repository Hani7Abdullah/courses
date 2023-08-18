from nltk.stem import PorterStemmer

def stemmer(corpus):
    filtered_sentence_stem = []
    ps = PorterStemmer()

    for course_id, clean_course_title in corpus.items():
        for w in clean_course_title:
            filtered_sentence_stem.append(ps.stem(w))
        corpus[course_id] = filtered_sentence_stem
        filtered_sentence_stem = []
    
    return corpus

