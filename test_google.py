import pytest
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

class TestGoogle:

    

    def setup_class(cls):
      cls.driver = webdriver.Chrome(executable_path = "C:/Users/yamato.kozai/Documents/Github/Selenium-circleci/driver/chromedriver.exe")
      cls.driver.maximize_window()
      
    def setup_method(self):
      driver = self.driver
      driver.get("https://google.com")

    def test_case(self):
      driver = self.driver

      driver.save_screenshot("test-reports/result_001.png")

      driver.find_element(By.CSS_SELECTOR,"#tsf > div:nth-child(2) > div > div.RNNXgb > div > div.a4bIc > input").send_keys("hoge")

      driver.save_screenshot("test-reports/result_002.png")

      driver.find_element(By.CSS_SELECTOR,"#tsf > div:nth-child(2) > div > div.FPdoLc.VlcLAe > center > input.gNO89b").click()

      driver.save_screenshot("test-reports/result_003.png")

      assert driver.title.count('hoge'), "ページタイトルにhogeが含まれていること"

    def teardown_class(cls):
        cls.driver.quit()