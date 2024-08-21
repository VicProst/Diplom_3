from selenium.webdriver.common.by import By


class OrderFeedPageLocators:

        # Карточка заказа
    ORDER = (By.XPATH, '//li[contains(@class,"OrderHistory_listItem")]')

        # Заголовок "Состав"
    HEADER_COMPOSITION = (By.XPATH, '//p[contains(@class,"text text_type_main-medium mb-8")]')

        # Номер карточки заказа
    ORDER_CARD_ID = (By.XPATH, '//p[contains(@class,"text text_type_digits-default")]')

        # Кнопка "Конструктор"
    CONSTRUCTOR_BUTTON = (By.XPATH, '//a[@href="/"]/p[contains(@class,"AppHeader_header")]')

        # Cчетчик "Выполнено за всё время"
    FOR_ALL_TIME_COUNTER = (By.XPATH, '//div[2]/p[contains(@class,"OrderFeed_number")]')

        # Cчетчик "Выполнено за сегодня"
    FOR_TODAY_COUNTER = (By.XPATH, '//div[3]/p[contains(@class,"OrderFeed_number")]')

        # Поле "В работе"
    IN_PROGRESS_FIELD = (By.XPATH, '//ul[2]/li[contains(@class, "text_type_digits")]')
