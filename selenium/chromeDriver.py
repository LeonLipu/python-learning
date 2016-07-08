import os
from selenium import webdriver

ChromeDriver ='/Users/brahmanndak/Desktop/personalgit/python-learning/selenium/chromedriver'
os.environ["webdriver.chrome.driver"]=ChromeDriver
driver=webdriver.Chrome(ChromeDriver)
driver.get("http://www.google.com")

print driver.current_url+"this is pthon tutorial spource "
print driver.execute_async_script("document.title"); # injecting javascript
driver.get_screenshot_as_png("base.png");
driver.close()








# import os
# from selenium import webdriver
#
# chromedriver = "/Users/adam/Downloads/chromedriver"
# os.environ["webdriver.chrome.driver"] = chromedriver
# driver = webdriver.Chrome(chromedriver)
# driver.get("http://stackoverflow.com")
# driver.quit()
