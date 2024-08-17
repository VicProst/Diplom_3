import allure
from locators.reset_password_page_locators import ResetPasswordPageLocators
from pages.base_page import StellarBurgersBasePage


class StellarBurgersResetPasswordPage(StellarBurgersBasePage):

    @allure.step('Подождать загрузки кнопки показать/скрыть и кликнуть на нее')
    def wait_for_load_show_hide_button_and_click(self):
        self.find_element_located(ResetPasswordPageLocators.SHOW_HIDE_BUTTON).click()

    @allure.step('Полождать загрузки границ поля "email" и вывести текст атрибута "class"')
    def wait_for_load_boundaries_email_field_and_get_attribute(self):
        return self.find_element_located(ResetPasswordPageLocators.BOUNDARIES_EMAIL_FIELD).get_attribute('class')

    @allure.step('Полождать загрузки плейсхолдера поля "email" и вывести текст атрибута "class"')
    def wait_for_load_placeholder_email_field_and_get_attribute(self):
        return self.find_element_located(ResetPasswordPageLocators.PLACEHOLDER_EMAIL_FIELD).get_attribute('class')
