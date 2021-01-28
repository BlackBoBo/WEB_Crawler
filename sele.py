from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time



driver = webdriver.Chrome()
driver.get('https://www.boannews.com/media/t_list.asp')
time.sleep(1)
driver.find_element_by_class_name('news_txt').click()
print(driver.current_url)