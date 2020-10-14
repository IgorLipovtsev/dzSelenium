import time
from selenium.webdriver.common.action_chains import ActionChains

from resources.locators import TopMenu


def test_click_element(url_setup, browser):
    """проверяем локаторы """

    browser.get(url_setup)
    browser.find_element(*TopMenu.desktops_list).click()
    time.sleep(5)


def test_move_to_element(url_setup, browser):
    """проверяем локаторы """

    actions = ActionChains(browser)
    browser.get(url_setup)
    el1 = browser.find_element(*TopMenu.mp3_players_list)
    el2 = browser.find_element(*TopMenu.mp3_players_list).find_element(*TopMenu.mp3_1_17)
    actions.move_to_element(el1) \
        .move_to_element(el2) \
        .perform()
    el2.click()
    time.sleep(5)
