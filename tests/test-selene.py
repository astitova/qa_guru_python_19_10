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
def test_github_issue():
    browser.open("https://github.com")

    s(".header-search-button").click()
    s("#query-builder-test").send_keys("astitova/qa_guru_python_19_9").submit()

    s(by.link_text("astitova/qa_guru_python_19_9")).click()

    s("#issues-tab").click()
    s(by.css("[data-testid='issue-pr-title-link']")).should(have.exact_text("test issue"))










