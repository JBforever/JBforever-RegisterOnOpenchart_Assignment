from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Launch_chrome():
    def run_chrome(self):
        driver = webdriver.Chrome(
            executable_path="D:\\Jeshad\\Backup\\Jeshad Backup 31052021\\Testing course GitHub\\Full Project With Element\\AutomationBITM07-master\\Drivers\\chromedriver.exe")

        driver.maximize_window()

        driver.get("https://demo.opencart.com/")

        MyaccountBtn = driver.find_element(By.CSS_SELECTOR, '#top > div.container > div.nav.float-end > ul > li:nth-child(2) > div > a > span')
        MyaccountBtn.click()
        time.sleep(2)

        RegisterBtn = driver.find_element(By.CSS_SELECTOR,
                                           '#top > div.container > div.nav.float-end > ul > li:nth-child(2) > div > ul > li:nth-child(1) > a')
        RegisterBtn.click()
        time.sleep(2)

        firstname = driver.find_element(By.NAME, 'firstname')
        firstname.send_keys("Muhammad")
        time.sleep(2)

        lastname = driver.find_element(By.NAME, 'lastname')
        lastname.send_keys("Jeshad")
        time.sleep(2)

        email = driver.find_element(By.NAME, 'email')
        email.send_keys("md.jeshad97@gmail.com")
        time.sleep(2)

        password = driver.find_element(By.NAME, 'password')
        password.send_keys("bristi21")
        time.sleep(2)

        html = driver.find_element(By.XPATH, '/html')
        html.send_keys(Keys.END)

        SubscribeBtn = driver.find_element(By.CSS_SELECTOR, '#input-newsletter-yes')
        SubscribeBtn.click()
        time.sleep(2)

        html = driver.find_element(By.XPATH, '/html')
        html.send_keys(Keys.END)

        PrivacyBtn = driver.find_element(By.CSS_SELECTOR, '#form-register > div > div > div > input')
        PrivacyBtn.click()
        time.sleep(2)

        ContinueBtn = driver.find_element(By.CSS_SELECTOR, '#form-register > div > div > button')
        ContinueBtn.click()
        time.sleep(2)



















test_obj = Launch_chrome()
test_obj.run_chrome()
