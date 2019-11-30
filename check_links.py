
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.request import urlopen
from tabulate import tabulate
import time
 
class Broken_parser():
    def __init__(self):
        self.url= ""

    def status_code(self,url):
        try:
            if(url):
                status_code = urlopen(url).getcode()
                print(tabulate([[url ,str(status_code)]], headers=['url','status_code']))
        except Exception as exception:
            print(exception);

class Sel_tester():
    all_urls=[]
    def __init__(self):
        pass

    def setup_drivers(self):
        self.browser = webdriver.Firefox(executable_path=r'..\driver\geckodriver.exe')
        self.browser.maximize_window()
        self.browser.get('http://localhost:8080')

    def dom_status(self):
        self.browser.execute_script("alert('Moving to next Page, DOM state is '+document.readyState)")

    
    def examine_page(self):    
        links = self.browser.find_elements_by_xpath("//a[@href]")
        for link in links:
            print(link.get_attribute('href'))
            href = link.get_attribute('href')
            self.all_urls.append(href)
            checker = Broken_parser()
            checker.status_code(href)

    def navigate_by_tag(self,tag):
        print(tag)
        target_link = self.browser.find_element_by_link_text(tag)
        target_link.click()

    def navigate_by_xpath(self, xpath, tag):
        print(tag)
        event_page = self.browser.find_element_by_xpath(xpath)
        event_page.click()
    
    def progress_link(self):
        self.browser.switch_to_alert().accept()
        # print(self.all_urls)

    def test_conclude(self):
        #save in a file
        self.browser.quit()

if __name__=="__main__":
    linker = Broken_parser();
    linker.status_code("http://localhost:8080")

    url = Sel_tester()
    url.setup_drivers()
    url.examine_page()
    print("\n")
    
    url.navigate_by_tag('Go to Map')
            
    # campus Map check
  
    # url.dom_status()
    url.examine_page()
    url.navigate_by_xpath('/html/body/div/div/div[1]/div[1]/ul/li[5]/a', 'Event Page')
    print("\n")

    #event Form check
    # url.dom_status()
    url.examine_page()

    url.test_conclude()
    




