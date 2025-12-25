
import pytest

##### commented out the below browser fixture bcz it was creating conflict with pytest-playwright browser module
####   so to get rid of conflict and by defutl use that browser i commented out this 
# from playwright.sync_api import sync_playwright

# @pytest.fixture(scope="session")
# def browser():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         yield browser
#         browser.close()

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


# -------- code to manage the urls based on enviroments- --------
from config.env_config import ENV_CONFIG

def pytest_addoption(parser):
    parser.addoption("--env", default="qa")

@pytest.fixture(scope="session")
def env(request):
    return request.config.getoption("--env")

@pytest.fixture(scope="session")
def base_url(env):
    return ENV_CONFIG[env]["base_url"]
