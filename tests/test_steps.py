import allure
from allure_commons.types import Severity
from selene import browser, by, have, be
from selene.support.shared.jquery_style import s

@allure.tag('Web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'astitova')
@allure.feature('Задачи в репозитории')
@allure.story(f'Авторизованный пользователь может создать задачу в репозитории')
@allure.link('https://github.com')
def test_dynamic_steps():
    with allure.step("Открываем главную страницу"):
        browser.open("https://github.com")

    with allure.step("Ищем репозиторий"):
        s(".header-search-button").click()
        s("#query-builder-test").send_keys("astitova/qa_guru_python_19_9").submit()

    with allure.step("Переходим по ссылке репозитория"):
        s(by.link_text("astitova/qa_guru_python_19_9")).click()

    with allure.step("Открываем таб Issues"):
        s("#issues-tab").click()

    with allure.step("Проверяем наличие Issue с заголовком 'test issue'"):
        s(by.css("[data-testid='issue-pr-title-link']")).should(have.exact_text("test issue"))










