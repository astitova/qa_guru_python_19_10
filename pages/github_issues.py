import allure
from selene import browser, by, have
from selene.support.shared.jquery_style import s

class Issue():
    @allure.step("Открываем главную страницу")
    def open_main_page(self):
        browser.open("https://github.com")

    @allure.step("Ищем репозиторий {repo}")
    def search_for_repository(self, repo):
        s(".header-search-button").click()
        s("#query-builder-test").send_keys(repo).submit()

    @allure.step("Переходим по ссылке репозитория {repo}")
    def go_to_repository(self,repo):
        s(by.link_text(repo)).click()

    @allure.step("Открываем таб Issues")
    def open_issue_tab(self):
        s("#issues-tab").click()

    @allure.step("Проверяем наличие issue с заголовком {title}")
    def should_see_issue_with_title(self, title):
        s(by.css("[data-testid='issue-pr-title-link']")).should(have.exact_text(title))







