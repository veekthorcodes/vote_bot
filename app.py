""" ---------- DEPENDENCIES ----------

1 pip install selenium

2 dowload the chrome webdriver for the operating system 
  AND THE VERSION OF GOOGLE CHROME you are using with this link 
  https://sites.google.com/chromium.org/driver/

  it should be a zip file, just unzip it.

"""

from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import time

import warnings
warnings.filterwarnings("ignore")

# Change this PATH  variable to the relative path to where you have the extracted file from the chrome webdriver saved. In my case i saved the folder (chromedriver_linux64) in the same folder as i have app.py then inside the folder is the main chromedriver file.
PATH = "chromedriver_linux64/chromedriver"

driver = webdriver.Chrome(PATH)

# change n to the number of iterations you want the script to run for
n = 10000
site1 = "https://docs.google.com/forms/d/e/1FAIpQLSeGFt4pGHqHOYLEAJfii4JbYocUDP2k2znA7j5QMOErCU3yMw/viewform"

site2 = "https://docs.google.com/forms/d/e/1FAIpQLScXislPAGq__ra1ukydmqUuwcluo0spcIrk_eqvC3cLKRegBw/viewform"



for _ in range(n):
  print(f"Entry {_ + 1} out of {n}")
  print(":::::::::::::::::::: GETTING SITE ::::::::::::::::::::\n")



  driver.get(site2)

  el = driver.find_element_by_css_selector("div[id=i30]")
  if el.get_attribute("aria-checked") == "false":
    print("xxx BUTTON HAS NOT BEEN CLICKED xxx")
  # time.sleep(1)

  el.click()
  if el.get_attribute("aria-checked") == "true":
    print("vvv BUTTON HAS BEEN CLICKED vvv")
  # time.sleep(2)

  print("Submiting...")
  driver.find_element_by_css_selector("div [class='appsMaterialWizButtonPaperbuttonLabel quantumWizButtonPaperbuttonLabel exportLabel']").click()
  print("Submitted.\n\n")

driver.quit()