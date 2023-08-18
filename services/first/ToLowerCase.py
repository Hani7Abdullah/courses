
def toLowerCase(corpus):
    for course_id, clean_course_title in corpus.items():
        corpus[course_id] = clean_course_title.lower().strip()
        
    return corpus

