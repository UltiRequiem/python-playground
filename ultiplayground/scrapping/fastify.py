from bs4 import BeautifulSoup
from requests import get

response = get("https://fastify.io/docs/latest")
soup = BeautifulSoup(response.text, "html.parser")

block = soup.find("div", class_="column is-3 is-hidden-mobile")

for point in block.find_all("a"):
    print(f"- [ ] {point.text}")
