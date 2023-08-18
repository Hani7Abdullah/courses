import pickle
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from services.first.read_file import read_csv_file
import csv

def getSimilarity(query_index ,dataset):
    # get courses index
    file = 'indexes/'+dataset+'_index.pickle'
    with open(file, 'rb') as handle:
        normalized_matrix, courses_keys, courses_title, vectorizer = pickle.load(handle)

    # calculate similarity
    query_vector = query_index.reshape(1,-1)

    # Calculate cosine similarity between the query vector and course vectors
    cosine_similarities = cosine_similarity(query_vector, normalized_matrix)

    # Flatten the cosine similarities array
    cosine_similarities = np.ravel(cosine_similarities)

    # Get the indices that would sort the cosine similarities array in descending order
    indices = np.argsort(cosine_similarities)[::-1]

    # Rank the courses keys based on cosine similarity
    ranked_courses_keys = [courses_keys[i] for i in indices]

    # Rank the courses values based on cosine similarity
    ranked_courses_values = [courses_title[i] for i in indices]

    # formate result

    results = []
    for i, course_ID in enumerate(ranked_courses_keys):
        similarity = cosine_similarities[indices[i]]
        print (similarity)
        if similarity > 0.4:
            
            rank = i+1
    
            with open('datasets/'+dataset+'.csv', 'r') as f:
                reader = csv.DictReader(f)
                course_id, *_ = reader.fieldnames

                for row in reader:
                    if row[course_id] == course_ID:
                        course = row
                        results.append({ 
                            'id': rank, 
                            'similarity': similarity,
                            'course_id': course_ID,
                            'course_title': course['course_title'],
                            'url': course['url'],
                            'is_paid': course['is_paid'],
                            'price': course['price'],
                            'num_subscribers': course['num_subscribers'],
                            'num_reviews': course['num_reviews'],
                            'num_lectures': course['num_lectures'],
                            'level': course['level'],
                            'content_duration': course['content_duration'],
                            'published_timestamp': course['published_timestamp'],
                            'subject': course['subject'],
                            'clean_course_title':course['clean_course_title'],
                        })

    return results