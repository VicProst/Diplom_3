import allure
from data import Constants
from pages.main_page import StellarBurgersMainPage
from conftest import driver, reg_new_user_return_email_pass_del_this_user, login_new_user


@allure.epic('test_stellar_burgers_main_page')
class TestStellarBurgersMainPage:

    @allure.title('Проверка перехода на главную страницу по кнопке "Конструктор"')
    @allure.description('При клике на кнопку "Конструктор" открывается главная страница')
    def test_constructor_click_constructor_button_header_construct_burger_will_open(self, driver):
        main_page = StellarBurgersMainPage(driver)
        main_page.go_to_site(Constants.MAIN_URL)
        main_page.wait_for_load_personal_account_button_and_click()
        main_page.wait_for_load_constructor_button_and_click()
        header = main_page.wait_for_load_header_construct_burger_and_get_text()
        assert header == 'Соберите бургер'

    @allure.title('Проверка появления всплывающего окна с деталями, если кликнуть на ингредиент')
    @allure.description('При клике на ингредиент, появится всплывающее окно с деталями')
    def test_constructor_click_ingredient_header_ingredient_details_will_open(self, driver):
        main_page = StellarBurgersMainPage(driver)
        main_page.go_to_site(Constants.MAIN_URL)
        main_page.wait_for_load_crater_loaf_n_200i_button_and_click()
        header = main_page.wait_for_load_header_ingredient_details_and_get_text()
        ingredient = main_page.wait_for_load_ingredient_in_ingredient_details_and_get_text()
        assert header == 'Детали ингредиента' and ingredient == 'Краторная булка N-200i'

    @allure.title('Проверка закрытия всплывающего окна с деталями, если кликнуть на крестик')
    @allure.description('При клике на крестик, всплывающего окна с деталями закроется')
    def test_constructor_click_cross_mark_button_header_ingredient_details_is_none(self, driver):
        main_page = StellarBurgersMainPage(driver)
        main_page.go_to_site(Constants.MAIN_URL)
        main_page.wait_for_load_crater_loaf_n_200i_button_and_click()
        main_page.wait_for_load_cross_mark_button_and_click()
        header = main_page.find_header_ingredient_details()
        assert header == None

    @allure.title('Проверка увеличения каунтера определенного ингредиента, если добавить его в заказ')
    @allure.description('При добавлении ингредиента в заказ, увеличивается каунтер эго ингредиента')
    def test_constructor_add_ingredient_to_order_counter_increasing(self, driver):
        main_page = StellarBurgersMainPage(driver)
        main_page.go_to_site(Constants.MAIN_URL)
        main_page.wait_for_load_crater_loaf_n_200i_button_drag_and_drop_to_order_field()
        quantity = main_page.wait_for_load_ingredient_count_of_crater_loaf_n_200i_and_get_text()
        assert int(quantity) > 0

    @allure.title('Проверка оформления заказа залогиненным пользователем')
    @allure.description('Залогиненный пользователь может оформить заказ')
    def test_constructor_auth_user_added_ingredient_text_about_readiness_will_open(self, driver,
                                                    reg_new_user_return_email_pass_del_this_user, login_new_user):
        main_page = StellarBurgersMainPage(driver)
        main_page.wait_for_load_crater_loaf_n_200i_button_drag_and_drop_to_order_field()
        main_page.wait_for_load_place_an_order_button_and_click()
        text = main_page.wait_for_load_text_about_readiness_order_and_get_text()
        assert text == 'Ваш заказ начали готовить'
