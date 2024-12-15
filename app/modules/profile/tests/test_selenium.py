import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from core.environment.host import get_host_for_selenium_testing
from core.selenium.common import close_driver, initialize_driver_firefox


def login_user(driver, host):
    """Helper function to login a user"""
    driver.get(f'{host}/login')
    time.sleep(4)

    email_field = driver.find_element(By.NAME, 'email')
    password_field = driver.find_element(By.NAME, 'password')

    email_field.send_keys('user1@example.com')
    password_field.send_keys('1234')
    password_field.send_keys(Keys.RETURN)
    time.sleep(4)


def test_access_profile_summary():
    driver = initialize_driver_firefox()

    try:
        host = get_host_for_selenium_testing()
        login_user(driver, host)

        # Navigate to profile summary
        driver.get(f'{host}/profile/summary')
        time.sleep(4)

        try:
            # Verify access to profile summary page
            driver.find_element(By.XPATH, "//h1[contains(., 'User profile')]")
            print('Profile summary access test passed!')
        except NoSuchElementException:
            raise AssertionError('Profile summary access test failed!')

    finally:
        close_driver(driver)


def test_edit_profile_form():
    driver = initialize_driver_firefox()

    try:
        host = get_host_for_selenium_testing()
        login_user(driver, host)

        # Navigate to profile edit page
        driver.get(f'{host}/profile/edit')
        time.sleep(4)

        # Find and fill form fields
        name_field = driver.find_element(By.NAME, 'name')
        surname_field = driver.find_element(By.NAME, 'surname')
        orcid_field = driver.find_element(By.NAME, 'orcid')
        affiliation_field = driver.find_element(By.NAME, 'affiliation')

        # Clear existing values
        name_field.clear()
        surname_field.clear()
        orcid_field.clear()
        affiliation_field.clear()

        # Input new values
        name_field.send_keys('John')
        surname_field.send_keys('Doe')
        orcid_field.send_keys('0000-0002-1825-0097')
        affiliation_field.send_keys('Test University')

        # Click submit button
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        time.sleep(4)

        # Verify success message
        assert driver.find_element(By.CLASS_NAME, "alert-success"), "Profile update should show success message"

    finally:
        close_driver(driver)


def test_required_fields_validation():
    driver = initialize_driver_firefox()

    try:
        host = get_host_for_selenium_testing()
        login_user(driver, host)

        driver.get(f'{host}/profile/edit')
        time.sleep(4)

        # Find form fields
        name_field = driver.find_element(By.NAME, 'name')
        surname_field = driver.find_element(By.NAME, 'surname')

        # Clear fields and submit empty form
        name_field.clear()
        surname_field.clear()
        surname_field.send_keys(Keys.RETURN)

        time.sleep(2)

        # Verify validation errors
        try:
            error_messages = driver.find_elements(By.CLASS_NAME, 'alert-error')
            assert len(error_messages) > 0, "Validation errors should appear for empty required fields"
            print('Required fields validation test passed!')
        except NoSuchElementException:
            raise AssertionError('Required fields validation test failed - no error messages found')

    finally:
        close_driver(driver)


def test_invalid_orcid_format():
    driver = initialize_driver_firefox()

    try:
        host = get_host_for_selenium_testing()
        login_user(driver, host)

        driver.get(f'{host}/profile/edit')
        time.sleep(4)

        orcid_field = driver.find_element(By.NAME, 'orcid')
        orcid_field.clear()
        orcid_field.send_keys('invalid-orcid-format')
        orcid_field.send_keys(Keys.RETURN)

        time.sleep(2)

        # Verify ORCID validation error
        try:
            driver.find_element(By.XPATH, "//*[contains(text(), 'Invalid ORCID format')]")
            print('ORCID validation test passed!')
        except NoSuchElementException:
            raise AssertionError('ORCID validation test failed!')

    finally:
        close_driver(driver)


if __name__ == "__main__":
    test_access_profile_summary()
    test_edit_profile_form()
    test_required_fields_validation()
    test_invalid_orcid_format()
