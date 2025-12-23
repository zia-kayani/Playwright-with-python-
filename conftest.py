
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

# #Added this fixture so that my tracing should work 
# #this will create the seperate context of the browser 
@pytest.fixture
def context(browser):
    context = browser.new_context()

    context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )

    yield context

    context.tracing.stop(path="trace.zip")
    context.close()

@pytest.fixture
def page(context):
    page = context.new_page()
    yield page
    page.close()