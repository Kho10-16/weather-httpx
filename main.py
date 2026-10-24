import httpx
from dataclasses import dataclass
import time
import asyncio
# latitude=4.3993&longitude=113.9916&current=temperature_2m&timezone=Asia%2FSingapore

@dataclass
class Weather:
    city:str
    temperature: float
    time: str

async def get_weather(latitude: float, longitude: float, city:str) -> Weather:
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m",
        "timezone": "Asia/Singapore",
    }
    url = "https://api.open-meteo.com/v1/forecast"
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
    data = response.json()
    return Weather(
        city=city,
        temperature=data['current']['temperature_2m'],
        time=data['current']['time']
    )


async def main() -> None:
    current_time = time.perf_counter()
    miri, kuching = await asyncio.gather(
        get_weather(4.3993, 113.9916, "Miri"),
        get_weather(1.5535, 110.3593, "Kuching"),
    )
    
    new_time = time.perf_counter()
    difference_time = new_time - current_time
    print(f'{difference_time:.2f}')

    print(f"美里现在的温度{miri.time}: {miri.temperature}")
    print(f"古晋现在的温度{kuching.time}: {kuching.temperature}")
    if miri.temperature > kuching.temperature:
        print("美里比古晋热")
    elif kuching.temperature > miri.temperature:
        print("古晋比美里热")
    else:
        print("一样热！")

    

if __name__ == "__main__":
    asyncio.run(main())
