import asyncio
import aiohttp

URL = "https://example.com"
TOTAL_REQUESTS = 10000
CONCURRENCY = 200

async def fetch(session, i):
    try:
        async with session.get(URL, timeout=10) as response:
            print(f"[{i}] PASSED - Status: {response.status}")
    except Exception as e:
        print(f"[{i}] FAILED - {type(e).__name__}")

async def run():
    connector = aiohttp.TCPConnector(limit=CONCURRENCY)
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = [fetch(session, i) for i in range(1, TOTAL_REQUESTS + 1)]
        await asyncio.gather(*tasks, return_exceptions=True)

asyncio.run(run())
