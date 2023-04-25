from flask import Flask, request
from flask_cors import CORS
# from markupsafe import escape
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)
CORS(app)

@app.route('/scrape', methods=['POST'])
def scrape():
    # get the URL from the request arguments
    # url = request.args.get('url')

    website_url = request.json['url']

    # print(website_url)

    response = requests.get(website_url)
    # make a request to the URL and get the content
    # response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # soup = BeautifulSoup(response.content, 'html.parser')

    # define the relevant tags to scrape
    relevant_tags = ['div', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'a', 'span', 'em', 'strong', 'b', 'i', 'u', 'ol', 'ul', 'li', 'img', 'table', 'thead', 'tbody', 'tfoot', 'tr', 'th', 'td']

    text_on_page = ''
    for tag in soup.find_all(relevant_tags):
        if tag.string:
            text_on_page += tag.string + ' '

    # print(text_on_page)
    # # find all the relevant elements in the page and join them into a single string
    # text_on_page = "\n".join([tag.get_text() for tag in soup.find_all(relevant_tags)])

    # create a response containing the scraped text
    return text_on_page

if __name__ == '__main__':
    app.run(debug=True)