from playwright.sync_api import sync_playwright

def test_get_api():
   with sync_playwright() as p:
       request_context = p.request.new_context(
           extra_http_headers={
               'Accept':'application/json',
               'Authorization':'Bearer YOUR_ACCESS_TOKEN',
               'X-Api-kay':'reqres-free-v1'
           }
       )
       response = request_context.get("https://reqres.in/api/users/2")
       assert response.status == 200
       print(response.json())
       request_context.dispose()


