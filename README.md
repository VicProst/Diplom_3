## Дипломный проект. Задание 3: Тестирование UI

### Автотесты для проверки UI сервиса Stellar Burgers

### Структура проекта

- `locators` - пакет, содержащий локаторы страниц веб-приложения
- `pages` - пакет, содержащий методы страниц веб-приложения
- `tests` - пакет, содержащий тесты страниц веб-приложения
- `conftest.py` - фикстуры для тестов
- `data.py` - константы и данные для тестов
- `generator.py` - генератор создания нового пользователя
- `allure_results` - пакет, содержащий json-файлы для Allure-отчета

### Реализованные сценарии

Созданы UI-тесты, покрывающие сценарии: `Восстановление пароля`, `Личный кабинет`, `Проверка основного функционала`,
`Раздел «Лента заказов»`

### TestStellarBurgersAccountPage:

- `test_account_auth_user_click_personal_account_button_account_page_will_open` - Проверка перехода на страницу личного кабинета по кнопке "Личный кабинет"
- `test_account_click_order_history_button_chapter_order_history_will_open` - Проверка перехода в раздел "История заказов" по кнопке "История заказов"
- `test_account_click_exit_button_login_page_will_open` - Проверка выхода из аккаунта по кнопке "Выход"

### TestStellarBurgersForgotPasswordPage:

- `test_password_recovery_click_restore_password_button_password_recovery_page_will_open` - Проверка перехода на страницу восстановления пароля по кнопке "Восстановить пароль"
- `test_password_recovery_valid_email_click_restore_button_reset_password_page_will_open` - Проверка перехода на страницу сброса пароля по кнопке "Восстановить"
- `test_password_recovery_click_show_hide_button_password_field_is_active` - Проверка активации поля "Пароль" по кнопке "показать/скрыть"

### TestStellarBurgersMainPage:

- `test_constructor_click_constructor_button_header_construct_burger_will_open` - Проверка перехода на главную страницу по кнопке "Конструктор"
- `test_constructor_click_ingredient_header_ingredient_details_will_open` - Проверка появления всплывающего окна с деталями, если кликнуть на ингредиент
- `test_constructor_click_cross_mark_button_header_ingredient_details_is_none` - Проверка закрытия всплывающего окна с деталями, если кликнуть на крестик
- `test_constructor_add_ingredient_to_order_counter_increasing` - Проверка увеличения каунтера определенного ингредиента, если добавить его в заказ
- `test_constructor_auth_user_added_ingredient_text_about_readiness_will_open` - Проверка оформления заказа залогиненным пользователем

### TestStellarBurgersOrderFeedPage:

- `test_order_feed_click_order_feed_button_order_feed_page_will_open` - Проверка перехода на страницу "Лента заказов" по кнопке "Лента заказов"
- `test_order_feed_click_order_header_composition_will_open` - Проверка открытия всплывающего окна с деталями заказа, если кликнуть на заказ
- `test_order_feed_auth_user_create_order_order_id_visible_in_order_card_number` - Проверка отображения заказов на странице "Лента заказов" из раздела "История заказов"
- `test_order_feed_auth_user_create_order_all_time_counter_number_increasing` - Проверка увеличения числа в счётчике "Выполнено за всё время", после создания нового заказа
- `test_order_feed_auth_user_create_order_for_today_counter_number_increasing` - Проверка увеличения числа в счётчике "Выполнено за сегодня", после создания нового заказа
- `test_order_feed_auth_user_create_order_order_id_visible_in_in_progress_field` - Проверка появления номера заказа в разделе "В работе", после оформления заказа

### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск автотестов**

>  `$ pytest -v tests/`

**Генерация Allure-отчета**

>  `$ pytest tests/ --alluredir=allure_results`

**Создание HTML-отчета**

>  `$ allure serve allure_results`