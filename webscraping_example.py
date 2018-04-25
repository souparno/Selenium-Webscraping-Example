from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# Specifying incognito mode as you launch your browser[OPTIONAL]
option = webdriver.ChromeOptions()

# Create new Instance of Chrome in incognito mode
browser = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', chrome_options=option)

# Go to desired website
browser.get("https://angel.co/bangalore")

# Wait 20 seconds for page to load
timeout = 20

page = 2;

# set the timeout for the ajax request or else you will get a TimeoutException
browser.set_script_timeout(timeout);

try:
    # Wait until the final element [Avatar link] is loaded.
    # Assumption: If Avatar link is loaded, the whole page would be relatively loaded because it is among
    # the last things to be loaded.
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'with_data')]")))
except TimeoutException:
    print("Timed out waiting for page to load")
    browser.quit()

while True :
    # read the script
    script = open('./javascript/inject.js', 'r').read() + ";initAjax(" + str(page) + ");"

    # execute the script
    browser.execute_script(script)
    page = page + 1
    time.sleep(3)

    if (len(browser.find_elements(By.XPATH, "//div[contains(@class, 'results_holder')]//div"))) == 1:
        break

browser.quit()

