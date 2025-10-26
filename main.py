from datetime import date, timedelta
from random import choice, randint

from fastapi import FastAPI, HTTPException, Request


app = FastAPI(title="Weather API", version="1.0.0")


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


@app.get("/weatherforecast")
async def get_weatherforecast(request: Request) -> list[dict]:
    secret = request.headers.get("X-Ocop-Proxy-Secret")
    if secret != "2d76020d-797d-479b-b019-e11c10c33e6f":
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


