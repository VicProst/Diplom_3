import allure
from data import Constants
from pages.main_page import StellarBurgersMainPage
from pages.account_page import StellarBurgersAccountPage
from conftest import driver, reg_new_user_return_email_pass_del_this_user, login_new_user


@allure.epic('test_stellar_burgers_account_page')
class TestStellarBurgersAccountPage:

    @allure.title('Проверка перехода на страницу личного кабинета по кнопке "Личный кабинет"')
    @allure.description('При клике на кнопку "Личный кабинет" авторизованный пользователь может перейти '
                        'на страницу личного кабинета')
    def test_account_auth_user_click_personal_account_button_account_page_will_open(self, driver,
                                reg_new_user_return_email_pass_del_this_user, login_new_user):
        main_page = StellarBurgersMainPage(driver)
        main_page.wait_for_load_personal_account_button_and_click()
        main_page.wait_url_contains(Constants.ACCOUNT_PROFILE_URL)
        account_page = StellarBurgersAccountPage(driver)
        current_url = account_page.check_url()
        assert current_url == Constants.ACCOUNT_PROFILE_URL

    @allure.title('Проверка перехода в раздел "История заказов" по кнопке "История заказов"')
    @allure.description('При клике на кнопку "История заказов" пользователь может перейти в раздел "История заказов"')
    def test_account_click_order_history_button_chapter_order_history_will_open(self, driver,
                                reg_new_user_return_email_pass_del_this_user, login_new_user):
        main_page = StellarBurgersMainPage(driver)
        main_page.wait_for_load_personal_account_button_and_click()
        account_page = StellarBurgersAccountPage(driver)
        account_page.wait_for_load_order_history_button_and_click()
        account_page.wait_url_contains(Constants.ACCOUNT_ORDER_HISTORY_URL)
        current_url = account_page.check_url()
        assert current_url == Constants.ACCOUNT_ORDER_HISTORY_URL

    @allure.title('Проверка выхода из аккаунта по кнопке "Выход"')
    @allure.description('При клике на кнопку "Выход" пользователь выходит из аккаунта')
    def test_account_click_exit_button_login_page_will_open(self, driver,
                                reg_new_user_return_email_pass_del_this_user, login_new_user):
        main_page = StellarBurgersMainPage(driver)
        main_page.wait_for_load_personal_account_button_and_click()
        account_page = StellarBurgersAccountPage(driver)
        account_page.wait_for_load_exit_button_and_click()
        account_page.wait_url_contains(Constants.LOGIN_URL)
        current_url = account_page.check_url()
        assert current_url == Constants.LOGIN_URL
