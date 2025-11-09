import pytest
from utils.driver_factory import create_driver
from utils.constants import BASE_URL


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser = request.param
    driver =create_driver(browser)
    driver.get(BASE_URL)
    yield driver
    driver.quit()