import allure
from allure_commons.types import Severity
from selene.support.shared import browser
from selene.support import by
from selene.support.conditions import be


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "vishnyakova")
@allure.feature("Задачи в репозитории")
@allure.story("Пример теста без шагов")
@allure.link("https://github.com", name="Testing")
def test_github():
    browser.config.driver.maximize_window()
    browser.open_url("https://github.com")

    browser.element(".header-search-wrapper").click()
    browser.element(".header-search-wrapper").send_keys("eroshenkoam/allure-example")
    browser.element(".header-search-wrapper").submit()

    browser.element(by.link_text("eroshenkoam/allure-example")).click()

    browser.element("#issues-tab").click()

    browser.element(by.partial_text("#76")).should(be.visible)

@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "vishnyakova")
@allure.feature("Задачи в репозитории")
@allure.story("Пример теста с лямбда шагами")
@allure.link("https://github.com", name="Testing")
def test_dynamic_steps():  # с помощью with
    with allure.step("Открываем главную страницу"):
        browser.config.driver.maximize_window()
        browser.open_url("https://github.com")

    with allure.step("Ищем репозиторий"):
        browser.element(".header-search-wrapper").click()
        browser.element(".header-search-wrapper").send_keys("eroshenkoam/allure-example")
        browser.element(".header-search-wrapper").submit()

    with allure.step("Переходим по ссылке репозитория"):
        browser.element(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step("Открываем таб Issues"):
        browser.element("#issues-tab").click()

    with allure.step("Проверяем наличие Issues с номером 76"):
        browser.element(by.partial_text("#76")).should(be.visible)

@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "vishnyakova")
@allure.feature("Задачи в репозитории")
@allure.story("Пример теста с декораторами")
@allure.link("https://github.com", name="Testing")
def test_decorator_steps(): # c помощью степ
    open_main_page()
    search_for_repository("eroshenkoam/allure-example")
    go_to_repository("eroshenkoam/allure-example")
    open_issue_tab()
    should_see_issue_with_number("#76")


@allure.step("Открываем главную страницу")
def open_main_page():
    browser.config.driver.maximize_window()
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

