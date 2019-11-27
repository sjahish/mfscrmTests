import unittest
import time
from selenium import webdriver
import xlrd


class readAndAddCustomer(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_read_add_customer(self):
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
        print("Logged in")
        time.sleep(1)
        # Click View details under Customer
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div/div/div[1]/div/div/p[2]/a").click()
        time.sleep(1)

        workbook = xlrd.open_workbook("C:/Users/vaish/Customer_data.xlsx")
        sheet = workbook.sheet_by_name("Sheet1")
        rowcount = sheet.nrows
        for curr_row in range(1, rowcount, 1):
            # Click Add Customer button
            elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/div/a/span").click()
            time.sleep(1)

            row = sheet.row_values(curr_row)
            name = row[1]
            elem = driver.find_element_by_id("id_cust_name")
            elem.send_keys(name)

            organization = row[2]
            elem = driver.find_element_by_id("id_organization")
            elem.send_keys(organization)

            role = row[3]
            elem = driver.find_element_by_id("id_role")
            elem.send_keys(role)

            room = row[4]
            elem = driver.find_element_by_id("id_bldgroom")
            elem.send_keys(room)

            account_no = row[5]
            elem = driver.find_element_by_id("id_account_number")
            elem.send_keys(str(account_no))

            address = row[6]
            elem = driver.find_element_by_id("id_address")
            elem.send_keys(address)

            city = row[7]
            elem = driver.find_element_by_id("id_city")
            elem.send_keys(city)

            state = row[8]
            elem = driver.find_element_by_id("id_state")
            elem.send_keys(state)

            zipcode = row[9]
            elem = driver.find_element_by_id("id_zipcode")
            elem.send_keys(str(zipcode))

            email = row[10]
            elem = driver.find_element_by_id("id_email")
            elem.send_keys(email)

            phone = row[11]
            elem = driver.find_element_by_id("id_phone_number")
            elem.send_keys(str(phone))
            #click save
            elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()
            time.sleep(1)


        print("Added Customers successfully")




    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()