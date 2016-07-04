import os
from selenium import webdriver

ChromeDriver ='/Users/brahmanndak/Desktop/personalgit/python-learning/selenium/chromedriver'
os.environ["webdriver.chrome.driver"]=ChromeDriver
driver=webdriver.Chrome(ChromeDriver)
driver.get("http://www.google.com")
driver.close()

print driver.current_url+"this is pthon tutorial spource "       







# import os
# from selenium import webdriver
#
# chromedriver = "/Users/adam/Downloads/chromedriver"
# os.environ["webdriver.chrome.driver"] = chromedriver
# driver = webdriver.Chrome(chromedriver)
# driver.get("http://stackoverflow.com")
# driver.quit()
