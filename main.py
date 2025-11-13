import os
from datetime import date, timedelta
from random import choice, randint
from fastapi import FastAPI, HTTPException, Request

app = FastAPI(title="Weather API", version="1.0.0")
proxy_secret = os.getenv("proxy_secret")

SUMMARIES = [
    "Freezing",
    "Bracing",
    "Chilly",
    "Cool",
    "Mild",
    "Warm",
    "Balmy",
    "Hot",
    "Sweltering",
    "Scorching",
]


@app.get("/weatherforecast", status_code=200)
async def get_weatherforecast(request: Request) -> list[dict]:
    secret = request.headers.get("X-Ocop-Proxy-Secret")
    print("request secret header: >>{0}<<".format(proxy_secret))

    if secret != proxy_secret or secret is None:
        raise HTTPException(status_code=401, detail="Unauthorized")

    forecasts: list[dict] = []
    for i in range(1, 6):
        temp_c = randint(-20, 55)
        forecasts.append(
            {
                "date": (date.today() + timedelta(days=i)).isoformat(),
                "temperatureC": temp_c,
                "temperatureF": 32 + int(temp_c / 0.5556),
                "summary": choice(SUMMARIES),
            }
        )
    return forecasts
