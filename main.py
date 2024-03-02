import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://automationintesting.online")

driver.find_element(By.CSS_SELECTOR, "#name").send_keys("Jonathan")

driver.find_elements(By.CSS_SELECTOR, ".form-control")[1].send_keys("test@email.com")

driver.find_element(By.CSS_SELECTOR, "input[data-testid='ContactPhone']").send_keys("093274689287")

driver.find_element(By.CSS_SELECTOR, 'form > div > input[aria-label="Subject"]').send_keys('Subject')

driver.find_element(By.CSS_SELECTOR, 'form textarea[data-testid="ContactDescription"]').send_keys('Description')

driver.find_element(By.CSS_SELECTOR, 'form > br + button').click()

time.sleep(2)





