import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import StellarBurgersBasePage


class StellarBurgersMainPage(StellarBurgersBasePage):

    @allure.step('Подождать загрузки кнопки "Войти в аккаунт" и кликнуть на нее')
    def wait_for_load_login_to_account_button_and_click(self):
        self.find_element_located(MainPageLocators.LOGIN_TO_ACCOUNT_BUTTON).click()

    @allure.step('Подождать загрузки кнопки "Личный кабинет" и кликнуть по ней')
    def wait_for_load_personal_account_button_and_click(self):
        self.find_element_located(MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

    @allure.step('Подождать загрузки кнопки "Конструктор" и кликнуть по ней')
    def wait_for_load_constructor_button_and_click(self):
        self.find_element_located(MainPageLocators.CONSTRUCTOR_BUTTON).click()

    @allure.step('Подождать загрузки заголовка "Соберите бургер" и вывести его текст')
    def wait_for_load_header_construct_burger_and_get_text(self):
        return self.find_element_located(MainPageLocators.HEADER_CONSTRUCT_BURGER).text

    @allure.step('Подождать загрузки кнопки ингридиента "Краторная булка N-200i" и кликнуть по ней')
    def wait_for_load_crater_loaf_n_200i_button_and_click(self):
        self.find_element_located(MainPageLocators.CRATER_LOAF_N_200I_BUTTON).click()

    @allure.step('Подождать загрузки заголовка "Детали ингредиента" и вывести его текст')
    def wait_for_load_header_ingredient_details_and_get_text(self):
        return self.find_element_located(MainPageLocators.HEADER_INGREDIENT_DETAILS).text

    @allure.step('Вывести название ингредиента из всплывающего окна "Детали ингредиента"')
    def wait_for_load_ingredient_in_ingredient_details_and_get_text(self):
        return self.find_element_located(MainPageLocators.INGREDIENT_NAME_IN_INGREDIENT_DETAILS).text

    @allure.step('Подождать загрузки кнопки крестик и кликнуть по нему')
    def wait_for_load_cross_mark_button_and_click(self):
        self.find_element_located(MainPageLocators.CROSS_MARK_BUTTON).click()

    @allure.step('Найти заголовок "Детали ингредиента"')
    def find_header_ingredient_details(self):
        self.find_element(MainPageLocators.HEADER_INGREDIENT_DETAILS)

    @allure.step('Подождать загрузки кнопки "Краторная булка N-200i", нажать на нее и перемести в поле заказа')
    def wait_for_load_crater_loaf_n_200i_button_drag_and_drop_to_order_field(self):
        source = self.find_element_located(MainPageLocators.CRATER_LOAF_N_200I_BUTTON)
        target = self.find_element_located(MainPageLocators.ORDER_FIELD)
        self.drag_and_drop_element(source, target)

    @allure.step('Вывести значение счетчика ингредиента "Краторная булка N-200i"')
    def wait_for_load_ingredient_count_of_crater_loaf_n_200i_and_get_text(self):
        return self.find_element_located(MainPageLocators.INGREDIENT_COUNT_OF_CRATER_LOAF_N_200I).text

    @allure.step('Подождать загрузки кнопки "Оформить заказ" и кликнуть по ней')
    def wait_for_load_place_an_order_button_and_click(self):
        self.find_element_located(MainPageLocators.PLACE_AN_ORDER_BUTTON).click()

    @allure.step('Подождать загрузки текста о готовности заказа во всплывающем окне "Заказ" и вывести его текст')
    def wait_for_load_text_about_readiness_order_and_get_text(self):
        return self.find_element_located(MainPageLocators.TEXT_ABOUT_READINESS_ORDER).text

    @allure.step('Подождать загрузки кнопки "Лента заказов" и кликнуть по ней')
    def wait_for_load_order_feed_button_and_click(self):
        self.find_element_located(MainPageLocators.ORDER_FEED_BUTTON).click()

    @allure.step('Подождать загрузки идентификатора заказа и вывести его текст')
    def wait_for_load_order_id_and_get_text(self):
        return self.find_element_located(MainPageLocators.ORDER_ID).text

    @allure.step('Подождать пока значек загрузки в окне "Заказ" исчезнет')
    def wait_for_loading_icon_go_away(self):
        self.wait_for_element_go_away(MainPageLocators.LOADING_ICON)

    @allure.step('Создать заказ')
    def create_order(self):
        source = self.find_element_located(MainPageLocators.CRATER_LOAF_N_200I_BUTTON)
        target = self.find_element_located(MainPageLocators.ORDER_FIELD)
        self.drag_and_drop_element(source, target)
        self.find_element_located(MainPageLocators.PLACE_AN_ORDER_BUTTON).click()
        self.wait_for_element_go_away(MainPageLocators.LOADING_ICON)
        self.find_element_located(MainPageLocators.CROSS_MARK_BUTTON).click()
