# import time

# def sleep():
#     print(f'Time: {time.time() - start:.2f}')
#     time.sleep(1)

# def sum(name, numbers):
#     total = 0
#     for number in numbers:
#         print(f'Task {name}: Computing {total}+{number}')
#         sleep()
#         total += number
#     print(f'Task {name}: Sum = {total}\n')

# start = time.time()
# tasks = [
#     sum("A", [1, 2]),
#     sum("B", [1, 2, 3]),
# ]
# end = time.time()
# print(f'Time: {end-start:.2f} sec')


import asyncio


async def io_related(name):
    print(f'{name} started')
    await asyncio.sleep(1)
    print(f'{name} finished')


async def main():
    await asyncio.gather(
        io_related('first'),
        io_related('second'),
    )  # 1s + 1s = over 1s


if __name__ ==  '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
