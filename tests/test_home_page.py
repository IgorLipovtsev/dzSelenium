import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

from locators import HomePage, Footer, TopMenu



def test_home_page(url_setup, browser):
    """проверяем локаторы """

    actions = ActionChains(browser)


    browser.get(url_setup)
    # browser.find_element(*TopMenu.desktops).click()
    # browser.find_element(*TopMenu.pc).click()


    # el1 = browser.find_element(*TopMenu.mp3_players)
    # el2 = browser.find_element(*TopMenu.mp3_players).find_element(*TopMenu.mp3_4_9)
    # actions.move_to_element(el1)\
    #     .move_to_element(el2)\
    #     .perform()
    # el2.click()

    browser.find_element(*TopMenu.tablets).click()


    time.sleep(5)