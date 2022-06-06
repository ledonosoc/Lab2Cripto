from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from multiprocessing.connection import wait
lines = []
with open('C:/Users/Esteban/Documents/UDP/Criptografía/Lab2/clave,rut.txt') as f:
    lines = f.readlines()

datos = []
for line in lines:
    datos = line.split(",") 

    driver = webdriver.Chrome('C:/Users/Esteban/Documents/UDP/Criptografía/Lab2/chromedriver')
    driver.get('http://www.asimet.cl')

    WebDriverWait(driver,15).until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/div[3]/header/div/div/div/div/div[2]/div[2]/div[2]/ul[1]/li/a/span'))) 
    login_panel_button = driver.find_element(By.XPATH,'/html/body/div[3]/header/div/div/div/div/div[2]/div[2]/div[2]/ul[1]/li/a/span')
    sleep(2)
    login_panel_button.click() 
    sleep(3) 
    input_email= driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div/div/form/div[2]/input')
    input_contraseña = driver.find_element(By.XPATH ,'/html/body/div[2]/div/div[1]/div/div/form/div[3]/input') 
    input_login = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div/div/form/input[1]') 
    sleep(3) 
    input_email.send_keys(datos[1]) 
    sleep(2) 
    input_contraseña.send_keys(datos[0])  
    sleep(2)
    input_login.click()  
    sleep(3)