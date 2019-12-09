
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.request import urlopen
from tabulate import tabulate
from selenium.webdriver.support.ui import Select
import unittest
import time


class TestForm(unittest.TestCase):



    def test_driver(self):
     

        self.browser = webdriver.Firefox( executable_path=r'..\driver\geckodriver.exe')
        self.browser.maximize_window()
        
        self.browser.get('http://localhost:8080')
        self.browser.execute_script("navigator.geolocation.getCurrentPosition = function(success) { success({coords: {latitude: 44.566818,  longitude: -123.279352}}); }")
        print("Unit Test - 1")
        self.assertEqual(self.browser.title, "Vue App")

    def test_navigation(self):
        self.browser = webdriver.Firefox( executable_path=r'..\driver\geckodriver.exe')
        self.browser.maximize_window()
        
        self.browser.get('http://localhost:8080')
        login=self.browser.find_element_by_link_text('Login')
        login.click()
        print("Unit Test -2")
        print(self.browser.current_url)
        self.assertEqual(self.browser.current_url,"http://localhost:8080/#/dashboard")

    def test_formvalidation(self):
        self.browser = webdriver.Firefox( executable_path=r'..\driver\geckodriver.exe')
        self.browser.maximize_window()
        
        self.browser.get('http://localhost:8080/#/eventform')

        eventTitle= self.browser.find_element_by_xpath('//*[@id="EventName"]')
        eventTitle.send_keys("Software Engineering Class")

        submit = self.browser.find_element_by_xpath('//*[@id="content"]/div/div/form/div[6]/button')
        submit.click()
        print("Unit Test -3")
        display_msg = self.browser.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div/div/div/div')
        self.assertEqual("The event has been saved.", display_msg.text)  

    def test_unknownpage(self):
        self.browser = webdriver.Firefox( executable_path=r'..\driver\geckodriver.exe')
        self.browser.maximize_window()
        
        self.browser.get('http://localhost:8080/#/badpage')
        display_msg = self.browser.find_element_by_xpath('//*[@id="app"]/div[2]/h1')
        self.assertEqual("Page not found.",display_msg.text)


    def tearDown(self):
        self.browser.quit()
        


if __name__=="__main__":
    # checker = FormTest()
    # checker.setup_drivers()
    # checker.navigate()
    # checker.single_unit()
    unittest.main(verbosity=2)
    

    print("\n")
    


