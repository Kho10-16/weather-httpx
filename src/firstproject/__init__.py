import httpx

def get_weather(latitude, longtitude)：
    url = 'https://api.open-meteo.com/v1/forecast?latitude=4.3993&longitude=113.9916&hourly=temperature_2m&timezone=Asia%2FSingapore'
    response = httpx.request(url)
    print(response.status_code)

def main():
    get_weather()

if __name__ == "__main__":
    main()