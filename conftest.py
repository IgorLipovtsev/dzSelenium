import pytest
import logging
from fixtures.browser import Browser


def pytest_addoption(parser):
    """добавляем параметры для командой строки"""

    parser.addoption(
        "--url",
        action="store",
        default="http://192.168.64.2/",
        help="this is request url",
    )
    parser.addoption("--browser", action="store", default="chrome", help="This is request browser", required=False)
    parser.addoption("--implicitly_wait", action="store", default="10", help="waiting time in the seconds",
                     required=False)
    parser.addoption("--file", action='store', default=None, help='file with log report')
    parser.addoption(
        "--headless", action="store", default=False, help="headless mode for browser"
    )


@pytest.fixture()
def url_setup(request):
    """читаем url c командой строки"""

    return request.config.getoption("--url")


@pytest.fixture()
def driver(request):
    """Фикстура запуска различных браузеров"""
    active_browser = request.config.getoption("--browser")
    wait = request.config.getoption("--implicitly_wait")
    filename = request.config.getoption('--file')

    active_browser = Browser(browser=active_browser, wait=wait)
    logging.basicConfig(level=logging.INFO, filename=filename)
    active_browser.browser_log.info(f'{active_browser} is starting!')

    yield active_browser.driver
    active_browser.driver.quit()
    active_browser.browser_log.info(f'{active_browser} is stopping!')
