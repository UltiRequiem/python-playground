"""
https://stackoverflow.com/questions/70928442
"""

import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup

URL = "https://rosstat.gov.ru/folder/12781"

responce = requests.get(URL).text
soup = BeautifulSoup(responce, "lxml")
block = soup.find("div", class_="col-lg-8 order-1 order-lg-1")

list_info_block_row = block.find_all(
    "div", class_="document-list__item document-list__item--row"
)

for text_block_row in list_info_block_row:
    new_list = []
    title_element_row = text_block_row.find("div", class_="document-list__item-title")
    preprocessing_title = title_element_row.text.strip()
    link_element_row = text_block_row.find("a").get("href")
    new_list.append(preprocessing_title)

    if not link_element_row.startswith("http"):
        parsed_url = urlparse(URL)
        link_element_row = (
            parsed_url.scheme + "://" + parsed_url.netloc + link_element_row
        )

    new_list.append(link_element_row)

    print(new_list)
    print(title_element_row.text.strip())
    print(link_element_row)
    print("\n\n")
