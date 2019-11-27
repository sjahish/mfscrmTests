import unittest
import time
from selenium import webdriver


class addCustomerTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_add_customer(self):
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
        # Click Add Customer button
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/div/a/span").click()
        time.sleep(1)
        elem = driver.find_element_by_id("id_cust_name")
        elem.send_keys("Shafiq Jahish")
        elem = driver.find_element_by_id("id_organization")
        elem.send_keys("Capstone Inc.")

        elem = driver.find_element_by_id("id_role")
        elem.send_keys("Staff Assistant")

        elem = driver.find_element_by_id("id_bldgroom")
        elem.send_keys("PKI Room 270")

        elem = driver.find_element_by_id("id_account_number")
        elem.send_keys("100")

        elem = driver.find_element_by_id("id_address")
        elem.send_keys("1000 High dr.")

        elem = driver.find_element_by_id("id_city")
        elem.send_keys("Omaha")

        elem = driver.find_element_by_id("id_state")
        elem.send_keys("Nebraska")

        elem = driver.find_element_by_id("id_zipcode")
        elem.send_keys("68090")

        elem = driver.find_element_by_id("id_email")
        elem.send_keys("sj@unomaha.edu")

        elem = driver.find_element_by_id("id_phone_number")
        elem.send_keys("4021234567")

        # Click Save
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()
        time.sleep(1)
        assert "Added Customer successfully"



    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()