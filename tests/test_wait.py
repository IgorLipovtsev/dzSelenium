import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



from locators import HomePage, Footer, TopMenu


def test_wait_for_element():
    """проверяем локаторы """
    # wait = WebDriverWait(browser, 10)

    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)  # seconds
    driver.get("https://www.google.com/")
    e = driver.find_element_by_name('q')
    e.send_keys(("Otus"))
    e.send_keys(Keys.ENTER)
    el = driver.find_element_by_id("center_col")
    # element = wait.until(lambda x: len(driver.find_elements_by_css_selector("center_col")) > 0)
    element = wait.until(EC.presence_of_element_located((By.ID, "center_col")))

def test_wait_for_element_is_gone():
    """проверяем локаторы """
    driver = webdriver.Chrome()
    # driver.implicitly_wait(10)
    driver.get("https://pagination.js.org/")
    wait = WebDriverWait(driver, 10)  # seconds
    demo1 = driver.find_element_by_id("demo1")
    items = demo1.find_elements_by_css_selector(".data-container ul li")
    print(items.pop(0).text)
    pagination = demo1.find_elements_by_css_selector(".paginationjs-pages ul li")
    pagination.pop(2).click()
    # wait.until(EC.staleness_of(items.pop(0)))
    items = demo1.find_elements_by_css_selector(".data-container ul li")
    print(items.pop(0).text)
    driver.quit()

def test_example():
    driver = webdriver.Chrome()
    driver.get("https://aliexpress.ru/home.htm")
    wait = WebDriverWait(driver, 10)
    try:
        el = driver.find_element_by_css_selector(".close-layer")
        el.click()
        wait.until(EC.staleness_of(el))
    finally:
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-role=join-link]")))
        search = driver.find_element_by_css_selector(".search-key")
        enter = driver.find_element_by_css_selector("span.join-btn > a")
        search.send_keys("Желтый человека нога")
        search.send_keys(Keys.ENTER)
        # wait.until(EC.staleness_of(enter))
        product_list = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'li.list-item')))
        current = driver.current_window_handle
        product_list.pop(0).click()
        all_windows = driver.window_handles
        for each in all_windows:
            if each != current:
                driver.switch_to.window(each)
                break
        country_list = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ul.sku-property-list")))
        china = country_list.pop(0)
        china.find_element_by_css_selector('.sku-property-text').click()
        cost = driver.find_element_by_css_selector("div.product-shipping-price > span")
        text = cost.text
        more = driver.find_element_by_css_selector("span.next-input-group-addon.next-after > button")
        more.click()
        driver.quit()