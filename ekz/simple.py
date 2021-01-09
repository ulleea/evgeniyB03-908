async def simple(a=True):
    import time
    n=1
    while a:
        m = False
        k = 0
        for j in range(1, n + 1):
            if n % j == 0:
                if n == j or j == 1:
                        m = n
                else:
                    k = 1
        if k == 0:
            if m:
                print(m)
                b=time.time()
                try:
                    a=await asyncio.wait_for(stopper(),timeout=1.0)
                except asyncio.TimeoutError:
                    a=True
        n+=1

async def stopper():
    s=input()
    if s=='stop':
        return False
    else:
        return True

async def main():
    await simple()

import asyncio
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
