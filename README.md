# Weather API (FastAPI)

Minimal single-file FastAPI.

## Endpoint

- `GET /weatherforecast` – returns 5 random forecast entries.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Open: http://localhost:8000/docs

## Docker

```bash
docker build -t weather-api .
docker run --rm -p 8000:8000 weather-api
```

Open: http://localhost:8000/docs
