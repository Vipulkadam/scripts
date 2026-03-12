
import time
from Automation_Scripts.utils.config_reader import read_config
import logging

logger = logging.getLogger(__name__)
class LoginPage:

    def __init__(self, page):

        self.page = page
        self.config = read_config()
        # Locators
        self.no_thanks = "//button[@id='wzrk-cancel' and text()='No thanks']"
        self.login_on_hover = "a.userlink"
        self.login_button = "//a[@title='Log In' and text()='Log-in']"
        self.by_password = "//li[@class='tbItm signup_ctc']"
        self.email = "//input[@id='useremailel']"
        self.password = "//input[@id='userpassword']"
        self.login_button_submit = "//button[normalize-space()='Login']"
        self.cross_on_pop_up = "//a[contains(@class,'skip_btn') and @href='javascript:;']"
    def navigate(self):

        self.page.goto(self.config["base_url"], timeout=1500000)
        self.page.wait_for_load_state("domcontentloaded")

    def login_flow(self, email, password):

        # Click the "No Thanks" button if it appears
        try:
            self.page.locator(self.no_thanks).click()
        except Exception as e:
            print(f"No 'No Thanks' button appeared: {e}")

        start = time.time()
        timeout = 120

        while True:
            try:
                login_menu = self.page.locator(self.login_on_hover)

                # wait until visible
                login_menu.wait_for(state="visible", timeout=5000)

                # hover first (important for dropdown)
                login_menu.hover()

                # then click
                login_menu.click()
                break

            except Exception as e:
                if time.time() - start > timeout:
                    raise Exception("Unable to click Hello Login after 2 minutes")

                print("Retrying Hello Login click...")
                self.page.wait_for_timeout(3000)

        logger.info("Waiting for login button to appear")
        self.page.wait_for_timeout(9000)

        logger.info("Clicking Login button on homepage")
        self.page.locator(self.login_button).click()

        logger.info("Waiting for login iframe to load")
        self.page.wait_for_timeout(3000)

        logger.info("Locating login iframe")
        frame_element = self.page.query_selector("iframe#myframe")
        frame = frame_element.content_frame()

        logger.info("Switching to 'Login with Password' option")
        frame.click(self.by_password)

        logger.info("Entering Email ID")
        frame.locator(self.email).click()
        frame.locator(self.email).type(email, delay=100)

        logger.info("Entering Password")
        frame.locator(self.password).click()
        frame.locator(self.password).type(password, delay=100)

        logger.info("Clicking Login Submit button")
        frame.locator(self.login_button_submit).click()

        logger.info("Waiting for page to load after login")
        self.page.wait_for_timeout(5000)
        # ------------------------
        # ASSERTION: Login success
        # ------------------------
        assert self.page.locator("iframe#mVerifyIframe").is_visible(), "Login not successful or dashboard not loaded"
        logger.info("Login successful and dashboard loaded.")
        self.page.wait_for_timeout(5000)

        # step: appering pop up handling
        try:
            frame_newelement = self.page.query_selector("iframe#mVerifyIframe")
            frame_one = frame_newelement.content_frame()
            self.page.wait_for_timeout(1000)
            logger.info("Switching to Mobile Verification frame and clicking Skip")

            frame_one.locator(self.cross_on_pop_up).click()
            self.page.wait_for_timeout(9000)
        except Exception:
            logger.info("Popup did not appear or was already closed.")
        self.page.wait_for_timeout(5000)