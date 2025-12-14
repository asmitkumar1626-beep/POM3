from utilities.driver_setup import get_driver
import pytest


@pytest.fixture()
def driver():
    driver=get_driver()
    yield driver
    driver.quit()