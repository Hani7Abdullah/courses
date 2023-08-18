
from nltk.corpus import stopwords

def removeStopWords(corpus):
    stop_words = set(stopwords.words('english')+[':','`','``','!','#','$','%','^','&','*','-','+','?','/','~',']','[','}','{','"', '""',"''", "'",'.','..',',','|','(',')'])
                 
    filtered_sentence = []
    for course_id, clean_course_title in corpus.items():
        for w in clean_course_title:
            if w not in stop_words:
                filtered_sentence.append(w)
        corpus[course_id] = filtered_sentence
        filtered_sentence = []
     
    return corpus

