import time as t
import unittest
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class robot_aparat(unittest.TestCase):
    def setUp(self):
        self.driver=Firefox(executable_path="./geckodriver")
        pass
    def test_robot(self):
        self.driver.get("https://www.aparat.com/login")
        print(self.driver.title)
        t.sleep(15)
        elem=self.driver.find_element(By.ID, "username")
        elem.clear()
        elem.send_keys("phone number")
        elem.send_keys(Keys.ENTER)
        t.sleep(15)
        elem1=self.driver.find_element(By.ID,"password")
        elem1.clear()
        elem1.send_keys("password")
        elem1.send_keys(Keys.ENTER)

        
        pass
    def tearDown(self):
        #self.driver.close()
        pass
    pass

if __name__ == "__main__":
    unittest.main()



