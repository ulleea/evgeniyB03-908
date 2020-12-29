from collections import namedtuple
import time
import asyncio
from concurrent.futures import FIRST_COMPLETED
import aiohttp

Service = namedtuple('Service', ('name', 'url', 'ip_attr'))

SERVICES = (
    Service('ipify', 'https://api.ipify.org?format=json', 'ip'),
    Service('ip-api', 'http://ip-api.com/json', 'query')
)
async def fetch_ip(service):
    print(service.ip_attr)
    async with aiohttp.ClientSession() as session:
        async with session.get(service.url) as resp:
            a=await resp.json()
            print(a[service.ip_attr],service.ip_attr)
            return a


async def asynchronous():
    futures = [fetch_ip(service) for service in SERVICES]
    done,_ = await asyncio.wait(futures, return_when=asyncio.FIRST_COMPLETED)
ioloop = asyncio.get_event_loop()
ioloop.run_until_complete(asynchronous())