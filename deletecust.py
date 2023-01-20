import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_delete_cust(self): 
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/Login") # buka situs
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID,"Username").send_keys("salsa") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"Password").send_keys("123") # isi password
        time.sleep(1)
        driver.find_element(By.NAME,"login").click()
        time.sleep(1)
        driver.find_element(By.XPATH,"//*/tr[3]/td[7]/a[3]").click()
        time.sleep(1)
        driver.find_element(By.XPATH,"//*/div/input").click()

        response_edit = driver.find_element(By.XPATH,"//*/tbody/tr[3]/td[1]").text
        self.assertEqual(response_edit, "Deleted")

    def test_delete_by_search_name(self):
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/Login") # buka situs
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID,"Username").send_keys("salsa") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"Password").send_keys("123") # isi password
        time.sleep(1)
        driver.find_element(By.NAME,"login").click()

        searching = driver.find_element(By.XPATH, "//*/tbody/tr[4]/td[1]").text
        driver.find_element(By.NAME, "searching").send_keys(searching)
        time.sleep(1)
        driver.find_element(By.XPATH,"//*/form/input[2]").click()
        time.sleep(1)
        driver.find_element(By.XPATH,"//*/tr[2]/td[7]/a[3]").click()
        time.sleep(1)
        driver.find_element(By.XPATH,"//*/div/input").click()
        time.sleep(3)
        driver.find_element(By.NAME, "searching").send_keys("Kassie Homenick")
        time.sleep(1)
        driver.find_element(By.XPATH, "//*/form/input[2]").click()
        time.sleep(1)

        response_edit = driver.find_element(By.XPATH,"//*/tbody/tr[4]/td[1]").text
        self.assertEqual(response_edit, "Kassie Homenick")

    def test_delete_by_search_email(self):
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/Login") # buka situs
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID,"Username").send_keys("salsa") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"Password").send_keys("123") # isi password
        time.sleep(1)
        driver.find_element(By.NAME,"login").click()
        
        searching = driver.find_element(By.XPATH, "//*/tbody/tr[5]/td[6]").text
        driver.find_element(By.NAME, "searching").send_keys(searching)
        time.sleep(1)
        driver.find_element(By.XPATH,"//*/form/input[2]").click()
        time.sleep(1)
        driver.find_element(By.XPATH,"//*/tr[2]/td[7]/a[3]").click()
        time.sleep(1)
        driver.find_element(By.XPATH,"//*/div/input").click()
        time.sleep(3)
        driver.find_element(By.NAME, "searching").send_keys("katharyn.ondricka@yahoo.com")
        time.sleep(1)
        driver.find_element(By.XPATH, "//*/form/input[2]").click()
        time.sleep(1)

        response_edit = driver.find_element(By.XPATH,"//*/tbody/tr[5]/td[1]").text
        self.assertEqual(response_edit, "katharyn.ondricka@yahoo.com")





unittest.main()