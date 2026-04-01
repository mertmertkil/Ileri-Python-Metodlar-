import asyncio


async def main(msg):
    print(f"Start: {msg}")
    await asyncio.sleep(1)
    print(f"End: {msg}")


asyncio.run(main("Hello, Async!"))
