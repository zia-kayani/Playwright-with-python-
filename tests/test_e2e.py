def test_admin_user_searh(page, login_page, home_page, admin_user_search_page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    login_page.enter_username('Admin')
    login_page.enter_password('admin123')
    login_page.click_login()

    home_page.is_upgrade_button_visible()
    home_page.click_performance()
    home_page.profile_component.click_user_profile()
    home_page.profile_component.click_logout()
    home_page.is_upgrade_button_visible()

    #Admin userserach 
    admin_user_search_page.admin_click()
    admin_user_search_page.enter_username('hoale')
    admin_user_search_page.select_user_role_admin_or_ess()
    admin_user_search_page.enter_employeename_hint('hoa le')
    admin_user_search_page.select_status()
    admin_user_search_page.click_search_button()

