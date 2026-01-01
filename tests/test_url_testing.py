
def test_example(browser, base_url):
    # context = browser.new_context(viewport=None)
    context =  browser.new_context(   #controle the widht and height of the viewport 
            viewport={"width": 1920, "height": 1080}
    )
    page = context.new_page()
    page.goto(base_url)
    page.get_by_role("textbox", name="Username").fill("Admin")
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("link", name="Admin").click()
