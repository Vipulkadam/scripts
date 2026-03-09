
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def browser_page():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        yield page

        context.close()
        browser.close()

#extara for handleing multiple browsers
# @pytest.fixture(params=["chromium", "firefox"])
# def browser_page(request):
#
#     with sync_playwright() as p:
#
#         browser = getattr(p, request.param).launch(headless=False)
#
#         context = browser.new_context()
#
#         page = context.new_page()
#
#         yield page
#
#         context.close()
#         browser.close()

@pytest.hookimpl(hookwrapper=True)

def pytest_runtest_makereport(item):

    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:

        page = item.funcargs.get("browser_page")

        if page:
            page.screenshot(path="Screenshots/failure.png")