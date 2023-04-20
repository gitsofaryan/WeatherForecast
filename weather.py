import requests
import json
import sys


def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=(your api key)"
    response = requests.get(url)

    if response.status_code == 200:
        weather_data = json.loads(response.text)
        return weather_data
    else:
        print("Error fetching weather data.")
        sys.exit(1)


def print_weather(city):
    weather_data = get_weather(city)

    if weather_data:
        description = weather_data['weather'][0]['description'].capitalize()
        temp = round(weather_data['main']['temp'] - 273.15, 1)
        feels_like = round(weather_data['main']['feels_like'] - 273.15, 1)
        humidity = weather_data['main']['humidity']
        print(
            f"{city}: {description}, {temp}°C (feels like {feels_like}°C), Humidity: {humidity}%")
    else:
        print(f"Could not get weather data for {city}.")


def print_weather(city):
    weather_data = get_weather(city)

    if weather_data:
        description = weather_data['weather'][0]['description'].capitalize()
        temp = round(weather_data['main']['temp'] - 273.15, 1)
        feels_like = round(weather_data['main']['feels_like'] - 273.15, 1)
        humidity = weather_data['main']['humidity']
        print(
            f"{city}: {description}, {temp}°C (feels like {feels_like}°C), Humidity: {humidity}%")
    else:
        print(f"Could not get weather data for {city}.")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        city = sys.argv[1]
        print_weather(city)
    else:
        print("Usage: python weather.py <city>")
