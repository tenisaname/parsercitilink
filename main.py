import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium_stealth import stealth
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from dataclasses import make_dataclass
import pandas as pd
from pandas import DataFrame




if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.add_argument(r"--user-data-dir=C:\\path\\to\\chrome\\user\\data") #e.g. C:\Users\You\AppData\Local\Google\Chrome\User Data
    url = "https://www.citilink.ru/catalog/noutbuki//"
    driver = webdriver.Chrome(service=ChromeService(executable_path='C:\\Users\\ETenkin\\Desktop\\ParserCitilink\\chromedriver.exe'),options=options)
    
    driver.get(url)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/main/section/div[2]/div/div/section/div[2]/div[2]/div[1]/div/div[3]/div[1]"))) # Название товара
    numbers_staff = driver.find_element(By.XPATH,"/html/body/div[2]/div/main/section/div[1]/div[1]/div[2]/span/span").text
    numbers_staff = numbers_staff.split(' ')
    numbers_staff = int(numbers_staff[0])
    print(numbers_staff)
    
    number_of_pages = numbers_staff / 48
    remainder_division = numbers_staff % 50
    counter = 1
    names_smartphones = []
    price_smartphones = []
    url_smartphones = []
    for i in range(1,int(number_of_pages)):
        for j in range(1,48):
            name = driver.find_element(By.XPATH,"/html/body/div[2]/div/main/section/div[2]/div/div/section/div[2]/div[2]/div["+str(j)+"]/div/div[3]/div[1]").text
            price  = driver.find_element(By.XPATH,"/html/body/div[2]/div/main/section/div[2]/div/div/section/div[2]/div[2]/div["+str(j)+"]/div/div[7]/div[1]/div[2]/span/span/span[1]").text
            names_smartphones.append(name)
            price_smartphones.append(price)
            url_smartphones.append(url)
            counter+=1
        time.sleep(5)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/main/section/div[2]/div/div/section/div[2]/div[3]/div/div[2]/a[6]/div"))) 
        driver.find_element(By.XPATH,"/html/body/div[2]/div/main/section/div[2]/div/div/section/div[2]/div[3]/div/div[2]/a[6]/div").click
    
    df = DataFrame({"Name":names_smartphones, "Price":price_smartphones})
    df.to_excel('output.xlsx',sheet_name='sheet1',index=True)
