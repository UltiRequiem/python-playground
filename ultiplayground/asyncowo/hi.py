import asyncio


async def sai_hy(name: str):
    return f"Hi {name}!"


async def main():
    print(await sai_hy("Zero"))


asyncio.run(main())
