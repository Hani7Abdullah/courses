from nltk.stem import WordNetLemmatizer

def lemmatizer(corpus):
    lemmatizer = WordNetLemmatizer()
    lemmatizer_sentence = []

    for course_id, clean_course_title in corpus.items():
        for w in clean_course_title:
            lemmatizer_sentence.append(lemmatizer.lemmatize(w, pos = 'v'))
        corpus[course_id] = lemmatizer_sentence
        lemmatizer_sentence = []
        
    return corpus

