class WatchlistPage:
    def __init__(self, page):
        self.page = page
        #locators
        self.login_on_hover = "a.userlink"
        self.add_stock_input = "div#stockAddblock input[placeholder='Type to search...']"
        self.exchange_select = "div#stockAddblock select#Stock_Exchange_Type"
        # self.add_button = "div#stockAddblock button.add_transaction"
        self.add_button = "//div[@class='fade tab-pane active show']//button[@class='add_transaction'][normalize-space()='+Add']"
        self.watchlist_rows = "table.ka-table tbody.ka-tbody tr.ka-tr.ka-row"
        self.no_data_span = "td.ka-no-data-cell span"
        self.my_watchlist = "a[title = 'My Watchlist']"

    def handeling_pop_up_and_redirection_to_watchlist(self):
        login_menu = self.page.locator(self.login_on_hover)
        # wait until visible
        login_menu.wait_for(state="visible", timeout=5000)
        # hover first (important for dropdown)
        login_menu.hover()
        # then click
        login_menu.click()
        self.page.wait_for_timeout(1000)
        self.page.locator(self.my_watchlist).click()
        self.page.wait_for_timeout(1000)

    def count_stocks_in_watchlist(self) -> int:
        """Returns the number of stocks currently in the watchlist."""

        self.handeling_pop_up_and_redirection_to_watchlist()

        # Wait a little for DOM to settle
        self.page.wait_for_timeout(1000)

        # Check if "No data" element is visible
        if self.page.is_visible(self.no_data_span):
            return 0

        # Locate all table rows inside the watchlist
        rows = self.page.locator(self.watchlist_rows)

        # Wait for at least 1 row (if expected)
        rows.first.wait_for(state="visible", timeout=6000)

        # Return the count of rows
        return rows.count()

    def add_stock(self, stock_name: str) -> None:
        """Add a stock to the watchlist with exact match."""
        # Wait for input and type the stock name
        self.page.locator(self.add_stock_input).wait_for(state="visible", timeout=5000)
        self.page.fill(self.add_stock_input, stock_name)
        # Use get_by_role for exact match on heading
        stock_item = self.page.get_by_role("heading", name=stock_name, exact=True)
        stock_item.wait_for(state="visible", timeout=5000)
        # Click the exact match
        stock_item.click()
        # Optional: wait for UI update
        self.page.wait_for_timeout(2000)
        self.page.locator(self.add_button).wait_for(state="visible", timeout=5000)
        self.page.locator(self.add_button).click()
        self.page.wait_for_timeout(1000)