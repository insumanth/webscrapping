import time
import requests
import csv
from lxml import etree
from gtts import gTTS

url_to_scrape = "https://www.theguardian.com/uk/culture"
response = requests.get(url=url_to_scrape)
print("  => Fetched Page")

if response.status_code == 200:
    html_dom = etree.HTML(response.text)
    print("  => Page Fetch Successful")
    print("  => Parsing HTML Data")
else:
    print(f"  => Failed to Fetch HTML File , Status Code {response.status_code}")
    exit()

headline_nodes = html_dom.xpath("//a[@data-link-name='article' and @aria-hidden='true']")
print("  => Extracting Nodes")

headlines = []
count = 0
for node in headline_nodes:
    headline = node.text
    link = node.attrib['href']
    count += 1
    line = {
        "No": count,
        "Headline": headline,
        "URL": link
    }
    headlines.append(line)

print("  => Extracting Text from Nodes")

print("  => Getting Current Time")
time_string = time.strftime("on_%Y_%m_%d_at_%H_%M")
file_name_tsv = f"Guardian_News_{time_string}.tsv"
file_name_mp3 = f"Guardian_News_{time_string}.mp3"

print("  => Saving into File")
csv_field_names = headlines[0].keys()
with open(file_name_tsv, 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, csv_field_names, delimiter="\t")
    csv_writer.writeheader()
    csv_writer.writerows(headlines)

headline_list = []
for line in headlines:
    headline_list.append(line['Headline'])

headline_text = " . ".join(headline_list)

print("  => Converting Text to Speech")
tts = gTTS(headline_text)
tts.save(file_name_mp3)
print("  => File saved")

