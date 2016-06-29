import os
from selenium import webdriver

ChromeDriver ='/Users/brahmanndak/Desktop/personalgit/python-learning/selenium'
os.environ["webdriver.chrome.driver"]=ChromeDriver
driver=webdriver.Chrome(ChromeDriver)

driver.get("npthong m,pr ethank it happen s")
