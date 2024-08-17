import allure
from locators.account_page_locators import AccountPageLocators
from pages.base_page import StellarBurgersBasePage


class StellarBurgersAccountPage(StellarBurgersBasePage):

    @allure.step('Подождать загрузки кнопки "История заказов" и кликнуть на нее')
    def wait_for_load_order_history_button_and_click(self):
        self.find_element_located(AccountPageLocators.ORDER_HISTORY_BUTTON).click()

    @allure.step('Подождать загрузки кнопки "Выход" и кликнуть на нее')
    def wait_for_load_exit_button_and_click(self):
        self.find_element_located(AccountPageLocators.EXIT_BUTTON).click()
