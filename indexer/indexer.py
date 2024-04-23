from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import os

class Indexer:
    def __init__(self, output_dir):
        # Initialize the TF-IDF Vectorizer
        self.vectorizer = TfidfVectorizer()
        self.output_dir = output_dir
        self.docs = self.load_documents()
        self.tfidf_matrix = None

    def load_documents(self):
        """Load HTML content from crawled pages."""
        docs = []
        for file_name in os.listdir(self.output_dir):
            file_path = os.path.join(self.output_dir, file_name)
            with open(file_path, 'r', encoding='utf-8') as file:
                docs.append(file.read())
        return docs

    def create_index(self):
        """ Create an index from the documents using TF-IDF. """
        # Transform documents into a TF-IDF matrix
        self.tfidf_matrix = self.vectorizer.fit_transform(self.docs)

    def save_index(self, path='index.pkl'):
        """ Save the vectorizer and TF-IDF matrix to a file. """
        # Use pickle to serialize the vectorizer and matrix
        with open(path, 'wb') as f:
            pickle.dump((self.vectorizer, self.tfidf_matrix), f)

    def load_index(self, path='index.pkl'):
        """ Load the vectorizer and TF-IDF matrix from a file. """
        # Check if the index file exists and load it
        if os.path.exists(path):
            with open(path, 'rb') as f:
                self.vectorizer, self.tfidf_matrix = pickle.load(f)
        else:
            raise FileNotFoundError("Index file not found.")

    def get_scores_for_query(self, query):
        """ Query the index with the specified text and return similarity scores. """
        # Transform the query to the same feature space as the documents
        query_vec = self.vectorizer.transform([query])
        # Compute cosine similarity between the query vector and all document vectors
        scores = cosine_similarity(query_vec, self.tfidf_matrix)
        
        url_scores = list(zip(scores[0]))
        return url_scores

    def get_urls(self):
        """Get URLs from the URLs file."""
        current_file_path = os.path.abspath(__file__)

        # Move one folder up in the directory structure
        project_dir = os.path.dirname(os.path.dirname(current_file_path))
        output_dir = os.path.join(project_dir, 'output')
        try:
            with open(os.path.join(output_dir, 'urls.txt'), 'r', encoding='utf-8') as file:
                urls = [line.strip() for line in file if line.strip()]
            return urls
        except FileNotFoundError:
            return []
if __name__ == '__main__':
    # Example usage
    current_file_path = os.path.abspath(__file__)

    # Move one folder up in the directory structure
    project_dir = os.path.dirname(os.path.dirname(current_file_path))
    output_dir = os.path.join(project_dir, 'crawled_pages')
    indexer = Indexer(output_dir)
    indexer.create_index()
    indexer.save_index()
    query = "example query"
    scores = indexer.get_scores_for_query(query)
    urls = indexer.get_urls()
