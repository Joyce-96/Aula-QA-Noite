from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://joyce-96.github.io/Aula-QA-Noite/")

username = driver.find_element(By.ID, "email")
username.send_keys("teste@teste.com")

password = driver.find_element(By.ID, "senha")
password.send_keys("123456")

login_button = driver.find_element(By.ID, "button-entrar")
login_button.click()

time.sleep(5)

if "dashboard" in driver.current_url:
    print("Login realizado com sucesso!")
else:
    print("Falha no login.")

driver.quit()
