from selenium import webdriver
import time

import warnings
warnings.filterwarnings('ignore')

path = 'chromedriver_linux64/chromedriver'

driver = webdriver.Chrome(path)

n = 100000

for _ in range(n):
  driver.get("https://bmaaofficial.com/2021-voting/")
  next_rated_act = driver.find_element_by_css_selector("input[id='PDI_answer50423881']")
  next_rated_act.click()
  driver.find_element_by_css_selector("a[id='pd-vote-button10965513']").click()
  time.sleep(2)

  time.sleep(1)
  best_female_act = driver.find_element_by_css_selector("input[id='PDI_answer50423812']")
  best_female_act.click()
  driver.find_element_by_css_selector("a[id='pd-vote-button10965502']").click()
  time.sleep(2)

  time.sleep(1)
  best_ep = driver.find_element_by_css_selector("input[id='PDI_answer50423697']")
  best_ep.click()
  driver.find_element_by_css_selector("a[id='pd-vote-button10965475']").click()
  time.sleep(2)
  
driver.quit()