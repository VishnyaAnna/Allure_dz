import allure
from selene import browser
from selene.support import by


def test_decorator_steps(): # c помощью степ
    open_main_page()
    search_for_repository("eroshenkoam/allure-example")
    go_to_repository("eroshenkoam/allure-example")
    open_issue_tab()
    should_see_issue_with_number("#76")


@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open_url("https://github.com")


@allure.step("Ищем репозиторий {repo}")
def search_for_repository(repo):
    browser.element(".header-search-wrapper").click()
    browser.element(".header-search-wrapper").send_keys(repo)
    browser.element(".header-search-wrapper").submit()


@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
    browser.element(by.link_text(repo)).click()


@allure.step("Открываем таб Issues")
def open_issue_tab():
    browser.element("#issues-tab").click()


@allure.step("Проверяем наличие таб Issues с {number}")
def should_see_issue_with_number(number):
    browser.element(by.partial_text(number)).click()