from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import pickle


def getInvertedIndex(corpus,mode,dataset):

    # Create a list of courses
    file = 'indexes/'+dataset+'_index.pickle'
    courses_title = list(corpus.values())
    courses_keys = list(corpus.keys())


    if(mode == 'offline'):
        
        # Create a TfidfVectorizer object
        vectorizer = TfidfVectorizer()

        # 'l2' for normalization
        transformer = TfidfTransformer(norm='l2')

        # Fit the vectorizer to the courses
        tfidf_matrix = vectorizer.fit_transform(courses_title)

        # Normalize the TF-IDF matrix
        normalized_matrix = transformer.fit_transform(tfidf_matrix)

        # write the result on file
        with open(file, 'wb') as handle:
            pickle.dump((normalized_matrix, courses_keys, courses_title, vectorizer), handle)
            
        return file
    
    else:
        # Create a TfidfVectorizer object
        with open(file, 'rb') as handle:
            normalized_matrix, courses_keys, courses_title, vectorizer = pickle.load(handle)

        #'l2' for normalization
        transformer = TfidfTransformer(norm='l2')
       
        # Fit the vectorizer to query
        tfidf_matrix = vectorizer.transform(list(corpus.values()))
        
        # Normalize the TF-IDF matrix
        normalized_matrix = transformer.fit_transform(tfidf_matrix)
       
        return normalized_matrix
