import allure
from locators.order_feed_page_locators import OrderFeedPageLocators
from pages.base_page import StellarBurgersBasePage


class StellarBurgersOrderFeedPage(StellarBurgersBasePage):

    @allure.step('Подождать загрузки заказа и кликнуть по нему')
    def wait_for_load_order_and_click(self):
        self.find_element_located(OrderFeedPageLocators.ORDER).click()

    @allure.step('Подождать загрузки заголовока "Состав" и вывести его текст')
    def wait_for_load_header_composition_and_get_text(self):
        return self.find_element_located(OrderFeedPageLocators.HEADER_COMPOSITION).text

    @allure.step('Подождать загрузки номера заказа и вывести его текст')
    def wait_for_load_order_number_and_get_text(self):
        return self.find_element_located(OrderFeedPageLocators.ORDER_CARD_ID).text

    @allure.step('Вывести значение счетчика "Выполнено за всё время" и вывести его текст')
    def wait_for_load_for_all_time_counter_and_get_text(self):
        return self.find_element_located(OrderFeedPageLocators.FOR_ALL_TIME_COUNTER).text

    @allure.step('Подождать загрузки кнопки "Конструктор" и кликнуть по ней')
    def wait_for_load_constructor_button_and_click(self):
        self.find_element_located(OrderFeedPageLocators.CONSTRUCTOR_BUTTON).click()

    @allure.step('Пролистать к счетчику "Выполнено за сегодня" и вывести его текст')
    def scroll_to_for_today_counter_and_get_text(self):
        return self.scroll_to_element(OrderFeedPageLocators.FOR_TODAY_COUNTER).text

    @allure.step('Подождать загрузки заказа в поле "В работе" и вывести его текст')
    def wait_for_load_order_in_progress_field_and_get_text(self):
        return self.find_element_located(OrderFeedPageLocators.IN_PROGRESS_FIELD).text
