from playwright.sync_api import expect

class ProfileComponent:
    def __init__(self,page):
        self.user_profile = page.locator("//p[@class='oxd-userdropdown-name']")
        self.about = page.get_by_role('link', name="About")
        self.support =  page.get_by_role('link', name="Support")
        self.change_password = page.get_by_role('link', name="Change Password")
        self.logout = page.get_by_role("menuitem", name="Logout")

    def click_user_profile(self):
        self.user_profile.click()
     

    def click_about(self):
        self.about.click()
    def click_support(self):
        self.support.click()
    def click_change_password(self):
        self.change_password.click()
    def click_logout(self):
        self.logout.click()
