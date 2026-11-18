import httpx

def download(url : str) -> bool:
    try : 
        httpx.get(url)
    except httpx.HTTPError:
        return False
    return True

def go_one_by_one(a):
    res : list = []
    for url in a:
        res.append(download(url))

    return res
