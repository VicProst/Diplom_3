from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:

        # Поле "email"
    EMAIL_FIELD = (By.XPATH, '//input[contains(@class,"text input__textfield")]')

        # Кнопка "Восстановить"
    RESTORE_BUTTON = (By.XPATH, '//button[contains(@class,"button_button")]')

        # Кнопка "Войти"
    ENTER_BUTTON_PASSWORD_RECOVERY_SCREEN = (By.XPATH, '//p/a[@class="Auth_link__1fOlj"]')
