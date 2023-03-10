news_sites = {
    "origo": "https://www.origo.hu",
    "index": "https://index.hu",
    "hvg": "https://hvg.hu"
}
api_key = "YOUR_WAYBACK_MACHINE_API_KEY"

import requests
import json
from datetime import datetime
from datetime import timedelta


def get_url_from_wayback_machine(site_name, date):
    url = f"https://archive.org/wayback/available?url={news_sites[site_name]}&timestamp={date}"
    response = requests.get(url)
    json_data = json.loads(response.content)
    return json_data['archived_snapshots']['closest']['url']
    
start_date = datetime(2010, 1, 1)
end_date = datetime(2020, 12, 31)

for site_name, site_url in news_sites.items():
    for date in (start_date + timedelta(n) for n in range((end_date - start_date).days)):
        formatted_date = date.strftime("%Y%m%d")
        url = get_url_from_wayback_machine(site_name, formatted_date)
        # TODO: Do something with the URL


import requests
from bs4 import BeautifulSoup
import huspacy

def process_text(text):
    nlp = huspacy.load("hu_core_ud_lg")
    doc = nlp(text)
    for token in doc:
        # Do something with the token, e.g. store it in a list or database
        pass

def get_text_from_url(url):
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text()
    process_text(text)

# Iterate over URLs and process their text
import waybackpy
# Python package that interfaces with the Internet Archive's Wayback Machine APIs.

def get_urls_from_waybackmachine(url):
    snapshots = []
    client = waybackpy.WaybackMachineClient()
    dates = client.get_available_dates(url)
    for date in dates:
        snapshots.extend(client.get_snapshots(url, date))
    urls = [snapshot.raw_url for snapshot in snapshots]
    return urls


# urls = [
#     "https://web.archive.org/web/20100101000000*/https://www.example.com/category/politics",
#     "https://web.archive.org/web/20110101000000*/https://www.example.com/category/politics",
#     "https://web.archive.org/web/20120101000000*/https://www.example.com/category/politics",
#     # add more URLs for other years as needed
# ]


for url in urls:
    get_text_from_url(url)
