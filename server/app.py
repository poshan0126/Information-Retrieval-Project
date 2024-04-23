from flask import Flask, request, render_template_string
import os
import itertools
import sys
sys.path.append('D:/Desktop/Spring2024/Information Retrieval/CNN_Crawler')

# Assume the crawler and indexer are imported correctly
# from your_crawler_module import your_crawler_function
from indexer.indexer import Indexer
from crawler.crawler import run_crawler

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        query = request.form['query']  # User's input for the query
        max_pages = int(request.form['max_pages'])
        depth = int(request.form['depth'])
        
        # Run the crawler to crawl pages and save URLs
        run_crawler(query, max_pages, depth)
        # Example usage
        current_file_path = os.path.abspath(__file__)

        # Move one folder up in the directory structure
        project_dir = os.path.dirname(os.path.dirname(current_file_path))
        output_dir = os.path.join(project_dir, 'crawled_pages')
        indexer = Indexer(output_dir)
        indexer.create_index()
        # Get URLs and scores for the query
        urls = indexer.get_urls()
        print("Here are urls ")
        print(urls)
        scores = indexer.get_scores_for_query(query)

        print("This is scores ")
        print(scores)
        data = list(zip(urls, scores))
        print(data)
        return render_template_string("""
    <h1>Search Results</h1>
    <form method="post">
        <input type="text" name="query" placeholder="Enter query" value="{{ query }}">
        <input type="number" name="max_pages" placeholder="Max pages" value="{{ max_pages }}">
        <input type="number" name="depth" placeholder="Depth" value="{{ depth }}">
        <button type="submit">Search</button>
    </form>
    <div style="width: 90%; margin: auto; overflow-x: hidden;">
        <table border="1" style="width: 100%; table-layout: fixed;">
            <tr>
                <th>URL</th>
                <th>Score</th>
            </tr>
            {% for url, score in data %}
            <tr>
                <td style="word-wrap: break-word;"><a href="{{ url }}" target="_blank">{{ url }}</a></td>
                <td>{{ score[0] }}</td>
            </tr>
            {% endfor %}
        </table>
    </div>
    """, query=query, max_pages=max_pages, depth=depth, data=data)

    else:
        return render_template_string("""
            <h1>Welcome to the Search Application</h1>
            <form method="post">
                <input type="text" name="query" placeholder="Enter query">
                <input type="number" name="max_pages" placeholder="Max pages">
                <input type="number" name="depth" placeholder="Depth">
                <button type="submit">Search</button>
            </form>
            """)


if __name__ == '__main__':
    app.run(debug=True)
