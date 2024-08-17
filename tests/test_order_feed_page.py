import allure
from data import Constants
from pages.main_page import StellarBurgersMainPage
from pages.order_feed_page import StellarBurgersOrderFeedPage
from conftest import driver, reg_new_user_return_email_pass_del_this_user, login_new_user, create_new_order


@allure.epic('test_stellar_burgers_order_feed_page')
class TestStellarBurgersOrderFeedPage:

    @allure.title('Проверка перехода на страницу "Лента заказов" по кнопке "Лента заказов"')
    @allure.description('При клике на кнопку "Лента заказов" можно перейти на страницу "Лента заказов"')
    def test_order_feed_click_order_feed_button_order_feed_page_will_open(self, driver):
        main_page = StellarBurgersMainPage(driver)
        main_page.go_to_site(Constants.MAIN_URL)
        main_page.wait_for_load_order_feed_button_and_click()
        main_page.wait_url_contains(Constants.ORDER_FEED_URL)
        order_feed_page = StellarBurgersOrderFeedPage(driver)
        current_url = order_feed_page.check_url()
        assert current_url == Constants.ORDER_FEED_URL

    @allure.title('Проверка открытия всплывающего окна с деталями заказа, если кликнуть на заказ')
    @allure.description('При клике на заказ, откроется всплывающее окно с деталями заказа')
    def test_order_feed_click_order_header_composition_will_open(self, driver):
        main_page = StellarBurgersMainPage(driver)
        main_page.go_to_site(Constants.MAIN_URL)
        main_page.wait_for_load_order_feed_button_and_click()
        order_feed_page = StellarBurgersOrderFeedPage(driver)
        order_feed_page.wait_for_load_order_and_click()
        header = order_feed_page.wait_for_load_header_composition_and_get_text()
        assert header == 'Cостав'

    @allure.title('Проверка отображения заказов на странице "Лента заказов" из раздела "История заказов"')
    @allure.description('Заказы из раздела "История заказов" отображаются на странице "Лента заказов"')
    def test_order_feed_auth_user_create_order_order_id_visible_in_order_card_number(self, driver,
                                 reg_new_user_return_email_pass_del_this_user, login_new_user, create_new_order):
        main_page = StellarBurgersMainPage(driver)
        main_page.wait_for_load_order_feed_button_and_click()
        order_feed_page = StellarBurgersOrderFeedPage(driver)
        order_id = create_new_order
        order_feed_page.wait_for_load_order_and_click()
        order_card_number = order_feed_page.wait_for_load_order_number_and_get_text()
        assert order_id in order_card_number

    @allure.title('Проверка увеличения числа в счётчике "Выполнено за всё время", после создания нового заказа')
    @allure.description('После создания нового заказа, число в счётчике "Выполнено за всё время" увеличивается')
    def test_order_feed_auth_user_create_order_all_time_counter_number_increasing(self, driver,
                                                    reg_new_user_return_email_pass_del_this_user, login_new_user):
        main_page = StellarBurgersMainPage(driver)
        main_page.wait_for_load_order_feed_button_and_click()
        order_feed_page = StellarBurgersOrderFeedPage(driver)
        counter_before = order_feed_page.wait_for_load_for_all_time_counter_and_get_text()
        order_feed_page.wait_for_load_constructor_button_and_click()
        main_page.create_order()
        main_page.wait_for_load_order_feed_button_and_click()
        counter_after = order_feed_page.wait_for_load_for_all_time_counter_and_get_text()
        assert counter_after > counter_before

    @allure.title('Проверка увеличения числа в счётчике "Выполнено за сегодня", после создания нового заказа')
    @allure.description('После создания нового заказа, число в счётчике "Выполнено за сегодня" увеличивается')
    def test_order_feed_auth_user_create_order_for_today_counter_number_increasing(self, driver,
                                                    reg_new_user_return_email_pass_del_this_user, login_new_user):
        main_page = StellarBurgersMainPage(driver)
        main_page.wait_for_load_order_feed_button_and_click()
        order_feed_page = StellarBurgersOrderFeedPage(driver)
        counter_before = order_feed_page.scroll_to_for_today_counter_and_get_text()
        order_feed_page.wait_for_load_constructor_button_and_click()
        main_page.create_order()
        main_page.wait_for_load_order_feed_button_and_click()
        counter_after = order_feed_page.scroll_to_for_today_counter_and_get_text()
        assert counter_after > counter_before

    @allure.title('Проверка появления номера заказа в разделе "В работе", после оформления заказа')
    @allure.description('После оформления нового заказа, его номер появляется в разделе "В работе"')
    def test_order_feed_auth_user_create_order_order_id_visible_in_in_progress_field(self, driver,
                                 reg_new_user_return_email_pass_del_this_user, login_new_user, create_new_order):
        main_page = StellarBurgersMainPage(driver)
        main_page.wait_for_load_order_feed_button_and_click()
        order_feed_page = StellarBurgersOrderFeedPage(driver)
        order_in_progress = order_feed_page.wait_for_load_order_in_progress_field_and_get_text()
        order_id = create_new_order
        assert order_id in order_in_progress
