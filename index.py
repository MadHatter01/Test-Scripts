
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


browser = webdriver.Firefox(executable_path=r'C:/Users/VaishuBox/Desktop/automation_test/driver/geckodriver.exe')

browser.get('http://localhost:8080')
browser.maximize_window()
browser.execute_script("alert('Landing Page successfully loaded. DOM state is '+document.readyState)")
# browser.execute_script("window.scrollBy({top: 1000,left: 0,behavior: 'smooth'});")

time.sleep(3)
browser.switch_to_alert().accept()
html=browser.find_element_by_tag_name('html')

html.send_keys(Keys.END)
time.sleep(1)
html.send_keys(Keys.PAGE_UP)

time.sleep(3)
browser.execute_script("alert('Moving to Map Page, DOM state is '+document.readyState)")
time.sleep(3)
browser.switch_to_alert().accept()

campus_map = browser.find_element_by_link_text('Go to Map')
campus_map.click()

time.sleep(3)
browser.execute_script("alert('Moving to Event Page, DOM state is '+document.readyState)")
time.sleep(3)
browser.switch_to_alert().accept()
event_page = browser.find_element_by_xpath('/html/body/div/div/div[1]/div[1]/ul/li[5]/a')
event_page.click()
time.sleep(3)
browser.execute_script("alert('End of Test')")
time.sleep(3)
browser.switch_to_alert().accept()

browser.close()

