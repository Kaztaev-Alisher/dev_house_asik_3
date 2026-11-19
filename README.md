# URL Download Benchmark

Сравнивает скорость загрузки списка URL тремя способами:

- `asyncio` — `httpx.AsyncClient` + `asyncio.gather`
- потоки — `ThreadPoolExecutor` (10 воркеров)
- последовательно — по одному запросу

## Запуск

```bash
pip install httpx
python main.py
```

URL берутся из `urls.txt` (по одному на строку). Для каждого способа выводится время, число успешных и неудачных запросов.
