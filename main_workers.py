import httpx
from concurrent.futures import ThreadPoolExecutor

def download_potok(url) -> bool:
    try : 
        httpx.get(url)
    except httpx.HTTPError:
        return False
    return True

def go_workers(a):
    res : list = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = executor.map(download_potok , a)
        for x in results:
            res.append(x)

    return res