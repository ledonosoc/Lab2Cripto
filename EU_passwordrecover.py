from asyncio.windows_events import NULL
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

#RESTABLECER CONTRASEÑA SITIO EUROPEO
driver.get(site)
WebDriverWait(driver,15).until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/div[4]/div/div[1]/a'))) 
close_session = driver.find_element(By.XPATH,'/html/body/div[4]/div/div[1]/a')
close_session.click()
sleep(5)
driver.get(site+'usuario/olvido-su-contrasena')
WebDriverWait(driver,15).until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/div[5]/div/div[4]/div/form/div[1]/input'))) 
input_email= driver.find_element(By.XPATH,'/html/body/div[5]/div/div[4]/div/form/div[1]/input')
sleep(1)
input_email.send_keys(email) 
sleep(5) 
# create action chain object
input_forgot = driver.find_element(By.XPATH,'/html/body/div[5]/div/div[4]/div/form/input')
# perform the operation
ActionChains(driver).move_to_element(input_forgot).perform()
captcha = input('Please enter captcha \n')
codigo = driver.find_element_by_id("sign_code")
#Enviamos el captcha obtenido
codigo.send_keys(captcha)
input_forgot.click()
sleep(3)
while True:
    try:   
        driver.find_element(By.CLASS_NAME,"Wrong")
    except:
        break
    else:
        captcha = input('Please enter captcha correctly\n')
        codigo = driver.find_element(By.ID,"sign_code")
        #Enviamos el captcha obtenido
        input_forgot = driver.find_element(By.NAME,'contact_submit')
        codigo.send_keys(captcha)
        input_forgot.click()
        sleep(3)

driver.switch_to.window(driver.window_handles[0])
input('Please enter when email is received')
driver.refresh()
sleep(3)
WebDriverWait(driver,15).until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/div[2]/div[3]/div[2]/div[1]/div/table/tbody/tr[1]/td[1]'))) 
open_mail = driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div[2]/div[1]/div/table/tbody/tr[1]/td[1]')
open_mail.click()
sleep(3)
iframe = driver.find_element(By.XPATH,'/html/body/div/div[3]/div/div[2]/div/div/iframe')
driver.switch_to.frame(iframe)
reset_link = driver.find_element(By.XPATH,'/html/body/div[2]/table/tbody/tr/td/table/tbody/tr[1]/td/table[3]/tbody/tr/td/div/div/div[1]/span/span/a')
sleep(2)
reset_link = reset_link.get_attribute('href')

driver.switch_to.window(driver.window_handles[1]) 
driver.get(reset_link)

input_new_password = driver.find_element(By.XPATH,'/html/body/div[5]/div/div[4]/div/form/div[1]/input')
reinput_new_password = driver.find_element(By.XPATH,'/html/body/div[5]/div/div[4]/div/form/div[2]/input')
input_change_password = driver.find_element(By.XPATH,'/html/body/div[5]/div/div[4]/div/form/input')
sleep(3) 
input_new_password.send_keys(passwordchange) 
sleep(2) 
reinput_new_password.send_keys(passwordchange)  
input_change_password.click()
sleep(3)