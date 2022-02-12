from bs4 import BeautifulSoup
from requests import get

BASE_URL = "https://reactjs.org"

response = get(f"{BASE_URL}/docs/getting-started.html")
soup = BeautifulSoup(response.text, "html.parser")

block = soup.find("div", class_="css-1sdm35g")

for category in block.find_all("button"):
    print(
        f"""\n <details>
  <summary>{category.text}</summary>
  """
    )
    for point in category.parent("a"):
        print(f"- [ ] [{point.text}]({BASE_URL}{point['href']})")

    print("</details>")
