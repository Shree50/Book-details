from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json
import time
import unittest
import HtmlTestRunner


class BookSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        ser_obj = Service("F:/Python/pythonProject/Driver/chromedriver.exe")
        cls.driver = webdriver.Chrome(service=ser_obj)

        cls.driver.get("https://www.flipkart.com/")
        cls.driver.maximize_window()

    def test_book_search(self):
        input_element = self.driver.find_element(By.CLASS_NAME, "Pke_EE")
        input_element.send_keys("Hindi Books", Keys.ENTER)
        time.sleep(5)

        actual_book_name = self.driver.find_element(By.CLASS_NAME, "wjcEIp")
        actual_rating = self.driver.find_element(By.CLASS_NAME, "XQDdHH")
        book_price = self.driver.find_element(By.CLASS_NAME, "Nx9bqj")
        actual_book_price = book_price.text.split("₹")

        details = [{
            "book_details": {
                "Book_Name": actual_book_name.text,
                "Rating": actual_rating.text,
                "Price": actual_book_price[1]
            },
        }]
        json_file = open("book.json", "w")
        json.dump(details, json_file, indent=4)
        json_file.close()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='F:/Python/pythonProject/Reports'))
