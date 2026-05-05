import pytest
from Automation_Scripts.pages.login_page import LoginPage
from Automation_Scripts.pages.watchlist_page import WatchlistPage
from Automation_Scripts.utils.csv_reader import read_stocks_from_csv
from Automation_Scripts.utils.config_reader import read_config

@pytest.mark.ui
def test_add_stocks(browser_page):
    page = browser_page
    # Read config for credentials
    config = read_config()
    email = config["credentials"]["email"]
    password = config["credentials"]["password"]
    #  Login
    login = LoginPage(page)
    login.navigate()
    login.login_flow(email, password)
    #  Go to watchlist
    watchlist = WatchlistPage(page)
    #  Count initial stocks
    initial_count = watchlist.count_stocks_in_watchlist()
    print("Initial Stocks in watchlist:", initial_count)

    # ⃣ Read stock symbols from CSV
    symbols = read_stocks_from_csv("Automation_Scripts/data/stocks.csv")  # e.g., ITC, ONGC, BHEL

    # Add stocks one by one
    for stock in symbols:
        watchlist.add_stock(stock)

    # Count final stocks
    final_count = watchlist.count_stocks_in_watchlist()
    print("Final Stocks in watchlist:", final_count)

    #  Assertion
    assert final_count >= initial_count, "Final stock count should be greater or equal to initial count"

