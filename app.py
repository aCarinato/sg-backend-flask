from flask import Flask, request, jsonify
from flask_cors import CORS

# from markupsafe import escape
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)
CORS(app)


@app.route("/scrape", methods=["POST"])
def scrape():
    try:
        website_url = request.json["url"]
        response = requests.get(website_url)

        # Check the HTTP status code to see if the request was successful
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            relevant_tags = [
                "div",
                "h1",
                "h2",
                "h3",
                "h4",
                "h5",
                "h6",
                "p",
                "a",
                "span",
                "em",
                "strong",
                "b",
                "i",
                "u",
                "ol",
                "ul",
                "li",
                "img",
                "table",
                "thead",
                "tbody",
                "tfoot",
                "tr",
                "th",
                "td",
            ]

            text_on_page = ""
            for tag in soup.find_all(relevant_tags):
                if tag.string:
                    text_on_page += tag.string + " "

            return jsonify({"success": True, "content": text_on_page})

        else:
            return jsonify({"success": False, "error": "URL not found or inaccessible"})

    except Exception as e:
        return jsonify({"success": False, "error": str(e)})


# @app.route("/scrape", methods=["POST"])
# def scrape():
#         # get the URL from the request arguments
#         # url = request.args.get('url')

#         website_url = request.json["url"]

#         # print(website_url)

#         response = requests.get(website_url)
#         # yc_web_page = response.text

#         # make a request to the URL and get the content
#         # response = requests.get(url)
#         soup = BeautifulSoup(response.text, "html.parser")
#         print(soup)
#         # soup = BeautifulSoup(response.content, 'html.parser')

#         # define the relevant tags to scrape
#         relevant_tags = [
#             "div",
#             "h1",
#             "h2",
#             "h3",
#             "h4",
#             "h5",
#             "h6",
#             "p",
#             "a",
#             "span",
#             "em",
#             "strong",
#             "b",
#             "i",
#             "u",
#             "ol",
#             "ul",
#             "li",
#             "img",
#             "table",
#             "thead",
#             "tbody",
#             "tfoot",
#             "tr",
#             "th",
#             "td",
#         ]

#         text_on_page = ""
#         for tag in soup.find_all(relevant_tags):
#             if tag.string:
#                 text_on_page += tag.string + " "

#         print(text_on_page)
#         # print(text_on_page)
#         # # find all the relevant elements in the page and join them into a single string
#         # text_on_page = "\n".join([tag.get_text() for tag in soup.find_all(relevant_tags)])

#         # response = {
#         #     'success': True,
#         #     'content': text_on_page
#         # }

#         # create a response containing the scraped text
#         return text_on_page


if __name__ == "__main__":
    app.run(debug=True)
