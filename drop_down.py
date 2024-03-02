import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/dropdown")

drop_down = driver.find_element(By.CSS_SELECTOR, "#dropdown").click()
drop_down.select_by_visible_text("Option 2")
time.sleep(3)
drop_down.select_by_index(1)
time.sleep(3)
drop_down.select_by_value('2')








