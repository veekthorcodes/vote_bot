""" ---------- REQUIREMENTS ----------

1 pip install selenium
2 dowload the chrome webdriver for the operating system 
  AND THE VERSION OF GOOGLE CHROME you are using with this link 
  https://sites.google.com/chromium.org/driver/
  it should be a zip file, just unzip it and replace the chromedriver folder in this directory with the one you downloaded.

"""

from selenium.webdriver.common.by import By
from selenium import webdriver
import warnings
import time
warnings.filterwarnings("ignore")  # ignore warnings

PATH = "chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(PATH)

SITE_OLD = "https://docs.google.com/forms/d/e/1FAIpQLSf8iqzLxBVQHzHeW15bmb2sbxaO4W6Qkbo2-wknTzWo92Re-Q/viewform"
SITE = "https://docs.google.com/forms/d/e/1FAIpQLSe3YI_5g4_KsLeMlyEjZN1hv194afpWtBDUNzhSbnep13F-rg/viewform?usp=pp_url&entry.1258404478=Option+1"
EMAIL = "veekthorcodes1@gmail.com"

contestants_map = {
    # "INIYE": "//div[@id='i18']",
    # "MR. KINGZO": "//div[@id='i42']",
    # "MR. LEGEND": "//div[@id='i58']",
    "JOKER": "//div[@id='i18']",
}
number_of_votes = 3000 # change number_of_votes to the number of iterations you want the script to run for

for n in range(number_of_votes):
    print(f"* vote number [{n + 1}] out of [{number_of_votes}] estimated votes *\n")
    print("Getting Site...")
    driver.get(SITE)

    print("Entering Email...\n")
    driver.find_element(By.XPATH, "//input[@type='email']").send_keys(EMAIL) 


    for contestant, xpath in contestants_map.items():
        print(f"Finding {contestant}...")
        el = driver.find_element(By.XPATH, xpath)
        if el.get_attribute(name="aria-checked") == "false":
            el.click()
            print(f"voted for {contestant}.\n")
        else:
            print(
                f"{contestant} already has not been voted for, not found, or something went wrong")

    # submit the form
    driver.find_element(By.XPATH, "//div[@class='uArJ5e UQuaGc Y5sE8d VkkpIf QvWxOd']").click()
    print("vvv SUBMITTED vvv.\n\n")
    # time.sleep(3)

driver.quit()

# to run the script in the terminal, type: python3 season_2.py