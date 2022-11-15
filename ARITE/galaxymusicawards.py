from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import warnings
warnings.filterwarnings('ignore')

path = '../chromedriver_linux64/chromedriver'

driver = webdriver.Chrome(path)

n = 10000

url = 'https://galaxymusicawards.com/rookie-of-the-year/'

for _ in range(n):
    print(f"vote number {_+1} out of {n}")
    driver.get(url)
    arite = driver.find_element(By.CSS_SELECTOR, "input[id='answer[196]']")
    print("Clicking on Arite...")
    arite.click()
    time.sleep(1)
    print("Arite clicked.")
    print("Voting...")
    driver.find_element(By.CSS_SELECTOR, "div[class='basic-vote']").click()
    time.sleep(5)
    print("Voted!\n")

driver.quit()
