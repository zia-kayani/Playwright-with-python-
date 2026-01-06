from pages.orangeHRM_login_page import LoginPage
from pages.orangeHRM_homepage_page  import HomePage
from pages.admin_user_search import AdminUserSearchPage
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def login_page(page):
    return LoginPage(page)  
@pytest.fixture
def home_page(page):
    return HomePage(page)
@pytest.fixture
def admin_user_search_page(page):
    return AdminUserSearchPage(page)

import pytest
# Hook for the tests where login is pre-requisite
@pytest.fixture(autouse=True)
def loggedin_already(request):
    
    # only run for tests marked with "login_required"
    if 'login_required' not in request.keywords:
        yield
        return
    
    with sync_playwright() as p:
        #------- before each ---------
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        page.locator("input[name='username']").fill("Admin")
        page.locator("input[name='password']").fill("admin123")
        page.locator("button[type='submit']").click()

        yield page
        #------- after each ----------
        print('\n')
        browser.close()

