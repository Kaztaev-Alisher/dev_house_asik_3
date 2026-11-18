import asyncio
import httpx

async def download_async(client , url) -> bool:
    try : 
        await client.get(url)
        return True
    except httpx.HTTPError:
        return False

async def main(urlss):
    async with httpx.AsyncClient() as client: 
        # task = asyncio.create_task([download_async(client , url) for url in urlss])
        return await asyncio.gather(*[download_async(client , url) for url in urlss])

def go_asyncio(a):
    return asyncio.run(main(a))
