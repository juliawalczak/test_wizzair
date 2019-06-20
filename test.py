# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import unittest
import time
import test_data

class WizzairRegistrationTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://wizzair.com/pl-pl/main-page#/")
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_wrong_email(self):
        driver = self.driver
        sign_in_button = driver.find_element_by_xpath('//*[@id="app"]/div/header/div[1]/div/nav/ul/li[7]/button')
        sign_in_button.click()
        registration_button = driver.find_element_by_xpath("//button[text()='Rejestracja']")
        registration_button.click()
        country_field = driver.find_element_by_xpath('//*[@id="regmodal-scroll-hook-6"]/div[1]/label/input')
        country_field.send_keys(test_data.valid_country)
        country_field.send_keys(Keys.ENTER)
        country_code_field= driver.find_element_by_xpath('//*[@id="regmodal-scroll-hook-3"]/div[1]/div/div[1]/div')
        country_code_field.click()
        country_code_field2 = driver.find_element_by_xpath('//*[@id="regmodal-scroll-hook-3"]/div[1]/div/div[1]/ul/li[1]/input')
        country_code_field2.send_keys(test_data.valid_country)
        country_code_field2.send_keys(Keys.ENTER)
        name_field = driver.find_element_by_xpath('//input[@placeholder="Imię"]')
        name_field.send_keys(test_data.valid_name)
        surname_field = driver.find_element_by_xpath('//input[@placeholder="Nazwisko"]')
        surname_field.send_keys(test_data.valid_surname)
        if test_data.valid_gender == 'male':
            gender_switch = driver.find_element_by_xpath("//label[@for='register-gender-male']")
            driver.execute_script("arguments[0].click()", gender_switch)
        else:
            gender_switch = driver.find_element_by_xpath("//label[@for='register-gender-female']")
            driver.execute_script("arguments[0].click()", gender_switch)
        telephone_field = driver.find_element_by_name("phoneNumberValidDigits")
        telephone_field.send_keys(test_data.valid_telephone)
        email_field = driver.find_element_by_css_selector("input[placeholder='E-mail'][data-test='booking-register-email']")
        email_field.send_keys(test_data.invalid_email)
        password_field = driver.find_element_by_xpath("//input[@data-test='booking-register-password']")
        password_field.send_keys(test_data.valid_password)
        
        privacy_policy = driver.find_element_by_xpath("//label[@for='registration-privacy-policy-checkbox']")
        privacy_policy.click()
        final_register_button = driver.find_element_by_xpath("//button[@data-test='booking-register-submit']")
        final_register_button.click()
        error_notice = driver.find_element_by_xpath('//*[@id="regmodal-scroll-hook-4"]/div[2]/span/span')
        assert error_notice.is_displayed()
        self.assertEqual(error_notice.get_attribute('innerText'), u"Nieprawidłowy adres e-mail")
        driver.save_screenshot('test_wrong_email.png')

if __name__== '__main__':
    unittest.main(verbosity=2)


