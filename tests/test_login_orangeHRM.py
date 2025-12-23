
import re
from playwright.sync_api import Page, expect

from pages.orangeHRM_login_page import LoginPage
from pages.orangeHRM_homepage_page  import HomePage
#for Admin and search 
from pages.admin_user_search import AdminUserSearchPage

def test_example(page: Page) -> None:
    login_page = LoginPage(page)
    home_page =  HomePage(page)
    admin_user_search_page =  AdminUserSearchPage(page)

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login_page.enter_username('Admin')
    login_page.enter_password('admin123')
    login_page.click_login()

    home_page.is_upgrade_button_visible()
    home_page.click_performance()
    home_page.is_upgrade_button_visible()

    #Admin userserach 
    admin_user_search_page.admin_click()
    admin_user_search_page.enter_username('hoale')
    admin_user_search_page.select_user_role_admin_or_ess()
    admin_user_search_page.enter_employeename_hint('hoa le')
    admin_user_search_page.select_status()
    admin_user_search_page.click_search_button()


