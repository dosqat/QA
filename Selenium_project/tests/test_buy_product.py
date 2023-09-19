import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.cart_page import Cart_page
from pages.client_information_page import Client_information_page
from pages.finish_page import Finish_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.payment_page import Payment_page


def test_buy_product_1():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    service = Service(executable_path='C:\\Users\\user\\PycharmProjects\\Test_Selenium\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=service)

    print("Start Test 1")

    login = Login_page(driver)
    login.authorization()
    mp = Main_page(driver)
    mp.select_products_1()

    cp = Cart_page(driver)
    cp.click_checkout_button()

    cip = Client_information_page(driver)
    cip.input_information()

    p = Payment_page(driver)
    p.click_finish_button()

    f = Finish_page(driver)
    f.finish()

    print("Finish Test 1")
    time.sleep(5)
    driver.quit()

def test_buy_product_2():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    service = Service(executable_path='C:\\Users\\user\\PycharmProjects\\Test_Selenium\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=service)

    print("Start Test 2")

    login = Login_page(driver)
    login.authorization()
    mp = Main_page(driver)
    mp.select_products_2()

    cp = Cart_page(driver)
    cp.click_checkout_button()

     #cip = Client_information_page(driver)
     #cip.input_information()

     #p = Payment_page(driver)
     #p.click_finish_button()

     #f = Finish_page(driver)
     #f.finish()

    print("Finish Test 2")
    time.sleep(5)
    driver.quit()


def test_buy_product_3():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    service = Service(executable_path='C:\\Users\\user\\PycharmProjects\\Test_Selenium\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=service)

    print("Start Test 3")

    login = Login_page(driver)
    login.authorization()
    mp = Main_page(driver)
    mp.select_products_3()

    cp = Cart_page(driver)
    cp.click_checkout_button()

    #cip = Client_information_page(driver)
    #cip.input_information()

   # p = Payment_page(driver)
   # p.click_finish_button()

    #f = Finish_page(driver)
   # f.finish()

    print("Finish Test 3")
    time.sleep(5)
    driver.quit()


