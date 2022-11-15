from selenium import webdriver
import time

import warnings
warnings.filterwarnings('ignore')

path = 'chromedriver_linux64/chromedriver'

driver = webdriver.Chrome(path)

n = 100000

for _ in range(n):
  print(f"Entry {_+1} out of {n}\n")
  print("<:::::::::: GETTING WEBSITE ::::::::::>\n")
  driver.get("https://bmaaofficial.com/2021-voting/")
  
  next_rated_act = driver.find_element_by_css_selector("input[id='PDI_answer50423881']")
  print("Getting next rated act button...")
  next_rated_act.click()
  print("next rated act button clicked.")
  driver.find_element_by_css_selector("a[id='pd-vote-button10965513']").click()
  print("voted!\n")
  # time.sleep(2)

  # time.sleep(1)
  best_female_act = driver.find_element_by_css_selector("input[id='PDI_answer50423812']")
  print("Getting best female act button...")
  best_female_act.click()
  print("best female act button clicked.")
  driver.find_element_by_css_selector("a[id='pd-vote-button10965502']").click()
  print("voted!\n")
  # time.sleep(2)

  # time.sleep(1)
  best_ep = driver.find_element_by_css_selector("input[id='PDI_answer50423697']")
  print("Getting best ep button...")
  best_ep.click()
  print("best ep button clicked.")
  driver.find_element_by_css_selector("a[id='pd-vote-button10965475']").click()
  print("voted!\n")
  # time.sleep(2)
  
driver.quit()