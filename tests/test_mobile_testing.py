def test_mobile_login(playwright, browser):
    iphone = playwright.devices["iPhone 11"]

    context = browser.new_context(**iphone, record_video_dir="reports/")
    page = context.new_page()

    page.goto("https://opensource-demo.orangehrmlive.com")
    page.fill("input[name='username']", "Admin")
    page.fill("input[name='password']", "admin123")
    page.click("button[type='submit']")

    page.wait_for_timeout(3000)
    #taking the screenshot 
    page.screenshot(path="reports/screenshot.png", full_page=True)
    #take screenshot based on layout
    # page.locator('div.orangehrm-login-form').screenshot(path="reports/screenshot.png")

    context.close()
