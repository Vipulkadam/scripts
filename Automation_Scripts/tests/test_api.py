import pytest
import requests

BASE_URL = "https://yh-finance.p.rapidapi.com"

headers = {
    "X-RapidAPI-Key": "YOUR_API_KEY",
    "X-RapidAPI-Host": "yh-finance.p.rapidapi.com"
}


@pytest.mark.api
def test_get_stock_data():

    url = BASE_URL + "/stock/v2/get-summary"

    query = {
        "symbol": "AAPL",
        "region": "US"
    }

    response = requests.get(url, headers=headers, params=query)

    assert response.status_code == 200

    data = response.json()

    assert "price" in data

@pytest.mark.api
def test_post_example():

    url = "https://jsonplaceholder.typicode.com/posts"

    payload = {
        "title": "test automation",
        "body": "pytest api testing",
        "userId": 1
    }

    response = requests.post(url, json=payload)

    assert response.status_code == 201