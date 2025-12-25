def test_mobile_login(playwright, browser):
    iphone = playwright.devices["iPhone 11"]

    context = browser.new_context(**iphone)
    page = context.new_page()

    page.goto("https://opensource-demo.orangehrmlive.com")
    page.fill("input[name='username']", "Admin")
    page.fill("input[name='password']", "admin123")
    page.click("button[type='submit']")

    context.close()
