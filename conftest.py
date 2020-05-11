import pytest
from selenium import webdriver


def pytest_addoption(parser):
    """добавляем параметры для командой строки"""

    parser.addoption(
        "--url",
        action="store",
        default="http://192.168.64.2/",
        help="this is request url",
    )
    parser.addoption(
        "--browser", action="store", default="Chrome", help="this is browser"
    )
    parser.addoption(
        "--headless", action="store", default=False, help="headless mode for browser"
    )
    parser.addoption(
        "--wait", action="store", type="int", default=10, help="implicitly wait value for driver"
    )


@pytest.fixture()
def url_setup(request):
    """читаем url c командой строки"""

    return request.config.getoption("--url")


@pytest.fixture()
def browser(request):
    """настройка браузера"""

    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    implicitly_wait_value = request.config.getoption("--wait")

    if browser == "Chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--ignore-certificate-errors")

        if headless == False:
            driver = webdriver.Chrome(options=options)

        else:
            options.add_argument("--headless")
            driver = webdriver.Chrome(options=options)


    elif browser == "Firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--ignore-certificate-errors")

        if headless == False:
            driver = webdriver.Firefox(options=options)
        else:
            options = webdriver.FirefoxOptions()
            options.add_argument("--headless")
            driver = webdriver.Firefox(options=options)

    elif browser == "Safari":
        driver = webdriver.Safari()

    request.addfinalizer(driver.quit)

    driver.maximize_window()
    driver.implicitly_wait(implicitly_wait_value)

    return driver
