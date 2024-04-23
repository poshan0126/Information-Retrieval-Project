import os
import urllib.parse
from scrapy.crawler import CrawlerProcess
from scrapy.spiders import CrawlSpider
from scrapy.http import Request

class WebCrawler(CrawlSpider):
    name = "webcrawler"
    
    def __init__(self, query, max_pages=100, depth=3, output_dir='crawled_pages', urls_file_path='urls.txt', *args, **kwargs):
        super(WebCrawler, self).__init__(*args, **kwargs)
        self.google_search_url = f"https://www.google.com/search?q={query}"
        self.max_pages = max_pages
        self.depth = depth
        self.count = 0
        self.output_dir = output_dir
        self.urls_file_path = urls_file_path

        # Clear the URL file before starting a new crawl
        self.clear_url_history()

        # Setting up the initial settings
        self.custom_settings = {
            'DEPTH_LIMIT': self.depth,
            'CONCURRENT_REQUESTS': 16,
            'AUTOTHROTTLE_ENABLED': True,
            'DOWNLOAD_DELAY': 1,
            'USER_AGENT': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
        }

    def start_requests(self):
        yield Request(self.google_search_url, self.parse_google_search)

    def parse_google_search(self, response):
        links = response.css('a[href]:not([href*="aclk"])').xpath('@href').extract()
        valid_links = [link for link in links if 'url?q=' in link and not 'webcache' in link and not 'google.com' in link]
        
        for link in valid_links[:self.max_pages]:
            actual_url = link.split('&')[0].replace('/url?q=', '')
            actual_url = urllib.parse.unquote(actual_url)
            yield response.follow(actual_url, self.parse_item)

    def parse_item(self, response):
        self.count += 1
        if self.count <= self.max_pages:
            with open(self.urls_file_path, 'a', encoding='utf-8') as url_file:
                url = response.url
                url_file.write(url + '\n')
            yield {
                'url': response.url
            }
    def clear_url_history(self):
        """Clear the history in the URL file by truncating it."""
        if self.urls_file_path:
            # Adjust the file path to be relative to the project directory
            full_path = os.path.join(self.output_dir, self.urls_file_path)
            # Ensure the directory exists
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            # Create the file if it doesn't exist
            open(full_path, 'a').close()
            # Truncate the file
            with open(full_path, 'w') as file:
                file.truncate(0)

def run_crawler(query, max_pages, depth):
    # Get the absolute path of the current file
    current_file_path = os.path.abspath(__file__)

    # Move one folder up in the directory structure
    project_dir = os.path.dirname(os.path.dirname(current_file_path))
    output_dir = os.path.join(project_dir, 'crawled_pages')
    urls_file_path = os.path.join(project_dir, 'output', 'urls.txt')

    process = CrawlerProcess(settings={
        'USER_AGENT': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
        'FEEDS': {},
    })
    process.crawl(WebCrawler, query=query, max_pages=max_pages, depth=depth, output_dir=output_dir, urls_file_path=urls_file_path)
    process.start()

if __name__ == '__main__':
    query = "Naive Bayes Quantifier"
    max_pages = 10
    depth = 3

    # Run the crawler
    run_crawler(query, max_pages, depth)
