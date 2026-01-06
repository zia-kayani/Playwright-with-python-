from playwright.sync_api import expect
import pytest

@pytest.mark.login_required
def test_login_success(loggedin_already):
    page =  loggedin_already
    assert page.url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

def test_without_login_hook(page):
    print('no hook here')
    assert True
  

