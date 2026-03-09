class WatchlistPage:
    def __init__(self, page):
        self.page = page
        #locators
        self.add_stock_input = "div#stockAddblock input[placeholder='Type to search...']"
        self.exchange_select = "div#stockAddblock select#Stock_Exchange_Type"
        self.add_button = "div#stockAddblock button.add_transaction"
        self.watchlist_rows = "table.watchlist_table tbody tr"  # update selector for watchlist table
        self.no_data_span = "td.ka-no-data-cell span"

    def count_stocks_in_watchlist(self) -> int:
        """Returns number of stocks currently in watchlist."""
        if self.page.is_visible(self.no_data_span):
            return 0
        return len(self.page.query_selector_all(self.watchlist_rows))

    def add_stock(self, stock_name: str, exchange: str = "N") -> None:
        """Add a stock to the watchlist."""
        self.page.fill(self.add_stock_input, stock_name)
        self.page.select_option(self.exchange_select, exchange)
        self.page.click(self.add_button)
        # wait for stock to appear in watchlist
        self.page.wait_for_timeout(1000)
