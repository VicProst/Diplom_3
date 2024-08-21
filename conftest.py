import pytest
from selenium import webdriver
import requests
from data import Constants, APIUserUrls
from generator import register_new_user_and_return_email_password
from pages.login_page import StellarBurgersLoginPage
from pages.main_page import StellarBurgersMainPage


# Открыть браузер 'chrome' и 'firefox', а в конце закрыть их
@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
        driver.maximize_window()
    elif request.param == 'firefox':
        driver = webdriver.Firefox()
        driver.maximize_window()
    else:
        raise ValueError(f'Unknown browser: {request.param}')
    yield driver
    driver.quit()

# Зарегистрировать нового пользователя, вернуть его данные, а в конце удалить этого пользователя
@pytest.fixture
def reg_new_user_return_email_pass_del_this_user():
    response, email_pass = register_new_user_and_return_email_password()
    yield response, email_pass
    token = response.json()['accessToken']
    requests.delete(Constants.MAIN_URL + APIUserUrls.DELETE_USER_URL, headers={'Authorization': token})

# Открыть браузер, зарегистрировать нового пользователя, вернуть его данные, авторизоваться этим пользователем,
# а в конце удалить этого пользователя и закрыть браузер
@pytest.fixture()
def login_new_user(driver, reg_new_user_return_email_pass_del_this_user):
    main_page = StellarBurgersMainPage(driver)
    main_page.go_to_site(Constants.MAIN_URL)
    main_page.wait_for_load_login_to_account_button_and_click()
    login_page = StellarBurgersLoginPage(driver)
    email_pass = reg_new_user_return_email_pass_del_this_user[1]
    login_page.wait_for_load_email_field_and_enter_email(email_pass[0])
    login_page.wait_for_load_password_field_and_enter_password(email_pass[1])
    login_page.wait_for_load_enter_button_and_click()

# Открыть браузер, зарегистрировать нового пользователя, вернуть его данные, авторизоваться этим пользователем,
# создать новый заказ, вернуть его номер, а в конце удалить этого пользователя и закрыть браузер
@pytest.fixture()
def create_new_order(driver, reg_new_user_return_email_pass_del_this_user, login_new_user):
    main_page = StellarBurgersMainPage(driver)
    main_page.wait_for_load_crater_loaf_n_200i_button_drag_and_drop_to_order_field()
    main_page.wait_for_load_place_an_order_button_and_click()
    main_page.wait_for_loading_icon_go_away()
    order_id = main_page.wait_for_load_order_id_and_get_text()
    main_page.wait_for_load_cross_mark_button_and_click()
    return str(order_id)
