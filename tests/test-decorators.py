from allure_commons.types import Severity
from pages.github_issues import Issue
import allure

issue = Issue()
@allure.tag('Web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'astitova')
@allure.feature('Задачи в репозитории')
@allure.story(f'Авторизованный пользователь может создать задачу в репозитории')
@allure.link('https://github.com')
def test_decorator_steps():
    issue.open_main_page()
    issue.search_for_repository("astitova/qa_guru_python_19_9")
    issue.go_to_repository("astitova/qa_guru_python_19_9")
    issue.open_issue_tab()
    issue.should_see_issue_with_title("test issue")










