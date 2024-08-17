from selenium.webdriver.common.by import By


class ResetPasswordPageLocators:

        # Кнопка "показать/скрыть"
    SHOW_HIDE_BUTTON = (By.XPATH, '//div[@class="input__icon input__icon-action"]')

        # Границы поля "email"
    BOUNDARIES_EMAIL_FIELD = (By.XPATH, '//div[contains(@class,"input_type_text")]')

        # Плейсхолдер поля "email"
    PLACEHOLDER_EMAIL_FIELD = (By.XPATH, '//label[text()="Пароль"]')
