import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep

#Fixture for Firefox
@pytest.fixture(scope="class")
def driver_init(request):
    driver_path = '../gpu-scraper/drivers/geckodriver'
    option = Options()
    option.binary_location = '/usr/lib/firefox/firefox'
    ff_driver = webdriver.Firefox(firefox_options = option, executable_path = driver_path)
    #ff_driver = webdriver.Firefox()
    request.cls.driver = ff_driver
    yield
    ff_driver.close()

@pytest.mark.usefixtures("driver_init")
class BasicTest:
    pass
class Test_URL(BasicTest):
        def test_open_url(self):
            self.driver.get("https://www.lambdatest.com/")
            print(self.driver.title)

            sleep(5)

