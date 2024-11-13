# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestTestfiltrosfinal():

  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_testfiltrosfinal(self):
    self.driver.get("http://localhost:5000/")
    self.driver.set_window_size(1920, 1043)
    self.driver.find_element(By.CSS_SELECTOR, ".sidebar-item:nth-child(3) .align-middle:nth-child(2)").click()
    dropdown = self.driver.find_element(By.ID, "publication_type")
    dropdown.find_element(By.XPATH, "//option[. = 'None']").click()
    element = self.driver.find_element(By.ID, "publication_type")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.ID, "publication_type")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.ID, "publication_type")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    dropdown = self.driver.find_element(By.ID, "publication_type")
    dropdown.find_element(By.XPATH, "//option[. = 'Data Management Plan']").click()
    element = self.driver.find_element(By.ID, "publication_type")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.ID, "publication_type")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.ID, "publication_type")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.ID, "model_count").click()
    self.driver.find_element(By.ID, "model_count").send_keys("1")
    self.driver.find_element(By.ID, "model_count").send_keys(Keys.ENTER)
    self.driver.find_element(By.ID, "model_count").click()
    self.driver.find_element(By.ID, "model_count").send_keys("4")
    self.driver.find_element(By.ID, "model_count").send_keys(Keys.ENTER)
    self.driver.find_element(By.ID, "model_count").send_keys(Keys.ENTER)
    self.driver.find_element(By.ID, "model_count").send_keys("0")
    self.driver.find_element(By.CSS_SELECTOR, ".col-12 > .row:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".form-check:nth-child(2) > .form-check-input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".form-check:nth-child(3) > .form-check-input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".form-check:nth-child(4) > .form-check-input").click()
    element = self.driver.find_element(By.ID, "size_limit")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.ID, "size_limit")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.ID, "size_limit")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.ID, "size_limit").send_keys("3440")
    self.driver.find_element(By.ID, "size_limit").click()
    element = self.driver.find_element(By.ID, "size_limit")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.ID, "size_limit")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.ID, "size_limit")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.ID, "size_limit").send_keys("0")
    self.driver.find_element(By.ID, "size_limit").click()
    element = self.driver.find_element(By.ID, "size_limit")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.ID, "size_limit")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.ID, "size_limit")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.ID, "size_limit").send_keys("10000")
    self.driver.find_element(By.ID, "size_limit").click()
    dropdown = self.driver.find_element(By.ID, "publication_type")
    dropdown.find_element(By.XPATH, "//option[. = 'Annotation Collection']").click()
    element = self.driver.find_element(By.ID, "publication_type")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.ID, "publication_type")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.ID, "publication_type")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.ID, "clear-filters").click()
    self.driver.find_element(By.LINK_TEXT, "Explore").click()
    dropdown = self.driver.find_element(By.ID, "publication_type")
    dropdown.find_element(By.XPATH, "//option[. = 'Book Section']").click()
    element = self.driver.find_element(By.ID, "publication_type")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.ID, "publication_type")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.ID, "publication_type")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    dropdown = self.driver.find_element(By.ID, "publication_type")
    dropdown.find_element(By.XPATH, "//option[. = 'Data Management Plan']").click()
    element = self.driver.find_element(By.ID, "publication_type")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.ID, "publication_type")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.ID, "publication_type")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.ID, "model_count").click()
    self.driver.find_element(By.ID, "model_count").send_keys("02")
    self.driver.find_element(By.ID, "model_count").send_keys(Keys.ENTER)
    self.driver.find_element(By.CSS_SELECTOR, ".col-12 > .row:nth-child(3) > .col-12").click()
    self.driver.find_element(By.ID, "clear-filters").click()
    element = self.driver.find_element(By.ID, "size_limit")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.ID, "size_limit")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.ID, "size_limit")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.ID, "size_limit").send_keys("0")
    self.driver.find_element(By.ID, "size_limit").click()
    self.driver.find_element(By.ID, "clear-filters").click()
    self.driver.find_element(By.CSS_SELECTOR, ".col-12 > .row:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".form-check:nth-child(2) > .form-check-input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".form-check:nth-child(3) > .form-check-input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".form-check:nth-child(4) > .form-check-input").click()
    self.driver.find_element(By.ID, "clear-filters").click()
  