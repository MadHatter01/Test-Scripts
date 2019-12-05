
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.request import urlopen
from tabulate import tabulate
from selenium.webdriver.support.ui import Select
import unittest
import time


class FormTest(unittest.TestCase):


    def setup_drivers(self):
     
        # DesiredCapabilities capabilities = DesiredCapabilities.firefox();
        # capabilities.setCapability(FirefoxDriver.PROFILE, geoDisabled);
        
        self.browser = webdriver.Firefox( executable_path=r'..\driver\geckodriver.exe')
        self.browser.maximize_window()
        
        self.browser.get('http://localhost:8080')
        self.browser.execute_script("navigator.geolocation.getCurrentPosition = function(success) { success({coords: {latitude: 44.566818,  longitude: -123.279352}}); }")

    def navigate(self):
        login=self.browser.find_element_by_link_text('Login')
        login.click()
        self.browser.find_element_by_xpath('/html/body/div/div/div[1]/div[1]/ul/li[5]/a').click()

    def single_unit(self):
        eventTitle= self.browser.find_element_by_xpath('//*[@id="EventName"]')
        eventTitle.send_keys("Software Engineering Class")

        submit = self.browser.find_element_by_xpath('//*[@id="content"]/div/div[2]/form/div[6]/button')
        submit.click()

        display_msg = self.browser.find_element_by_xpath('//*[@id="content"]/div/div[2]/div')
        assert "The event has been saved" in display_msg.text

    def tearDown(self):
        self.browser.quit()


if __name__=="__main__":
    checker = FormTest();

    # checker.setup_drivers()
    # checker.navigate()
    # checker.single_unit()
    unittest.main()
    

    print("\n")
    


