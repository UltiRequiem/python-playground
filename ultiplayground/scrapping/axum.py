from bs4 import BeautifulSoup
from requests import get

BASE_URL = "https://docs.rs/axum/latest/axum"

response = get(BASE_URL)
soup = BeautifulSoup(response.text, "html.parser")

block = soup.find_all("h2")

for link in [url.find("a") for url in block[3:-4]]:
    print(f"- [ ] [{link.text}]({BASE_URL+'/'+link.get('href')})")
