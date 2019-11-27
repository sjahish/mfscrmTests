import unittest
import time
from selenium import webdriver


class deleteCustomerTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_delete_customer(self):
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
        # Click View details under Customer
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div/div/div[1]/div/div/p[2]/a").click()
        time.sleep(1)
        # Click Delete Customer button
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[4]/td[13]/a").click()
        time.sleep(1)
        alert = driver.switch_to.alert
        alert.accept()
        print("alert accepted")
        time.sleep(1)
        assert "Deleted Customer successfully"


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()