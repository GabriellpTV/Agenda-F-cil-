import datetime
import time
from tkinter.filedialog import askopenfilename
import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import calendar
import os
import tkinter as tk
from tkinter import *
from tkinter import Tk
from paths import * 
 
def last_day_of_month(year, month):
    return calendar.monthrange(year, month)[1]
 
def atualizar():
    global email, senha
    email = email_input.get()
    senha = senha_input.get()
    email_label.pack_forget()
    email_input.pack_forget()
    senha_label.pack_forget()
    senha_input.pack_forget()
    paragrafo_label.config(text="Agora Coloque a Base com os Fornecedores que Deseja Faturar")
    button.config(text="Inserir", command=lambda: iserir_base())
 
def iserir_base():
    base = askopenfilename()
    paragrafo_label.config(text="Deseja Faturar?")
    button.config(text="Faturar", command=lambda: faturar(base))
 
def faturar(base):
    time.sleep(6)
    processo_hub(base)
 
def buscar_elemento(driver, path):
    return driver.find_element('xpath', path)

def esperar_ficar_visivel(driver, path):
    element = WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, path)))
    return element 

def finalizar(base):
    paragrafo_label.config(text="Os produtos foram Faturados\nDeseja abrir o Relatório?")
    button.config(text="Abrir", command=lambda: abrir(base))
 
def abrir(base):
    os.startfile(base)
    root.quit()

def processo_hub(base):
    global email, senha
    
    relatorio = pd.read_excel(base)
    mes_atual = datetime.datetime.now().month
    mes_anterior = (mes_atual - 1) % 12
    if mes_anterior == 0:
        mes_anterior = 12
 
    year = datetime.datetime.now().year
    last_day = last_day_of_month(year, mes_anterior)
    data = f"{last_day}/{mes_anterior}/{year}"
 
    time.sleep(6)
    chrome_options = Options()
    # chrosme_options.add_argument("--headless=new")
    chrome_options.add_experimental_option("detach", True)
    servico = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=servico, options=chrome_options)
 
    time.sleep(6)

    # Login
    driver.get("https://hub.webmotors.com.br/login")
    buscar_elemento(driver, login_input_email).send_keys(email)
    buscar_elemento(driver, login_input_senha).send_keys(senha)
    buscar_elemento(driver, login_submit_button).click()
    
    # Caminho do Cadastro
    element = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[1]/a')))
    element.click()
    
    for i, cliente in enumerate(relatorio['Cliente']):
        cnpj = str(relatorio.loc[i, 'CNPJ'])
        valor_antigo = float(relatorio.loc[i, 'Total'])
        valor = "{:,.2f}".format(valor_antigo).replace('.', ',')

        faturado = str(relatorio.loc[i, 'Faturado'])

        if faturado  != 'Sim': 
            cont = 0
            while cont != 3:
                try:
                    element = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/nav[2]/div/div[2]/div/ul/li[2]/a')))
                    element.click()
                    buscar_elemento(driver, financeiro_menu_cadastrar_midia_programatica).click()

                    # Buscar Cliente
                    element = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/form/div[2]/div[2]/div/button')))
                    element.click()

                    element = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div/div/div[2]/form/div/div[1]/input')))
                    element.send_keys(cnpj)
                    time.sleep(2)
                    buscar_elemento(driver, midia_programatica_selecionar_button).click()
                    time.sleep(3)
    
                    situação = buscar_elemento(driver, midida_programatica_selecionar_situação).text
    
                    if situação == 'Ativo':
                        element = WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input.btnSelecionarCliente.btnModal.btnDefault.btnGreen')))
                        element.click()
    
                        element = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/form/div[4]/div[2]/div/div/select/option[5]')))
                        element.click()
                        time.sleep(2)
                        buscar_elemento(driver, midia_programatica_cadastrar__rps_diario).click()
                        buscar_elemento(driver, midia_programatica_cadastrar_produto_agenda_facil).click()
                        buscar_elemento(driver, midia_programatica_cadastrar_preco_total).send_keys(valor)
                        buscar_elemento(driver, midia_programatica_cadastrar_quantidade).send_keys('1')
                        buscar_elemento(driver, midia_programatica_cadastrar_data_faturamento).send_keys(data) 
                        buscar_elemento(driver, midia_programatica_cadastrar_confirmar_midia).click()
                        time.sleep(3)
                        buscar_elemento(driver, midia_programatica_cadastrar_confirmar_midia_sim).click()

                        print(cliente)
                        relatorio['Status'].loc[relatorio['Cliente'] == str(cliente)] = situação
                        relatorio['Faturado'].loc[relatorio['Cliente'] == str(cliente)] = 'Sim'
                        time.sleep(2)
                        cont = 3
                    else:
                        print(cliente)
                        relatorio['Status'].loc[relatorio['Cliente'] == str(cliente)] = situação
                        relatorio['Faturado'].loc[relatorio['Cliente'] == str(cliente)] = 'Não'
                        time.sleep(2)
                        cont = 3
                except:
                    cont += 1
                    if cont == 3:
                        relatorio['Status'].loc[relatorio['Cliente'] == str(cliente)] = "Não Encontrado"
                        relatorio['Faturado'].loc[relatorio['Cliente'] == str(cliente)] = 'Não'
                        time.sleep(2)
                    pass
 
        relatorio.to_excel(base, index=False)
        time.sleep(5)
 
    driver.quit()
    finalizar(base)

# Criar Interface Visual
root = Tk()
root.title('Inserir dados do Usuário')
root.resizable(False, False)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 550
window_height = 300
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")
 
label_titulo = Label(root, text="Faturar Fornecedores?")
label_titulo.pack()
 
paragrafo_label = Label(root, text="Primeiramente Insira os Dados de Login:")
paragrafo_label.pack()
 
email_label = Label(root, text="E-mail:")
email_label.pack()
email_input = Entry(root)
email_input.pack()
email_input.focus_set()
 
senha_label = Label(root, text="Senha:")
senha_label.pack()
senha_input = Entry()
senha_input.pack()
 
text_label = Label(root, text="")
text_label.pack()
button = Button(root, text="Guardar Login", command=atualizar)
button.pack()
 
root.mainloop()
