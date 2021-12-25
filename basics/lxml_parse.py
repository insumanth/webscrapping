# Import required library
# lxml is a XML and HTML Parser
from lxml import etree 
# Requests is used to send request and receive response
import requests

url_to_scrap = "https://quotes.toscrape.com/"

# Sending request
response = requests.get(url_to_scrap)

# Checking if the request was successful
if response.status_code == 200:
    # Extract data
    html_data = response.text
    # Parse HTML
    dom = etree.HTML(html_data)
    # HTML Selector
    quotes = dom.xpath("//span[@class='text']")
    # Iterate and print result
    for i in quotes:
        print(i.text)
