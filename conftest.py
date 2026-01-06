
import pytest



# #Added this fixture so that tracing should work 
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