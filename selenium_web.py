from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class Infow():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def get_info(self, query):
        self.query=query
        self.driver.get("https://www.wikipedia.org")


        search_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "searchInput"))
        )
        search_input.click()

        search_input.send_keys(self.query)
        sleep(2)

        search_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "pure-button"))
        )
        search_button.click()

        
        sleep(3)
        self.driver.quit()

# assist = Infow()
# assist.get_info("neutron stars")