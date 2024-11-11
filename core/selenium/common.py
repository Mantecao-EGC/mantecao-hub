from selenium import webdriver
from selenium.webdriver.chrome.service import Service as SC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as SF
from webdriver_manager.firefox import GeckoDriverManager


def initialize_driver():
    # Initializes the browser options
    options = webdriver.ChromeOptions()

    # Initialise the browser using WebDriver Manager
    service = SC(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver


def initialize_driver_firefox():
    options = webdriver.FirefoxOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # Quitar "--headless" si quieres ver el navegador en modo visible
    # options.add_argument("--headless")  # Puedes quitar esto para modo visible

    # Iniciar el driver de Firefox usando webdriver-manager
    service = SF(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=options)
    return driver


def close_driver(driver):
    driver.quit()
