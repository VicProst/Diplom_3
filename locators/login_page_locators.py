from selenium.webdriver.common.by import By


class LoginPageLocators:

        # Кнопка "Восстановить пароль"
    PASSWORD_RECOVERY_BUTTON = (By.XPATH, '//a[@href="/forgot-password"]')

        # Заголовок "Вход"
    HEADER_ENTER = (By.XPATH, '//h2[text()="Вход"]')

        # Поле "Email"
    EMAIL_FIELD = (By.XPATH, '//input[@name="name"]')

        # Поле "Пароль"
    PASSWORD_FIELD = (By.XPATH, '//input[@type="password"]')

        # Кнопка "Войти"
    ENTER_BUTTON = (By.XPATH, '//button[contains(@class,"button_button")]')

        # Кнопка "Зарегистрироваться"
    REGISTER_BUTTON = (By.XPATH, '//a[@class="Auth_link__1fOlj" and @href="/register"]')
