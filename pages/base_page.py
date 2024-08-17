import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains


class StellarBurgersBasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Перейти на сайт {base_url}')
    def go_to_site(self, base_url):
        return self.driver.get(base_url)

    @allure.step('Ожидание загрузки {locator}')
    def find_element_located(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator),
                                                      message=f'Not found {locator}')

    @allure.step('Ожидание загрузки всех {locator}')
    def find_all_elements_located(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_all_elements_located(locator),
                                                      message=f'Not found {locator}')

    @allure.step('Ожидание кликабельности {locator}')
    def find_element_to_be_clickable(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator),
                                                      message=f'Not found {locator}')

    @allure.step('Ожидание пока текст {locator} будет отличаться от {text}')
    def wait_for_changed_text(self, locator, text, time=10):
        return WebDriverWait(self.driver, time).until(EC.none_of(EC.text_to_be_present_in_element(locator, text)))

    @allure.step('Ожидание пока текст {locator} будет отличаться от {text}')
    def text_to_be_present_in_element_attribute(self, element, attribute, text, time=10):
        WebDriverWait(self.driver, time).until(EC.text_to_be_present_in_element_attribute(element, attribute, text))

    @allure.step('Ожидание пока {locator} исчезнет')
    def wait_for_element_go_away(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.none_of(EC.visibility_of_element_located(locator)))

    @allure.step('Вывести адрес текущей страницы')
    def check_url(self):
        current_url = self.driver.current_url
        return current_url

    @allure.step('Ожидание появления {url} в адресной строке')
    def wait_url_contains(self, url, time=10):
        WebDriverWait(self.driver, time).until(EC.url_contains(url))

    @allure.step('Вывести адрес ссылки по которой перейдешь по клику на {locator}')
    def check_site_link(self, locator):
        address = self.driver.find_element(*locator).get_attribute('href')
        return address

    @allure.step('Сменить окно браузера')
    def switch_to_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Пролистать до {locator}')
    def scroll_to_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    @allure.step('Кликнуть по {locator}')
    def click_to_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Ввести текст в {locator}')
    def enter_text_in_element(self, locator, text):
        return self.driver.find_element(*locator).send_keys(text)

    @allure.step('Вывести текст из {locator}')
    def get_text_from_element(self, locator):
        return self.driver.find_element(*locator).text


    @allure.step('Вывести текст атрибута {attribute} из {locator}')
    def get_attribute_from_element(self, locator, attribute):
        return self.driver.find_element(*locator).get_attribute(attribute)

    @allure.step('Найти {locator}')
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Переместить из {source} в {target}')
    def drag_and_drop_element(self, source, target):
        action = ActionChains(self.driver)
        action.drag_and_drop(source, target).perform()
