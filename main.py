import asyncio


async def async_func():
    print("запуск...")
    await asyncio.sleep(3)
    print("...done")


async def main():
    print("step")
    await async_func()


asyncio.run(main())

