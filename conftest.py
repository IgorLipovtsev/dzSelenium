import pytest
from selenium import webdriver


def pytest_addoption(parser):
    """добавляем параметры для командой строки"""

    parser.addoption(
        "--url",
        action="store",
        default="http://192.168.64.2",
        help="this is request url",
    )
    parser.addoption(
        "--browser", action="store", default="Chrome", help="this is browser"
    )
    parser.addoption(
        "--headless", action="store", default=False, help="headless mode for browser"
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

    if browser == "Chrome":
        if headless == False:
            driver = webdriver.Chrome()
            driver.maximize_window()
        else:
            options = webdriver.ChromeOptions()
            options.add_argument("--headless")
            driver = webdriver.Chrome(options=options)
            driver.maximize_window()

    elif browser == "Firefox":

        if headless == False:
            driver = webdriver.Firefox()
            driver.maximize_window()
        else:
            options = webdriver.FirefoxOptions()
            options.add_argument("--headless")
            driver = webdriver.Firefox(options=options)
            driver.maximize_window()

    elif browser == "Safari":
        driver = webdriver.Safari()
        driver.maximize_window()

    request.addfinalizer(driver.quit)
    return driver
