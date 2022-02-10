from bs4 import BeautifulSoup
from requests import get

response = get("https://reactjs.org/docs/getting-started.html")
soup = BeautifulSoup(response.text, "html.parser")

block = soup.find("div", class_="css-1sdm35g")

for point in block.find_all("a"):
    print(f"- [ ] {point.text}")
