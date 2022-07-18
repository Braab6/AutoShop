from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
from tkinter import *

from selenium.webdriver.common.action_chains import ActionChains

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
    driver = webdriver.Chrome("C:\\Users\\49152\\Downloads\\chromedriver_win32\\chromedriver.exe")
    driver.get("https://www.nike.com/de/t/air-jordan-1-low-herrenschuh-PPffMw/553558-130")

    time.sleep(3.5)
    print("smth")

    #cookie = driver.find_element(By.ID, "uc-btn-accept-banner").click()

    time.sleep(1)

 
    size = driver.find_element(By.ID, "skuAndSize__24375104").click()


root.title("AutoBot")
root.geometry("300x300")
Zalandobutton = Button(root, text="Zalando", command=Zalando)
Zalandobutton.pack()
Nikebutton = Button(root, text="Nike", command=Nike)
Nikebutton.pack()

root.mainloop()




