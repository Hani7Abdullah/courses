from services.first.Lemmatizer import lemmatizer
from services.first.RemoveStopWords import removeStopWords
from services.first.Stemmer import stemmer
from services.first.ToLowerCase import toLowerCase
from services.first.Tokenizer import tokenizer
from services.first.read_file import read_csv_file
from services.second.GetInvertedIndex import getInvertedIndex

def train(dataset):
    print('reading corpus...')
    corpus = read_csv_file('datasets/'+dataset+'.csv')
    

    print('corpus toLowerCase ...')
    corpus = toLowerCase(corpus)

    print('corpus tokenizer ...')
    corpus = tokenizer(corpus)


    print('corpus removeStopWords ...')
    corpus = removeStopWords(corpus)

    print('corpus stemmer ...')
    corpus = stemmer(corpus)

    print('corpus lemmatizer ...')
    corpus = lemmatizer(corpus)

    # join results 
    for course_id, clean_course_title in corpus.items():
        corpus[course_id] = " ".join(clean_course_title)
    print('finished text handling.')

    # inverted index (tfidf)
    getInvertedIndex(corpus,"offline",dataset)

    print("The model "+ dataset +" has been trained successfully")


# datasets : courses
print("This might take a few minutes ,Please wait ...") 
train('courses')