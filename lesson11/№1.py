import asyncio

async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({i})...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")

async def main():
    await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
# информация с сайта:
# Функция gather() модуля asyncio одновременно запускает объекты ожидания в последовательности *aws.
# =>одновременно начнутся все 3 задания и будут выполняться до их завершения, соответственно сначала завершится А потом В потом С.
# сначала будет написана f"Task {name}: Compute factorial({i})...", пока не посчитается, затем ответ по мере выполнения заданий