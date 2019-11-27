import unittest
import time
from selenium import webdriver


class editServiceTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_edit_service(self):
        user = "instructor"
        pwd = "maverick1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/accounts/login/")
        time.sleep(1)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        # Click Login button
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/input[2]").click()
        assert "Logged in"
        time.sleep(1)
        # Click View details under Service
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div/div/div[2]/div/div/p[2]/a").click()
        time.sleep(2)
        # Click Edit Service button
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[5]/td[8]/a").click()
        time.sleep(2)
        elem = driver.find_element_by_id("id_location")
        elem.clear()
        elem.send_keys("PKI Room 271")
        time.sleep(1)
        elem = driver.find_element_by_id("id_service_charge")
        elem.clear()
        elem.send_keys("270")

        # Click Update
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()
        time.sleep(2)
        assert "Updated Service successfully"


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()