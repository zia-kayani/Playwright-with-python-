import time 

def test_timeout(page):
    page.goto("https://playwright.dev/python/docs/waits")
    start_time = time.time()
    page.click('text=Getting started')
    
    # #10 seconds wait time for the element to be clicked 
    # page.click('tedt=Getting started', timeout=1000)
    end_time = time.time()
    print(f'start time is {start_time} and end time is {end_time} and total time taken is = {end_time - start_time}')

    #------------ implicit waiting for an elements based on selector -------
    page.wait_for_selector('div#message')   #waits until the element is present in the DOM
    page.wait_for_selector('div#message', state='visible')  # waits until the element is visible on the page
    page.wait_for_selector('div#message', state='hidden')  # waits until the element is hidden on the page

    #------------------- Network waitings -----------------
    with page.expect_response('**/api/data') as response_info:
        page.click('text=Fetch Data')

    response = response_info.value
    print(response.json())


  #------- defautl and explicit timeout -----
    page.set_default_timeout(5000) # set default timeout for all the operations
    page.wait_for_selector('div#message', timeout=2000) # explicit timeout for a particular operation
    