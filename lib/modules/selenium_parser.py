from contextlib import nullcontext
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 
from app_state import AppState
import os

class SeleniumParser:

    def initialize_parser(self):
        # if driver is already initialized, skip this part
        if AppState.web_driver is None:
            AppState.web_driver = webdriver.ChromeOptions() 
            
            # uncomment this to make browser headless
            if(os.environ.get("RUN_BACKGROUND") == '1'):
                AppState.web_driver.headless = True
                AppState.web_driver.add_argument('--headless=new')
            #-------------------------
            
            image_preferences = {"profile.managed_default_content_settings.images": 2}
            AppState.web_driver.add_experimental_option("prefs", image_preferences)
            
            #this code will stop browser from closing
            if(os.environ.get("CLOSE_BROWSER_AFTER_RUNNING") == '0'):
                AppState.web_driver.add_experimental_option("detach", True)
            
            AppState.web_driver.add_argument('--blink-settings=imagesEnabled=false')
            
            #make page fullscreen
            AppState.web_driver.add_argument('--start-maximized')

            AppState.web_driver.add_argument('--blink-settings=imagesEnabled=false')
            AppState.web_driver = webdriver.Chrome(service=ChromeService( 
                ChromeDriverManager().install()), options=AppState.web_driver)

    def getLinks(self, target_selector) -> list[str]:
        result = []
        elements = AppState.web_driver.find_elements(By.CSS_SELECTOR, target_selector)
        
        for x in elements:
            link = x.get_attribute('href')
            app_url = os.environ.get("APP_URL").replace('http://', '').replace('https://', '')
            
            if app_url in link.replace('http://', '').replace('https://', '') and ('/logout' in link) == False:
                result.append(link)
                
        return result