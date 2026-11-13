import asyncio


async def main():
    print("Начало операции")
    await asyncio.sleep(0.5)
    print("Конец строки")


asyncio.run(main())