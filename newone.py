from main_async import go_asyncio
from main_workers import go_workers
from main_one_by_one import go_one_by_one

import time

a : list[str] = []

with open("urls.txt") as f:
    for x in f:
        a.append(x.strip())


start = time.perf_counter()
res = go_asyncio(a)
print("asyncio - " , time.perf_counter() - start , sum(res) , len(res) - sum(res))

start = time.perf_counter()
res = go_workers(a)
print("potok - " , time.perf_counter() - start , sum(res) , len(res) - sum(res))

start = time.perf_counter()
res = go_one_by_one(a)
print("one by one - " , time.perf_counter() - start , sum(res) , len(res) - sum(res))