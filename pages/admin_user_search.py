import re
from playwright.sync_api import Page, expect

class AdminUserSearchPage:
    def __init__(self, page:Page):
        self.page = page
        self.click_on_admin = page.get_by_role("link", name="Admin")
        self.username_input =  page.get_by_role("textbox").nth(1)
        self.select_user_option = page.get_by_text("-- Select --").first
        self.select_user_role = page.get_by_role("option", name="ESS")
        
        self.employeename_input = page.get_by_role("textbox", name="Type for hints...")
        self.select_employee_from_option =  page.get_by_role("option", name="hoa le")

        self.click_status_dropdown = page.locator("div").filter(has_text=re.compile(r"^-- Select --$")).nth(2)
        self.select_enabled = page.get_by_role("listbox").get_by_text("Enabled")

        self.search_button =  page.get_by_role("button", name="Search")

    
    def admin_click(self):
        self.click_on_admin.click()

    def enter_username(self, username:str):
        self.username_input.fill(username)
    
    def select_user_role_admin_or_ess(self):
        self.select_user_option.click()
        self.select_user_role.click()
    def enter_employeename_hint(self, employeename:str):
        self.employeename_input.fill(employeename)
        self.select_employee_from_option.click()
    
    def select_status(self):
        self.click_status_dropdown.click()
        self.select_enabled.click()
    
    def click_search_button(self):
        expect(self.search_button).to_be_enabled()
        self.search_button.click()

    

    

    



# def test_example(page: Page) -> None:
    # page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    # page.get_by_role("textbox", name="Username").click()
    # page.get_by_role("textbox", name="Username").fill("Admin")
    # page.get_by_role("textbox", name="Password").click()
    # page.get_by_role("textbox", name="Password").fill("admin123")
    # page.get_by_role("button", name="Login").click()
    # page.get_by_role("link", name="Admin").click()
    # page.get_by_role("textbox").nth(1).click()
    # page.get_by_role("textbox").nth(1).fill("hoale")

    # page.get_by_text("-- Select --").first.click()
    # page.get_by_role("option", name="ESS").click()

    # page.get_by_role("textbox", name="Type for hints...").fill("hoa le")
    # page.get_by_role("option", name="hoa le").click()
    # page.locator("div").filter(has_text=re.compile(r"^-- Select --$")).nth(2).click()
    # page.get_by_role("listbox").get_by_text("Enabled").click()
    # page.get_by_role("button", name="Search").click()
