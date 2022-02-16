import cfscrape

scraper = cfscrape.create_scraper()

response = scraper.get("https://developers.cloudflare.com/workers")

print(response.text)
