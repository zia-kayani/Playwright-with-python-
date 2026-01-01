from pages.orangeHRM_login_page import LoginPage
from pages.orangeHRM_homepage_page  import HomePage
from pages.admin_user_search import AdminUserSearchPage
import pytest

@pytest.fixture
def login_page(page):
    return LoginPage(page)  
@pytest.fixture
def home_page(page):
    return HomePage(page)
@pytest.fixture
def admin_user_search_page(page):
    return AdminUserSearchPage(page)