from playwright.sync_api import expect

def test_login_success(page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Verify we're on the login page
    expect(page.locator("//h5[normalize-space()='Login']")).to_have_text('Login')

    # Perform login
    page.locator("input[name='username']").fill("Admin")
    page.locator("input[name='password']").fill("admin123")
    page.locator("input[name='username']").clear()
    page.locator("input[name='password']").clear()
    page.pause()
    page.locator("button[type='submit']").click()

  

