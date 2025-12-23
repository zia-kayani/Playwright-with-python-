import re
import pytest
from playwright.sync_api import Page, expect

#csv file 
def get_csv_data() -> list:
    data = []
    import csv
    with open('./test-data/data.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)
        return data

#Json file data
def get_json_data():
    import json
    with open('./test-data/data.json', 'r') as fl:
        data =  json.load(fl)
        return ((item['username'], item['password']) for item in data)

@pytest.mark.parametrize('username,password', 
# [
#     ('Admin', 'admin123'),
#     ('naila', 'naila123')
# ]
# get_csv_data()
get_json_data()
)

def test_example(page: Page, username, password) -> None:
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill(username)
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill(password)
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_role("link", name="Dashboard")).to_be_visible()
