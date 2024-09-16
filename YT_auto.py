from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class YouTubeAutomation:
    def __init__(self):
        # Initialize WebDriver based on the browser choice
        
        self.driver = webdriver.Chrome()
        
        self.driver.maximize_window()

    def open_youtube(self):
        """Open YouTube in the browser."""
        self.driver.get("https://www.youtube.com")
        time.sleep(2)  # Wait for the page to load

    def search_video(self, search_term):
        """Search for a video on YouTube."""
        search_box = self.driver.find_element(By.NAME, "search_query")
        search_box.send_keys(search_term)
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)  # Wait for search results to load

    def click_first_video(self):
        """Click on the first video from the search results."""
        first_video = self.driver.find_element(By.XPATH, '(//a[@id="video-title"])[1]')
        first_video.click()
        time.sleep(5)  # Wait for the video to start playing

    def close_browser(self):
        """Close the browser."""
        self.driver.quit()

# if __name__ == "__main__":
#     # Example usage of YouTubeAutomation class
#     #DRIVER_PATH = 'path_to_your_chromedriver_or_geckodriver'
    
#     # Initialize the YouTubeAutomation object
#     yt_bot = YouTubeAutomation()

#     # Perform automation tasks
#     yt_bot.open_youtube()
#     yt_bot.search_video("Selenium Python Tutorial")
#     yt_bot.click_first_video()

#     # Close the browser
#     yt_bot.close_browser()