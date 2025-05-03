from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def check_plagiarism(text1, text2):
    documents = [text1, text2]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    return similarity * 100
text1 = "Artificial intelligence is the future of technology."
text2 = "Technology is moving towards artificial intelligence and automation."

similarity_percentage = check_plagiarism(text1, text2)
print(f"Plagiarism Similarity: {similarity_percentage:.2f}%")
