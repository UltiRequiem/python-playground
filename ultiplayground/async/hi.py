import asyncio


async def sai_hy(name: str):
    return f"Hi {name}!"


async def main():
    hey = await sai_hy("Zero")
    print(hey)


asyncio.run(main())
