'''
Created on Feb 12, 2017

@author: Vaibhav
'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from Helper.xpathList import *
from Helper.credentials import *
import time
from _asyncio import Future
from _ctypes_test import func


class FutureFuel(unittest.TestCase):

    def setUp(self):
        chrome_path = r"C:\Users\Vaibhav\Downloads\sikuli\chromedriver_win32(1)\chromedriver.exe" #My path to chromedriver.exe
        self.driver = webdriver.Chrome(chrome_path)
        

    def test_Login_Page_Pass(self):
        print("test_Login_Page_Pass:Started")
        driver = self.driver
        driver.get("https://futurefuel.io/login")
        self.assertIn("FutureFuel - Log In", driver.title)
        driver.find_element_by_class_name("logo").is_displayed()
        driver.find_element_by_name("email").send_keys('patil.va@husky.neu.edu')
        driver.find_element_by_name("password").send_keys('football')    
        driver.find_element_by_css_selector("button.btn.btn-blue").click()
        time.sleep(5)
        profileName = driver.find_element_by_css_selector("h2.candidate-name").text
        assert profileName =="Vaibhav Patil"
        print("test_Login_Page_Pass:Completed ")   
        
        
    def test_Login_Page_Fail(self):
        print("test_Login_Page_Fail:Started")
        driver = self.driver
        driver.get("https://futurefuel.io/login")
        self.assertIn("FutureFuel - Log In", driver.title)
        driver.find_element_by_class_name("logo").is_displayed()
        driver.find_element_by_name("email").send_keys('patil.va@husky.neu.edu')
        driver.find_element_by_name("password").send_keys('football')    
        
        goButton = driver.find_element_by_css_selector("button.btn.btn-blue")
        goButton.click()
        
        profileName = driver.find_element_by_css_selector("h2.candidate-name").text
        assert profileName =="Vaibhav Patil"
                
        time.sleep(5)
        
        assert "No results found." not in driver.page_source


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()