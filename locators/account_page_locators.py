from selenium.webdriver.common.by import By


class AccountPageLocators:

        # Кнопки "История заказов"
    ORDER_HISTORY_BUTTON = (By.XPATH, '//a[@href="/account/order-history"]')

        # Кнопка "Выход" на странице личного кабинета
    EXIT_BUTTON = (By.XPATH, '//button[contains(@class,"Account_button")]')
