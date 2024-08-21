import allure
from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from pages.base_page import StellarBurgersBasePage


class StellarBurgersForgotPasswordPage(StellarBurgersBasePage):

    @allure.step('Подождать загрузки поля "email" и ввести в него {email}')
    def wait_for_load_email_field_and_enter_email(self, email):
        self.find_element_located(ForgotPasswordPageLocators.EMAIL_FIELD).send_keys(email)

    @allure.step('Кликнуть на кнопку "Восстановить"')
    def click_to_restore_button(self):
        self.click_to_element(ForgotPasswordPageLocators.RESTORE_BUTTON)
