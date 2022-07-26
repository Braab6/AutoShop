from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
from tkinter import *
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import random

root = Tk()


def Zalando ():
    driver = webdriver.Chrome("C:\\Users\\49152\\Downloads\\chromedriver_win32\\chromedriver.exe")
    driver.get("https://www.zalando.de/jordan-air-1-sneaker-low-joc12o006-a13.html")

    time.sleep(3.5)
    print("smth")

    cookie = driver.find_element(By.ID, "uc-btn-accept-banner").click()

    time.sleep(1)

    dropdown = driver.find_element(By.ID, "picker-trigger").click()
    size = driver.find_element(By.CSS_SELECTOR, "label[for='size-picker-JOC12O006-A130095000'] div[class='_0xLoFW FCIprz']").click()


def Nike ():

    password = "t:W4gqHz@DGX"
    email = "raab06b@gmail.com"

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
   # For older ChromeDriver under version 79.0.3945.16
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    #For ChromeDriver version 79.0.3945.16 or over
    options.add_argument('--disable-blink-features=AutomationControlled')

    driver = webdriver.Chrome(chrome_options=options, executable_path=r'C:\\Users\\49152\\Downloads\\chromedriver_win32\\chromedriver.exe')
    driver.get("https://www.nike.com/de/t/air-jordan-1-low-herrenschuh-PPffMw/553558-130")
   
    time.sleep(2)


    print("smth")

    cookie = driver.find_element(By.ID, "hf_cookie_text_cookieAccept").click()
    time.sleep(3)
    #login in account
    favorite = driver.find_element(By.XPATH, "//span[@class='wishlist-btn__tooltip prl3-sm']").click()
    time.sleep(1)
    email = driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(7) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(6) > form:nth-child(2) > div:nth-child(3) > input:nth-child(4)").send_keys(email)
    time.sleep(1)
    action = ActionChains(driver)
    action.send_keys(Keys.TAB)
    action.send_keys(password)
    time.sleep(1)
    currentURL = driver.current_url
    #open new tab
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(currentURL)
    email = driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(7) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(6) > form:nth-child(2) > div:nth-child(3) > input:nth-child(4)").send_keys(email)
    action.send_keys(Keys.TAB)
    action.send_keys(password)
    action.send_keys(Keys.ENTER)
    action.perform()


    #driver.execute_script("window.history.go(-1)")
    #time.sleep(1)
    #size = driver.find_element(By.ID, "skuAndSize__24375214")
    #time.sleep(1)
    #driver.execute_script("arguments[0].scrollIntoView();", size)
    #time.sleep(1)
    #driver.execute_script("arguments[0].click();", size)
    #time.sleep(5)
    #cart = driver.find_element(By.XPATH, "//button[@aria-label='In den Warenkorb']") .click()
    #time.sleep(1)
    
    #time.sleep(100)
  
    

root.title("AutoBot")
root.geometry("300x300")
root.resizable(False, False)

Zalandobutton = Button(root, text="Zalando", command=Zalando)
Zalandobutton.pack()

Nikebutton = Button(root, text="Nike", command=Nike)
Nikebutton.pack()

closeButton = Button(root, text="Close", command=root.destroy)
closeButton.place(x=150, y=100)



root.mainloop()




