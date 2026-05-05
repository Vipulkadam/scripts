import pytest
import requests

BASE_URL = "https://yh-finance.p.rapidapi.com"
HEADERS = {
    "X-RapidAPI-Key": "YOUR_API_KEY",
    "X-RapidAPI-Host": "yh-finance.p.rapidapi.com"
}


# -------------------------
# Utility functions
# -------------------------
def get_request(endpoint, params=None, headers=None):
    response = requests.get(BASE_URL + endpoint, params=params, headers=headers or HEADERS)
    return response


def post_request(url, payload, headers=None):
    response = requests.post(url, json=payload, headers=headers)
    return response


def put_request(url, payload, headers=None):
    response = requests.put(url, json=payload, headers=headers)
    return response


def delete_request(url, headers=None):
    response = requests.delete(url, headers=headers)
    return response


# -------------------------
# Test Cases
# -------------------------

# @pytest.mark.api
def test_get_stock_summary():
    """Validate stock summary API response"""
    endpoint = "/stock/v2/get-summary"
    params = {"symbol": "AAPL", "region": "US"}

    response = get_request(endpoint, params=params)

    # Basic validation
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    data = response.json()
    assert "price" in data, "'price' key missing in response"
    assert "regularMarketPrice" in data["price"], "Market price data missing"

    # Additional validations
    market_price = data["price"].get("regularMarketPrice", {}).get("raw")
    assert isinstance(market_price, (int, float)), "Market price is not a number"


@pytest.mark.api
def test_post_create_resource():
    """Validate POST API creation"""
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {"title": "test automation", "body": "pytest api testing", "userId": 1}

    response = post_request(url, payload)

    assert response.status_code == 201, f"Expected 201, got {response.status_code}"
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]

@pytest.mark.api
def test_put_update_resource():
    """Validate PUT API update"""
    url = "https://jsonplaceholder.typicode.com/posts/1"
    payload = {"id": 1, "title": "updated title", "body": "updated body", "userId": 1}

    response = put_request(url, payload)

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]


@pytest.mark.api
def test_delete_resource():
    """Validate DELETE API"""
    url = "https://jsonplaceholder.typicode.com/posts/1"

    response = delete_request(url)

    assert response.status_code == 200 or response.status_code == 204, f"Expected 200/204, got {response.status_code}"

@pytest.mark.api
def test_stock_data_fields():
    """Extra validations for stock data"""
    endpoint = "/stock/v2/get-summary"
    params = {"symbol": "AAPL", "region": "US"}

    response = get_request(endpoint, params=params)
    data = response.json()

    # Validate important keys exist
    expected_keys = ["price", "summaryDetail", "financialData"]
    for key in expected_keys:
        assert key in data, f"{key} missing in response"

    # Validate numeric fields
    market_price = data.get("price", {}).get("regularMarketPrice", {}).get("raw")
    assert isinstance(market_price, (int, float)) and market_price > 0, "Invalid market price"

@pytest.mark.api
def test_invalid_symbol():
    """Test handling invalid stock symbol"""
    endpoint = "/stock/v2/get-summary"
    params = {"symbol": "INVALID123", "region": "US"}

    response = get_request(endpoint, params=params)

    # Validate error response
    assert response.status_code == 404 or response.status_code == 400