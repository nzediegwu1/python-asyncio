import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    return what


async def main():
    print(f"started at {time.strftime('%X')}")

    # Wait until the three tasks are completed
    # Should take around 2 seconds instead of 6 seconds for the three tasks
    [task1, task2, task3] = await asyncio.gather(
        say_after(2, 'hello'), say_after(2, 'world'), say_after(2, 'anaeze'))

    print(task1, task2, task3)

    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())
