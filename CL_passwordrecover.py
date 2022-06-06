from time import sleep
from weakref import ref
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
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
WebDriverWait(driver,15).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"span#email")))
emailInput = driver.find_element(By.CSS_SELECTOR,"span#email")
email = emailInput.text

datos = email.split('@')
datos = datos[0].split('.')
site = "https://www.rebelsgolf.cl/"
nombre = datos[0]
apellido = datos[1]
password = "ZDpLud4J."
passwordchange = "J4duLpDZ."

#CREADO NUEVA PESTAÑA
driver.execute_script("window.open('');") 
driver.switch_to.window(driver.window_handles[1]) 

#REGISTER SITIO CHILENO
driver.get(site)
WebDriverWait(driver,15).until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/div[1]/header/div[1]/div/div/div/div[4]/div/div[2]/a/img'))) 
login_panel_button = driver.find_element(By.XPATH,'/html/body/div[1]/header/div[1]/div/div/div/div[4]/div/div[2]/a/img')
sleep(2)
login_panel_button.click() 
sleep(3)
create_account_button = driver.find_element(By.XPATH,'/html/body/div[7]/div/div[2]/div[3]/div/div/div[2]/div[1]/a')
sleep(2)
create_account_button.click() 
sleep(2)
input_nombre= driver.find_element(By.XPATH,'/html/body/div[7]/div/div[2]/div[3]/div/div/div[3]/div[1]/form/div[1]/input')
input_apellido= driver.find_element(By.XPATH,'/html/body/div[7]/div/div[2]/div[3]/div/div/div[3]/div[1]/form/div[2]/input')
input_email= driver.find_element(By.XPATH,'/html/body/div[7]/div/div[2]/div[3]/div/div/div[3]/div[1]/form/div[3]/input')
input_contraseña = driver.find_element(By.XPATH ,'/html/body/div[7]/div/div[2]/div[3]/div/div/div[3]/div[1]/form/div[5]/input') 
input_create_account = driver.find_element(By.XPATH,'/html/body/div[7]/div/div[2]/div[3]/div/div/div[3]/div[1]/form/div[13]/button') 
sleep(1)
input_nombre.send_keys(nombre) 
sleep(2)
input_apellido.send_keys(apellido) 
sleep(2) 
input_email.send_keys(email) 
sleep(2) 
input_contraseña.send_keys(password)  
sleep(2)
input_create_account.click()  
sleep(5)

#RESTABLECER CONTRASEÑA SITIO CHILENO
driver.get(site)
WebDriverWait(driver,15).until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/div[1]/header/div[1]/div/div/div/div[4]/div/div[2]/a/img'))) 
login_panel_button = driver.find_element(By.XPATH,'/html/body/div[1]/header/div[1]/div/div/div/div[4]/div/div[2]/a/img')
forgot_button = driver.find_element(By.XPATH,'/html/body/div[7]/div/div[2]/div[1]/form/div[2]/div[3]/div[2]/a') 
sleep(2)
login_panel_button.click() 
sleep(3) 
forgot_button.click()  
sleep(3)
WebDriverWait(driver,15).until(EC.presence_of_all_elements_located((By.XPATH,"/html/body/div[2]/div[3]/div/div/div/div/div/article/div/div/form/p[3]/button"))) 
input_email= driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div/div/div/div/div/article/div/div/form/p[2]/input')
restore_password_button = driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div/div/div/div/div/article/div/div/form/p[3]/button")
input_email.send_keys(email)
sleep(3)
try:
    restore_password_button.click()
except:
    restore_password_button.click()
sleep(3)

driver.switch_to.window(driver.window_handles[0])
sleep(5)
driver.refresh()
sleep(3)
WebDriverWait(driver,15).until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/div[2]/div[3]/div[2]/div[1]/div/table/tbody/tr[1]/td[1]'))) 
open_mail = driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div[2]/div[1]/div/table/tbody/tr[1]/td[1]')
open_mail.click()
sleep(3)
iframe = driver.find_element(By.XPATH,'/html/body/div/div[3]/div/div[2]/div/div/iframe')
driver.switch_to.frame(iframe)
reset_link = driver.find_element(By.XPATH,'/html/body/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr/td[2]/table/tbody/tr[10]/td/a')
sleep(2)
reset_link = reset_link.get_attribute('href')

driver.switch_to.window(driver.window_handles[1]) 
driver.get(reset_link)

input_new_password = driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div/div/div/div/div/article/div/div/form/p[2]/span/input')
reinput_new_password = driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div/div/div/div/div/article/div/div/form/p[3]/span/input')
input_change_password = driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div/div/div/div/div/article/div/div/form/p[4]/button')
sleep(3) 
input_new_password.send_keys(passwordchange) 
sleep(2) 
reinput_new_password.send_keys(passwordchange)  
try:
    input_change_password.click()
except:
    input_change_password.click()  
sleep(3)
ActionChains(driver).move_to_element(driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/div/div/div/article/div/div/div[1]')).perform()