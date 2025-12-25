
def test_example(browser, base_url):
    page = browser.new_page()
    page.goto(base_url)
    page.get_by_role("textbox", name="Username").fill("Admin")
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("link", name="Admin").click()
