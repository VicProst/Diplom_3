from selenium.webdriver.common.by import By


class MainPageLocators:

        # Кнопка "Войти в аккаунт"
    LOGIN_TO_ACCOUNT_BUTTON = (By.XPATH, '//button[contains(@class,"button_button")]')

        # Кнопка "Оформить заказ"
    PLACE_AN_ORDER_BUTTON = (By.XPATH, '//button[contains(@class,"button_button")]')

        # Кнопка "Конструктор"
    CONSTRUCTOR_BUTTON = (By.XPATH, '//a[@href="/"]/p[contains(@class,"AppHeader_header")]')

        # Кнопка "Лента Заказов"
    ORDER_FEED_BUTTON = (By.XPATH, '//a[@href="/feed"]/p[contains(@class,"AppHeader_header")]')

        # Логотип «stellar burgers»
    LOGO_STELLAR_BURGERS = (By.XPATH, '//div/a[@class="active"]')

        # Кнопка "Личный Кабинет"
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, '//a[@href="/account"]/p[contains(@class,"AppHeader_header")]')

        # Заголовок "Соберите бургер"
    HEADER_CONSTRUCT_BURGER = (By.XPATH, '//h1[contains(@class,"text_type_main")]')

        # Кнопка ингридиента "Краторная булка N-200i"
    CRATER_LOAF_N_200I_BUTTON = (By.XPATH,
                        '//p[contains(@class, "BurgerIngredient_ingredient") and text()="Краторная булка N-200i"]')

        # Заголовок "Детали ингредиента"
    HEADER_INGREDIENT_DETAILS = (By.XPATH, '//h2[contains(@class,"Modal_modal__title_modified")]')

        # Название ингредиента во всплывающем окне "Детали ингредиента"
    INGREDIENT_NAME_IN_INGREDIENT_DETAILS = (By.XPATH, '//p[@class="text text_type_main-medium mb-8"]')

        # Кнопка крестик
    CROSS_MARK_BUTTON = (By.XPATH, '//section[1]//button')

        # Поле заказа
    ORDER_FIELD = (By.XPATH, '//img[contains(@class,"constructor-element__image")]')

        # Счетчик количества ингредиента "Краторная булка N-200i"
    INGREDIENT_COUNT_OF_CRATER_LOAF_N_200I = (By.XPATH, '//ul[1]/a[2]/div[1]/p[contains(@class,"counter_counter")]')

        # Текст о готовности заказа во всплывающем окне "Заказ"
    TEXT_ABOUT_READINESS_ORDER = (By.XPATH, '//div[2]/p[contains(@class,"undefined text")][1]')

        # Идентификатор заказа
    ORDER_ID = (By.XPATH, '//h2[contains(@class,"Modal_modal")]')

        # Значек загрузки в окне "Заказ"
    LOADING_ICON = (By.XPATH, '//div[contains(@class,"Modal_modal_opened")]')
