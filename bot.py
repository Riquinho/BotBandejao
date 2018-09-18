# coding=UTF-8
import time
import smtplib
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.common.exceptions import NoSuchElementException
from datetime import date
from pyvirtualdisplay import Display

import telepot

display=Display(visible=0, size=(800, 600)).start()

#while (int(time.strftime('%H%M%S')) != 201530):
#	print (time.strftime('%H%M%S'))

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://ru.ct.ufrj.br/form/ticket")
time.sleep(1)

verificador = None

while not verificador:
    try:
        verificador = driver.find_element_by_xpath('//option[.="CT - ALMOÇO ( dia %s das 10:30:00 até 14:20:00)"]' % date.today())
        print("Entrando...")
    except NoSuchElementException:
        time.sleep(10)
        print ("Aguardado bandejão abrir... Hora:" + time.strftime('%H:%M:%S'))
        driver.refresh()

print("Site disponivel para o agendamento")
print("Colocando CPF...")
cpf = driver.find_element_by_xpath('//input[@placeholder="CPF (sem pontuação)"]')
cpf.send_keys("12836825758")

print("Colocando data...")
data = driver.find_element_by_xpath('//input[@placeholder="Horário pretendido"]')
data.send_keys("%s 12:05:00" % date.today()) 
#data.click()
#data = driver.find_element_by_xpath('//span[.="12:00"]')
#data.click()
#data = driver.find_element_by_xpath('//span[.="12:05"]')
#data.click()

print("Clicando no capctha...")
cpf.click()
cpf.send_keys(Keys.TAB + Keys.TAB + Keys.TAB + " ")

time.sleep(3)
captha = driver.find_element_by_xpath('//button[@type="submit"]')
captha.click()

print ("Agendado!!!!!")
screen_name = "/home/joao/scripts/bandejao/screens/screen_%s.png" % date.today()
driver.save_screenshot(screen_name)
time.sleep(5)
driver.quit()
print("Sanvando imagem...")

print("Enviando mensagem para o telegram...")
bot = telepot.Bot("561853136:AAG3j6M4jpoC-4JeRcyXbJYMuURHuaZ5NPU")
bot.sendMessage(327947311,'Olá Riquinho, seu bandejão está agendado.')
bot.sendPhoto(chat_id=327947311, photo=open("/home/joao/scripts/bandejao/screens/screen_%s.png" % date.today(), 'rb'))
print ("Mensagem enviada para o telegram!")


