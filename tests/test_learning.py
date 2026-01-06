import time 

def test_timeout(page):
    page.goto("https://playwright.dev/python/docs/waits")
    start_time = time.time()
    page.click('text=Getting started')
    
    # #10 seconds wait time for the element to be clicked 
    # page.click('tedt=Getting started', timeout=1000)
    end_time = time.time()
    print(f'start time is {start_time} and end time is {end_time} and total time taken is = {end_time - start_time}')

