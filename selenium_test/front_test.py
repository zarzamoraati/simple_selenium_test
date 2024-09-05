from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import pytest 

## TODO  SESSION
@pytest.fixture(scope="session")
def web_driver():
    return webdriver.Chrome()
## TODO BIND URI 
@pytest.fixture(scope="function")
def fetch_page(web_driver):
    url="http://localhost:5173/"
    web_driver.get(url)
    return web_driver
## TODO TEST CLASS

class TestFront:
    ## TODO testing home
    def test_home(self,fetch_page):
        ## TODO locator 
            ## TODO find by id
        btn_square=fetch_page.find_element(by=By.ID,value="btn-square-id")
            ## TODO find by classname

        ## TODO web element
            ## TODO methods
        assert btn_square.is_displayed()
        assert btn_square.is_enabled()
        assert not btn_square.is_selected()
        btn_name=btn_square.get_attribute("name")
        assert btn_name == "btn-square-element"
            ## TODO attributes
        btn_text=btn_square.text
        assert btn_text == "Show a square box"
                ## get text
        ## TODO perform Action
        btn_square.click()
        square_box=fetch_page.find_element(by=By.CLASS_NAME,value="div-square-class")
        
        ## TODO wait strategy 
        wait = WebDriverWait(fetch_page,timeout=5.0)
        wait.until(lambda x: square_box.is_displayed())
        ## TODO assertions
        square_text = square_box.text
        assert square_text == "Square Example"
        