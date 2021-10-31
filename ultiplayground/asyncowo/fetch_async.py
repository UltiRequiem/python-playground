import requests
import asyncio
from datetime import datetime

print(datetime.now())

async def fetch(url:str):
    requests.get(url)


async def main():
    for _ in range(10):
        await fetch('https://www.google.com')


asyncio.run(main())

print(datetime.now())
