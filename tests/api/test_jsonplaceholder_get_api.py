import playwright

def test_api(playwright):
    request =  playwright.request.new_context()
    response = request.get('https://jsonplaceholder.typicode.com/posts/1',
                            headers={'Accept':'application/json'}
    
    )
    jsondata = response.json()

    print(jsondata)

    assert response.status  == 200
    assert jsondata['id'] == 1
    request.dispose()
