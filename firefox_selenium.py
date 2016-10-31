import time
from selenium import webdriver

driver =  webdriver.Firefox(executable_path="C:\Program Files (x86)\Mozilla Firefox\geckodriver.exe",
                            firefox_binary="C:\Program Files (x86)\Mozilla Firefox\Firefox.exe")

driver.get(url="http://www.google.com/")
#driver.get('http://www.google.com/');
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()