'''
Created on Feb 12, 2017

@author: Vaibhav
'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from Helper.xpathList import *
from Helper.credentials import *


class FutureFuel(unittest.TestCase):

    def setUp(self):
        chrome_path = r"C:\Users\Vaibhav\Downloads\sikuli\chromedriver_win32(1)\chromedriver.exe" #My path to chromedriver.exe
        self.driver = webdriver.Chrome(chrome_path)

    def test_Login_Page_Elements(self):
        driver = self.driver
        driver.get("https://futurefuel.io/login")
        self.assertIn("FutureFuel - Log In", driver.title)
#         elem = driver.find_element_by_name("q")
#         elem.send_keys("pycon")
#         elem.send_keys(Keys.RETURN)
#         assert "No results found." not in driver.page_source


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()