import allure
from selene import browser
from selene.support import by
from selene.support.conditions import be


def test_dynamic_steps():  # с помощью with
    with allure.step("Открываем главную страницу"):
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



