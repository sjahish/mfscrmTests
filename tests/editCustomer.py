import unittest
import time
from selenium import webdriver


class editCustomerTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_edit_customer(self):
        user = "instructor"
        pwd = "maverick1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/accounts/login/")
        time.sleep(1)
        # elem = driver.find_element_by_xpath("/html/body/section[1]/div/div/div/div/div/p[2]/a[1]").click()
        # time.sleep(3)
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
        # Click Edit Customer button
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[4]/td[12]/a").click()
        time.sleep(1)
        elem = driver.find_element_by_id("id_organization")
        elem.clear()
        elem.send_keys("ABC Inc.")

        elem = driver.find_element_by_id("id_state")
        elem.clear()
        elem.send_keys("NE")

        elem = driver.find_element_by_id("id_zipcode")
        elem.clear()
        elem.send_keys("67896")

        elem = driver.find_element_by_id("id_phone_number")
        elem.clear()
        elem.send_keys("6784562378")

        # Click Update
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()
        time.sleep(1)
        assert "Updated Customer successfully"


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()