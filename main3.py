import os
os.system("adb devices")
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_experimental_option("androidPackage", "org.chromium.chrome.stable")
driver = webdriver.Chrome(options=options)
driver.get("https://www.google.com")
print("Page title:", driver.title)
driver.quit()
