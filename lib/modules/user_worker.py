class UserWorker:
    config = None
    
    def __init__(self, config):
        self.config = config
        

    def login(self, url):
        # if driver is already initialized, skip this part
        if AppState.web_driver is None:
            AppState.web_driver = webdriver.ChromeOptions() 
            AppState.web_driver.headless = True
            AppState.web_driver.add_argument('--headless=new')
            image_preferences = {"profile.managed_default_content_settings.images": 2}
            AppState.web_driver.add_experimental_option("prefs", image_preferences)
            AppState.web_driver.add_argument('--blink-settings=imagesEnabled=false')
            self.driver = webdriver.Chrome(service=ChromeService( 
                ChromeDriverManager().install()), options=AppState.web_driver)
        self.driver.get(url)
