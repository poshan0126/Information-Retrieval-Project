# Search Application README

## Abstract
In this project, we developed a search application that indexes and retrieves documents using TF-IDF (Term Frequency-Inverse Document Frequency) and cosine similarity. The objective was to create a system capable of efficiently indexing and querying a collection of documents, providing users with relevant search results. The next steps involve potential enhancements such as improving indexing efficiency, incorporating more advanced ranking algorithms, and optimizing user interface elements for better user experience.

## Overview
This project, developed for the CS 429 Information Retrieval course, encompasses a web search application built using Python, integrating web crawling, indexing, and retrieval functionalities. Leveraging Flask as the web framework, the application employs Scikit-learn for text processing and cosine similarity computation, Scrapy for web crawling, and NLTK for natural language processing tasks. The core functionality revolves around indexing crawled web pages using TF-IDF vectors and retrieving relevant results based on user queries. By combining these components, the application provides users with a seamless interface to search for information across a collection of web pages, offering a comprehensive solution for web search and retrieval needs.
## Architecture and Design 
The architecture of this project is structured around a distributed system comprising several interconnected modules, each responsible for specific tasks within the web search application. At the core of the architecture is the Flask web framework, which serves as the interface for user interaction and query processing. The system employs Scrapy for web crawling, allowing for efficient and scalable extraction of data from diverse sources across the web. Extracted content is then processed using Scikit-learn's TF-IDF vectorizer to generate an index of documents, facilitating fast and accurate retrieval of relevant information. Additionally, NLTK is integrated into the system for natural language processing tasks such as tokenization and stemming, enhancing the quality of search results. The modular design enables seamless integration of new components and extensions, ensuring adaptability to evolving requirements and scalability to handle large-scale web crawling and indexing operations effectively. Overall, the architecture emphasizes flexibility, scalability, and performance to deliver a robust and efficient web search solution for users.
The design of this project revolves around a modular and scalable architecture aimed at efficiently handling web crawling, indexing, and retrieval tasks within a web search application. At the core of the design lies the integration of Flask, which serves as the web framework for handling user interactions and rendering search results. For web crawling, the project utilizes Scrapy, a powerful and extensible web crawling framework, to fetch and extract content from web pages. The extracted content is then processed using Scikit-learn's TF-IDF vectorizer to create an index of the crawled documents. This index, stored using Pickle serialization, enables efficient retrieval of relevant documents based on user queries. Additionally, NLTK is employed for preprocessing tasks such as tokenization and stemming to enhance the quality of search results. The design emphasizes modularity and flexibility, allowing for easy extension and customization of individual components to adapt to evolving requirements and accommodate future enhancements.

## Operations
Software commands include running the indexer to create the document index, querying the index with a search query, and presenting the results to the user. Installation instructions involve setting up Python dependencies and running the Flask application.
### Crawler
The Web Crawler is a Python script designed to extract web page URLs based on a specified query using the Scrapy framework. It initiates a Google search with the given query, retrieves relevant links from the search results, and follows them to crawl the corresponding web pages. The crawler operates within a defined maximum page limit and depth level to ensure efficient and focused crawling. The output, consisting of the crawled URLs, is saved to a designated file for further analysis or processing. Users can easily customize the query, maximum pages to crawl, and depth of the crawl by modifying the parameters in the script. Additionally, the script is well-documented and includes instructions for installation, usage, and contribution, making it accessible and adaptable for various crawling tasks.

### Indexer
This Python script implements an Indexer class designed for processing HTML content extracted from crawled web pages, building an index using the Term Frequency-Inverse Document Frequency (TF-IDF) technique, and facilitating query operations for similarity search. Leveraging libraries such as scikit-learn for TF-IDF feature extraction and cosine similarity computation, the Indexer class encapsulates methods for loading documents, creating and persisting the index, and querying the index with user-defined text queries. The main block demonstrates example usage by initializing the Indexer object with an output directory path, generating the index from crawled pages, saving it to disk, querying with a sample query, and retrieving URLs associated with the indexed documents. This script serves as a versatile tool for efficient information retrieval and text search tasks, offering flexibility and scalability for various applications requiring document indexing and similarity-based querying.

### APP
This Python script initializes a Flask web application for a search engine. It provides a simple HTML form where users can input a query, specify the maximum number of pages to crawl, and set the depth of the crawling process. Upon form submission, the script triggers a web crawler to fetch pages related to the user's query, saves the URLs of the crawled pages, and creates an index using the Indexer class. The script then retrieves URLs and similarity scores for the query from the index, combines them into a list of tuples, and renders them in an HTML table format for display on the web interface. The application dynamically updates the search results based on user input and allows for seamless interaction with the search functionality.

### Requirement
Flask
Scikit.learn
Scrapy
NLTK
Pickle
OS

### Installation

To install and run the web search application, follow these steps:

1. Clone this repository to your local machine:

    ```bash
    git clone <repository_url>
    ```

2. Navigate to the project directory:

    ```bash
    cd <project_directory>
    ```

3. Install the required dependencies using `pip`:

    ```bash
    pip install -r requirements.txt
    ```

4. Once the dependencies are installed, you can start the Flask server by running following inside server folder:

    ```bash
    python app.py
    ```

5. Open a web browser and go to `http://localhost:5000` to access the search application.

## Acknowledgement
I would like to express our gratitude to Professor for his guidance and support throughout this project. I am also thankful to the teaching assistants for their assistance and valuable feedback. Additionally, I appreciate the contributions of the learning management system and the helpful interactions with AI tools like ChatGPT, Claude, and Co-Pilot, which enhanced my learning experience.

## Conclusion
The project achieved success in implementing a basic search application capable of indexing and retrieving documents. However, there are areas for improvement such as indexing efficiency and user interface design. It's important to consider potential caveats such as scalability limitations and the need for further optimization.


## Source Code
Source code listings are available in the repository(https://github.com/poshan0126/Information-Retrieval-Project), along with documentation describing the project structure, dependencies, and usage instructions.

## Bibliography
1. Manning, C.D., Raghavan, P., and Schütze, H. Introduction to Information Retrieval. Cambridge University Press, 2008.
2. Croft, Bruce, Donald Metzler, and Trevor Strohman. Search Engines: Information Retrieval in Practice. Pearson Education, 2016.
3. GeeksforGeeks. "Python Program to Crawl a Web Page and Get Most Frequent Words." GeeksforGeeks, https://www.geeksforgeeks.org/python-program-crawl-web-page-get-frequent-words/. Accessed April 12, 2024.
4. GeeksforGeeks. "Python Program to Crawl a Web Page and Get Most Frequent Words." GeeksforGeeks. [Online]. Available: https://www.geeksforgeeks.org/python-program-crawl-web-page-get-frequent-words/. [Accessed: April 22, 2024].
5. Flask. "Flask Documentation." Flask. [Online]. Available: https://flask.palletsprojects.com/en/3.0.x/. [Accessed: April 15, 2024].

