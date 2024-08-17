import allure
from data import Constants
from pages.main_page import StellarBurgersMainPage
from pages.login_page import StellarBurgersLoginPage
from pages.forgot_password_page import StellarBurgersForgotPasswordPage
from pages.reset_password_page import StellarBurgersResetPasswordPage
from conftest import driver, reg_new_user_return_email_pass_del_this_user


@allure.epic('test_stellar_burgers_forgot_password_page')
class TestStellarBurgersForgotPasswordPage:

    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке "Восстановить пароль"')
    @allure.description('При клике на кнопку "Восстановить пароль" открывается страница восстановления пароля')
    def test_password_recovery_click_restore_password_button_password_recovery_page_will_open(self, driver):
        main_page = StellarBurgersMainPage(driver)
        main_page.go_to_site(Constants.MAIN_URL)
        main_page.wait_for_load_login_to_account_button_and_click()
        login_page = StellarBurgersLoginPage(driver)
        login_page.wait_for_load_password_recovery_button_and_click()
        login_page.wait_url_contains(Constants.FORGOT_PASSWORD_URL)
        forgot_password_page = StellarBurgersForgotPasswordPage(driver)
        current_url = forgot_password_page.check_url()
        assert current_url == Constants.FORGOT_PASSWORD_URL

    @allure.title('Проверка перехода на страницу сброса пароля по кнопке "Восстановить"')
    @allure.description('При вводе существующего пароля и клике на кнопку "Восстановить" '
                        'открывается страница сброса пароля')
    def test_password_recovery_valid_email_click_restore_button_reset_password_page_will_open(self,
                                                        driver, reg_new_user_return_email_pass_del_this_user):
        main_page = StellarBurgersMainPage(driver)
        main_page.go_to_site(Constants.MAIN_URL)
        main_page.wait_for_load_login_to_account_button_and_click()
        login_page = StellarBurgersLoginPage(driver)
        login_page.wait_for_load_password_recovery_button_and_click()
        forgot_password_page = StellarBurgersForgotPasswordPage(driver)
        email_pass = reg_new_user_return_email_pass_del_this_user[1]
        forgot_password_page.wait_for_load_email_field_and_enter_email(email_pass[0])
        forgot_password_page.click_to_restore_button()
        forgot_password_page.wait_url_contains(Constants.RESET_PASSWORD_URL)
        reset_password_page = StellarBurgersResetPasswordPage(driver)
        current_url = reset_password_page.check_url()
        assert current_url == Constants.RESET_PASSWORD_URL

    @allure.title('Проверка активации поля "Пароль" по кнопке "показать/скрыть"')
    @allure.description('При клике на кнопку "показать/скрыть" поле "Пароль" становится активным')
    def test_password_recovery_click_show_hide_button_password_field_is_active(self,
                                                        driver, reg_new_user_return_email_pass_del_this_user):
        main_page = StellarBurgersMainPage(driver)
        main_page.go_to_site(Constants.MAIN_URL)
        main_page.wait_for_load_login_to_account_button_and_click()
        login_page = StellarBurgersLoginPage(driver)
        login_page.wait_for_load_password_recovery_button_and_click()
        forgot_password_page = StellarBurgersForgotPasswordPage(driver)
        email_pass = reg_new_user_return_email_pass_del_this_user[1]
        forgot_password_page.wait_for_load_email_field_and_enter_email(email_pass[0])
        forgot_password_page.click_to_restore_button()
        reset_password_page = StellarBurgersResetPasswordPage(driver)
        reset_password_page.wait_for_load_show_hide_button_and_click()
        boundaries_condition = reset_password_page.wait_for_load_boundaries_email_field_and_get_attribute()
        placeholder_condition = reset_password_page.wait_for_load_placeholder_email_field_and_get_attribute()
        assert 'input_status_active' in boundaries_condition and 'input__placeholder-focused' in placeholder_condition
