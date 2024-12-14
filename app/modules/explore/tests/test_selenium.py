import time

from selenium.common.exceptions import NoSuchElementException  # type: ignore
from selenium.webdriver.common.by import By  # type: ignore
from selenium.webdriver.common.keys import Keys  # type: ignore

from core.environment.host import get_host_for_selenium_testing
from core.selenium.common import close_driver, initialize_driver_firefox


def test_features_with_value():

    driver = initialize_driver_firefox()

    try:
        host = get_host_for_selenium_testing()

        # Open the login page
        driver.get(f'{host}/explore')
        # Wait a little while to make sure the page has loaded completely
        time.sleep(4)
        # Find the features field and enter the values
        features_field = driver.find_element(By.NAME, 'core_features')
        features_field.clear()
        features_field.send_keys('4')
        # Send the form
        features_field.send_keys(Keys.RETURN)
        # Wait a little while to ensure that the action has been completed
        time.sleep(4)

        try:

            driver.find_element(By.XPATH, "//h3[contains(@class, 'h3 mb-3') and contains(., '0 datasets found')]")
            print('Test passed!')

        except NoSuchElementException:
            raise AssertionError('Test failed!')

    finally:

        # Close the browser
        close_driver(driver)


def test_features_with_empty():

    driver = initialize_driver_firefox()

    try:
        host = get_host_for_selenium_testing()

        # Open the login page
        driver.get(f'{host}/explore')
        # Wait a little while to make sure the page has loaded completely
        time.sleep(4)
        # Find the features field and enter the values
        features_field = driver.find_element(By.NAME, 'core_features')
        features_field.clear()
        features_field.send_keys('')
        # Send the form
        features_field.send_keys(Keys.RETURN)
        # Wait a little while to ensure that the action has been completed
        time.sleep(4)

        try:

            driver.find_element(By.XPATH, "//h3[contains(@class, 'h3 mb-3') and contains(., '4 datasets found')]")
            print('Test passed!')

        except NoSuchElementException:
            raise AssertionError('Test failed!')

    finally:

        # Close the browser
        close_driver(driver)


# Call the test functions

test_features_with_value()
test_features_with_empty()
