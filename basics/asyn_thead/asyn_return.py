import asyncio
import time


async def func1():
    print("我是func1")
    await asyncio.sleep(1)
    print("func1结束")
    return ("func1返回值")


async def func2():
    print("我是func2")
    await asyncio.sleep(2)
    print("func2结束")
    return ("func2返回值")


async def func3():
    print("我是func3")
    await asyncio.sleep(3)
    print("func3结束")
    return ("func3返回值")


async def main():
    f1 = func1()
    f2 = func2()
    f3 = func3()
    tasks = [
        asyncio.create_task(f2),
        asyncio.create_task(f1),
        asyncio.create_task(f3),
    ]
    # done, pending = await asyncio.wait(tasks)
    # for t in done:
    #     print(t.result())
    result = await asyncio.gather(*tasks, return_exceptions=True)
    # wait gather区别：wait没顺序，gather 按照传参顺序返回返回值
    print(result)


if __name__ == '__main__':
    asyncio.run(main())
