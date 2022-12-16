import allure
from selene import browser
from selene.support import by
from selene.support.conditions import be


def test_github():
    browser.open_url("https://github.com")

    browser.element(".header-search-wrapper").click()
    browser.element(".header-search-wrapper").send_keys("eroshenkoam/allure-example")
    browser.element(".header-search-wrapper").submit()

    browser.element(by.link_text("eroshenkoam/allure-example")).click()

    browser.element("#issues-tab").click()

    browser.element(by.partial_text("#76")).should(be.visible)
