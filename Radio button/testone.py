import pytest
import requests

def test_api():
    url = "https://api.openweathermap.org/data/2.5/find?q=pune&appid=5796abbde9106b7da4febfae8c44c232&units=metric"

    response = requests.get(url)

    assert response.status_code == 200

    data = response.json()

    print(data)

    temp = data["list"][0]["main"]["temp"]  # Correct key access

    print(f"Current temperature in Pune: {temp}°C")

    assert 0 <= temp <= 50  # Safer range check instead of exact value













