from playwright.sync_api import sync_playwright

#multiple tabs and pages
def test_multiple_tabs_and_pages():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()

        page1 =  context.new_page()
        page1.goto("https://www.google.com")

        page2 =  context.new_page()
        page2.goto("https://www.bing.com")

def test_open_new_page_on_click(page, context):
    # Open a page with a link that opens in a new tab
    page.goto("https://www.helloworld.org/")  # Replace with your test site

    # Wait for a new page to open from the click
    with context.expect_page() as new_page_info:
        page.click("a[target='_blank']")  # must exist on the page

    new_page = new_page_info.value
    new_page.wait_for_load_state()
    print(new_page.title())



#to switch between the tabs and pages
def test_switch_between_tabs_and_pages(page, context):
    import time
    page1 =  context.new_page()
    page1.goto("https://www.google.com")

    page2 =  context.new_page()
    page2.goto("https://www.bing.com")


    all_pages = context.pages
    p1 =  all_pages[1]
    print(p1.title())

    p2 =  all_pages[2]
    print(p2.title())

    time.sleep(10)


        



       
       