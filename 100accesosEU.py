from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from calendar import day_abbr
from ctypes import sizeof
from lib2to3.pgen2.driver import Driver
from multiprocessing.connection import wait
from tkinter import E, N, Button

options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(options=options, executable_path=r'C:/Users/Esteban/Documents/UDP/Criptografía/Lab2/chromedriver')
driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

email_site = "https://www.fakemail.net/"

#CREADO DE CORREO ELECTRÓNICO TERMPORAL
driver.get(email_site)
sleep(5)
emailInput = driver.find_element(By.CSS_SELECTOR,"span#email")

email = emailInput.text
datos = email.split('@')
nombre = datos[0].replace('.','')
site = "https://www.fr9.es/"
password = "ZDpLud4J"
passwordchange = "J4duLpDZ"

#CREADO NUEVA PESTAÑA
driver.execute_script("window.open('');") 
driver.switch_to.window(driver.window_handles[1]) 

#REGISTER SITIO EUROPEO
driver.get(site)
WebDriverWait(driver,15).until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/div[5]/div/form[2]/div[1]/input'))) 
input_nombre= driver.find_element(By.XPATH,'/html/body/div[5]/div/form[2]/div[1]/input')
input_contraseña = driver.find_element(By.XPATH ,'/html/body/div[5]/div/form[2]/div[2]/input')
input_email= driver.find_element(By.XPATH,'/html/body/div[5]/div/form[2]/div[3]/input') 
input_create_account = driver.find_element(By.XPATH,'/html/body/div[5]/div/form[2]/div[6]/input[2]')
close_button = driver.find_element(By.XPATH,'/html/body/div[5]/div/div[4]/div[1]/span[2]')
sleep(1)
input_nombre.send_keys(nombre) 
sleep(2) 
input_contraseña.send_keys(password)  
sleep(2)
input_email.send_keys(email) 
sleep(2)
close_button.click()
sleep(2)
input_create_account.click()  
sleep(5)

for i in range(100):
    print("Intento de inicio numero: "+str(i+1))
    driver.get(site)
    WebDriverWait(driver,15).until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/div[4]/div/div[1]/a'))) 
    close_session = driver.find_element(By.XPATH,'/html/body/div[4]/div/div[1]/a')
    while True:
        try:   
            close_button = driver.find_element(By.XPATH,'/html/body/div[4]/div/div[7]/div/button')
            close_button.click()
        except:
            break
    close_session.click()
    sleep(5)
    #LOGIN SITIO EUROPEO
    WebDriverWait(driver,15).until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/div[5]/div/form[1]/div/div[2]/input[2]'))) 
    input_email_mask= driver.find_element(By.XPATH,'/html/body/div[5]/div/form[1]/div/div[2]/input[2]')
    input_contraseña_mask = driver.find_element(By.XPATH ,'/html/body/div[5]/div/form[1]/div/div[1]/input[1]') 
    input_email= driver.find_element(By.XPATH,'/html/body/div[5]/div/form[1]/div/div[2]/input[3]')
    input_contraseña = driver.find_element(By.XPATH ,'/html/body/div[5]/div/form[1]/div/div[1]/input[2]') 
    input_login = driver.find_element(By.XPATH,'/html/body/div[5]/div/form[1]/div/input[1]') 
    input_email_mask.click()
    sleep(5) 
    input_email.send_keys(nombre) 
    input_contraseña_mask.click()
    sleep(5) 
    input_contraseña.send_keys(password)  
    sleep(5)
    input_login.click()  
    sleep(3)