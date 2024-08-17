import allure
from locators.login_page_locators import LoginPageLocators
from pages.base_page import StellarBurgersBasePage


class StellarBurgersLoginPage(StellarBurgersBasePage):

    @allure.step('Подождать загрузки кнопки "Восстановить пароль" и кликнуть на нее')
    def wait_for_load_password_recovery_button_and_click(self):
        self.find_element_located(LoginPageLocators.PASSWORD_RECOVERY_BUTTON).click()

    @allure.step('Подождать загрузки поля "email" и ввести в него {email}')
    def wait_for_load_email_field_and_enter_email(self, email):
        self.find_element_located(LoginPageLocators.EMAIL_FIELD).send_keys(email)

    @allure.step('Подождать загрузки поля "email" и ввести в него {password}')
    def wait_for_load_password_field_and_enter_password(self, password):
        self.find_element_located(LoginPageLocators.PASSWORD_FIELD).send_keys(password)

    @allure.step('Подождать загрузки кнопки "Войти" и кликнуть на нее')
    def wait_for_load_enter_button_and_click(self):
        self.find_element_located(LoginPageLocators.ENTER_BUTTON).click()
