from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os
import glob
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from pathlib import Path
from Classes.Pastas import Pastas

# instânciando o serviço de atualização automatica da versao do navegador Chrome
# Passo 1: iniciando chrome
c_options = webdriver.ChromeOptions()
# modo incógnito:
#c_options.add_argument("--incognito")
c_options.add_argument('--headless')
c_options.add_argument('--no-sandbox')
navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
navegador.minimize_window()

''' instâncias da classe Pastas com as turmas que serão usadas '''  
primeiro_a = Pastas('2 periodo Diarios/Diarios_1A','1A')
primeiro_b = Pastas('2 periodo Diarios/Diarios_1B','1B')
segundo_a = Pastas('2 periodo Diarios/Diarios_2A','2A')
segundo_b = Pastas('2 periodo Diarios/Diarios_2B','2B')
segundo_c = Pastas('2 periodo Diarios/Diarios_2C','2C')
terceiro_a = Pastas('2 periodo Diarios/Diarios_3A','3A')
terceiro_b = Pastas('2 periodo Diarios/Diarios_3B','3B')
terceiro_c = Pastas('2 periodo Diarios/Diarios_3C','3C')
quarto_a = Pastas('2 periodo Diarios/Diarios_4A','4A')
quarto_b = Pastas('2 periodo Diarios/Diarios_4B','4B')
quinto_a = Pastas('2 periodo Diarios/Diarios_5A','5A')
quinto_b = Pastas('2 periodo Diarios/Diarios_5B','5B')

def selecionar_diretorio():
  try:
    messagebox.showinfo(message='Selecione o local para salvar os diários')
    caminho_local = filedialog.askdirectory(
      initialdir='../',
      title='Selecione uma pasta para salvar'
      )
    if caminho_local == '':
        caminho_local = None
  except:
    print()

  return caminho_local

def pasta_downloads():
    home = Path.home()
    downloads = home / 'Downloads'
    return downloads

def logar_he():

    navegador.get('https://sistemahe.com.br/')
    #navegador.minimize_window()
    time.sleep(1)

    navegador.find_element(By.XPATH,
    '/html/body/div[2]/div/div[1]/div/div[2]/div/div/form/input[2]').send_keys(os.getenv('HE_USER'))
    navegador.find_element(By.XPATH,
    '/html/body/div[2]/div/div[1]/div/div[2]/div/div/form/input[3]').send_keys(os.getenv('HE_PASS'))
    navegador.find_element(By.XPATH,
    '/html/body/div[2]/div/div[1]/div/div[2]/div/div/form/div/input').send_keys(Keys.ENTER)

def diarios_1A():
    # links que fazem o download direto dos diários - turma 1A:
    # Arte:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15285&locale=pt_BR')
    # ciências:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15305&locale=pt_BR')
    #Ed física e natação:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15286&locale=pt_BR')
    # História/Geografia:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15306&locale=pt_BR')
    # Inglês - Language:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15282&locale=pt_BR')
    # Língua Portuguesa:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15280&locale=pt_BR')
    # Matemática:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15281&locale=pt_BR')
    # Math:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15283&locale=pt_BR')
    # música:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15287&locale=pt_BR')
    # Postura do estudante:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15284&locale=pt_BR')
    # science:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15304&locale=pt_BR')
    # Social Studies:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15303&locale=pt_BR')
    # TE / makers:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15315&locale=pt_BR')
    # xadrez:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15288&locale=pt_BR')
    time.sleep(10)

    caminho_diarios_1A = Pastas.criar_pasta(primeiro_a, destino_escolhido_usuario)
    Pastas.mover_arquivos(primeiro_a, downloads, caminho_diarios_1A)

def diarios_1B():
    # links que fazem o download direto dos diários - turma 1B:
    links = [
    "https://sistemahe.com.br/impressao_diario?id=15294&locale=pt_BR",
    "https://sistemahe.com.br/impressao_diario?id=15309&locale=pt_BR",
    "https://sistemahe.com.br/impressao_diario?id=15295&locale=pt_BR",
    "https://sistemahe.com.br/impressao_diario?id=15310&locale=pt_BR",
    "https://sistemahe.com.br/impressao_diario?id_15291&locale=pt_BR",
    "https://sistemahe.com.br/impressao_diario?id=15289&locale=pt_BR",
    "https://sistemahe.com.br/impressao_diario?id=15290&locale=pt_BR",
    "https://sistemahe.com.br/impressao_diario?id=15292&locale=pt_BR",
    "https://sistemahe.com.br/impressao_diario?id=15296&locale=pt_BR",
    "https://sistemahe.com.br/impressao_diario?id=15293&locale=pt_BR",
    "https://sistemahe.com.br/impressao_diario?id=15308&locale=pt_BR",
    "https://sistemahe.com.br/impressao_diario?id=15307&locale=pt_BR",
    "https://sistemahe.com.br/impressao_diario?id=15316&locale=pt_BR",
    "https://sistemahe.com.br/impressao_diario?id=15297&locale=pt_BR"
]
    for link in links:
        navegador.get(link)
    time.sleep(10)

    caminho_diarios_1B = Pastas.criar_pasta(primeiro_b, destino_escolhido_usuario)
    Pastas.mover_arquivos(primeiro_b, downloads, caminho_diarios_1B)
    
def diarios_2A():
    # links que fazem o download direto dos diários - turma 2A:
    # Arte:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15151&locale=pt_BR')
    # ciências:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15144&locale=pt_BR')
    #Ed física e natação:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15152&locale=pt_BR')
    # Espanhol:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15153&locale=pt_BR')
    # História/Geografia:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15145&locale=pt_BR')
    # Inglês - Language:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15146&locale=pt_BR')
    # Língua Portuguesa:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15142&locale=pt_BR')
    # Matemática:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15143&locale=pt_BR')
    # Math:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15147&locale=pt_BR')
    # música:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15154&locale=pt_BR')
    # Postura do estudante:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15150&locale=pt_BR')
    # science:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15148&locale=pt_BR')
    # Social Studies:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15149&locale=pt_BR')
    # TE / makers:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15299&locale=pt_BR')
    # xadrez:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15155&locale=pt_BR')
    time.sleep(10)

    caminho_diarios_2A = Pastas.criar_pasta(segundo_a, destino_escolhido_usuario)
    Pastas.mover_arquivos(segundo_a, downloads, caminho_diarios_2A)

def diarios_2B():
    # links que fazem o download direto dos diários - turma 2B:
    # Arte:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15165&locale=pt_BR')
    # ciências:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15158&locale=pt_BR')
    #Ed física e natação:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15166&locale=pt_BR')
    # Espanhol:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15167&locale=pt_BR')
    # História/Geografia:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15159&locale=pt_BR')
    # Inglês - Language:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15160&locale=pt_BR')
    # Língua Portuguesa:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15156&locale=pt_BR')
    # Matemática:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15157&locale=pt_BR')
    # Math:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15161&locale=pt_BR')
    # música:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15168&locale=pt_BR')
    # Postura do estudante:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15164&locale=pt_BR')
    # science:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15162&locale=pt_BR')
    # Social Studies:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15163&locale=pt_BR')
    # TE / makers:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15300&locale=pt_BR')
    # xadrez:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15169&locale=pt_BR')
    time.sleep(10)

    caminho_diarios_2B = Pastas.criar_pasta(segundo_b, destino_escolhido_usuario)
    Pastas.mover_arquivos(segundo_b, downloads, caminho_diarios_2B)

def diarios_2C():
    # links que fazem o download direto dos diários - turma 2C:
    # Arte:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15179&locale=pt_BR')
    # ciências:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15172&locale=pt_BR')
    #Ed física e natação:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15180&locale=pt_BR')
    # Espanhol:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15181&locale=pt_BR')
    # História/Geografia:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15173&locale=pt_BR')
    # Inglês - Language:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15174&locale=pt_BR')
    # Língua Portuguesa:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15170&locale=pt_BR')
    # Matemática:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15171&locale=pt_BR')
    # Math:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15175&locale=pt_BR')
    # música:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15182&locale=pt_BR')
    # Postura do estudante:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15178&locale=pt_BR')
    # science:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15176&locale=pt_BR')
    # Social Studies:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15177&locale=pt_BR')
    # TE / makers:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15301&locale=pt_BR')
    # xadrez:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15183&locale=pt_BR')
    time.sleep(10)

    caminho_diarios_2C = Pastas.criar_pasta(segundo_c, destino_escolhido_usuario)
    Pastas.mover_arquivos(segundo_c, downloads, caminho_diarios_2C)

def diarios_3A():
    # links que fazem o download direto dos diários - turma 3A:
    # Arte:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15194&locale=pt_BR')
    # ciências:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15188&locale=pt_BR')
    #Ed física e natação:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15195&locale=pt_BR')
    # Espanhol:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15196&locale=pt_BR')
    # Geografia:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15187&locale=pt_BR')
    # História:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15186&locale=pt_BR')
    # Inglês - Language:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15189&locale=pt_BR')
    # Língua Portuguesa:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15184&locale=pt_BR')
    # Matemática:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15185&locale=pt_BR')
    # Math:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15190&locale=pt_BR')
    # música:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15198&locale=pt_BR')
    # Postura do estudante:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15193&locale=pt_BR')
    # science:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15191&locale=pt_BR')
    # Social Studies:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15192&locale=pt_BR')
    # TE / makers:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15197&locale=pt_BR')
    # xadrez:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15199&locale=pt_BR')
    time.sleep(10)

    caminho_diarios_3A = Pastas.criar_pasta(terceiro_a, destino_escolhido_usuario)
    Pastas.mover_arquivos(terceiro_a, downloads, caminho_diarios_3A)

def diarios_3B():
    # links que fazem o download direto dos diários - turma 3B:
    # Arte:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15210&locale=pt_BR')
    # ciências:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15204&locale=pt_BR')
    #Ed física e natação:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15211&locale=pt_BR')
    # Espanhol:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15212&locale=pt_BR')
    # Geografia:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15203&locale=pt_BR')
    # História:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15202&locale=pt_BR')
    # Inglês - Language:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15205&locale=pt_BR')
    # Língua Portuguesa:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15200&locale=pt_BR')
    # Matemática:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15201&locale=pt_BR')
    # Math:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15206&locale=pt_BR')
    # música:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15214&locale=pt_BR')
    # Postura do estudante:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15209&locale=pt_BR')
    # science:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15207&locale=pt_BR')
    # Social Studies:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15208&locale=pt_BR')
    # TE / makers:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15213&locale=pt_BR')
    # xadrez:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15215&locale=pt_BR')
    time.sleep(10)

    caminho_diarios_3B = Pastas.criar_pasta(terceiro_b, destino_escolhido_usuario)
    Pastas.mover_arquivos(terceiro_b, downloads, caminho_diarios_3B)

def diarios_3C():
    # links que fazem o download direto dos diários - turma 3C:
    # Arte:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15916&locale=pt_BR')
    # ciências:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15910&locale=pt_BR')
    #Ed física e natação:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15917&locale=pt_BR')
    # Espanhol:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15918&locale=pt_BR')
    # Geografia:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15909&locale=pt_BR')
    # História:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15908&locale=pt_BR')
    # Inglês - Language:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15911&locale=pt_BR')
    # Língua Portuguesa:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15906&locale=pt_BR')
    # Matemática:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15907&locale=pt_BR')
    # Math:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15912&locale=pt_BR')
    # música:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15920&locale=pt_BR')
    # Postura do estudante:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15915&locale=pt_BR')
    # science:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15913&locale=pt_BR')
    # Social Studies:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15914&locale=pt_BR')
    # TE / makers:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15919&locale=pt_BR')
    # xadrez:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15921&locale=pt_BR')
    time.sleep(10)

    caminho_diarios_3C = Pastas.criar_pasta(terceiro_c, destino_escolhido_usuario)
    Pastas.mover_arquivos(terceiro_c, downloads, caminho_diarios_3C)
        
def diarios_4A():
    # links que fazem o download direto dos diários - turma 4A:
    # Arte:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15226&locale=pt_BR')
    # ciências:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15220&locale=pt_BR')
    #Ed física e natação:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15227&locale=pt_BR')
    # Espanhol:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15228&locale=pt_BR')
    # Geografia:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15219&locale=pt_BR')
    # História:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15218&locale=pt_BR')
    # Inglês - Language:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15221&locale=pt_BR')
    # Língua Portuguesa:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15216&locale=pt_BR')
    # Matemática:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15217&locale=pt_BR')
    # Math:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15222&locale=pt_BR')
    # música:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15230&locale=pt_BR')
    # Postura do estudante:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15225&locale=pt_BR')
    # science:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15223&locale=pt_BR')
    # Social Studies:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15224&locale=pt_BR')
    # TE / makers:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15229&locale=pt_BR')
    # xadrez:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15231&locale=pt_BR')
    time.sleep(10)

    caminho_diarios_4A = Pastas.criar_pasta(quarto_a, destino_escolhido_usuario)
    Pastas.mover_arquivos(quarto_a, downloads, caminho_diarios_4A)
    
def diarios_4B():
    # links que fazem o download direto dos diários - turma 4B:
    # Arte:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15242&locale=pt_BR')
    # ciências:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15236&locale=pt_BR')
    #Ed física e natação:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15243&locale=pt_BR')
    # Espanhol:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15244&locale=pt_BR')
    # Geografia:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15235&locale=pt_BR')
    # História:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15234&locale=pt_BR')
    # Inglês - Language:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15237&locale=pt_BR')
    # Língua Portuguesa:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15232&locale=pt_BR')
    # Matemática:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15233&locale=pt_BR')
    # Math:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15238&locale=pt_BR')
    # música:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15246&locale=pt_BR')
    # Postura do estudante:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15241&locale=pt_BR')
    # science:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15239&locale=pt_BR')
    # Social Studies:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15240&locale=pt_BR')
    # TE / makers:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15245&locale=pt_BR')
    # xadrez:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15247&locale=pt_BR')
    time.sleep(10)

    caminho_diarios_4B = Pastas.criar_pasta(quarto_b, destino_escolhido_usuario)
    Pastas.mover_arquivos(quarto_b, downloads, caminho_diarios_4B)

def diarios_5A():
    # links que fazem o download direto dos diários - turma 5A:
    # Arte:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15258&locale=pt_BR')
    # ciências:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15252&locale=pt_BR')
    #Ed física e natação:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15259&locale=pt_BR')
    # Espanhol:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15260&locale=pt_BR')
    # Geografia:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15251&locale=pt_BR')
    # História:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15250&locale=pt_BR')
    # Inglês - Language:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15253&locale=pt_BR')
    # Língua Portuguesa:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15248&locale=pt_BR')
    # Matemática:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15249&locale=pt_BR')
    # Math:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15254&locale=pt_BR')
    # música:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15311&locale=pt_BR')
    # Postura do estudante:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15257&locale=pt_BR')
    # science:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15255&locale=pt_BR')
    # Social Studies:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15256&locale=pt_BR')
    # TE / makers:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15261&locale=pt_BR')
    # xadrez:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15262&locale=pt_BR')
    time.sleep(10)

    caminho_diarios_5A = Pastas.criar_pasta(quinto_a, destino_escolhido_usuario)
    Pastas.mover_arquivos(quinto_a, downloads, caminho_diarios_5A)

def diarios_5B():
    # links que fazem o download direto dos diários - turma 5B:
    # Arte:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15273&locale=pt_BR')
    # ciências:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15267&locale=pt_BR')
    #Ed física e natação:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15274&locale=pt_BR')
    # Espanhol:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15275&locale=pt_BR')
    # Geografia:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15266&locale=pt_BR')
    # História:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15265&locale=pt_BR')
    # Inglês - Language:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15268&locale=pt_BR')
    # Língua Portuguesa:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15263&locale=pt_BR')
    # Matemática:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15264&locale=pt_BR')
    # Math:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15269&locale=pt_BR')
    # música:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15312&locale=pt_BR')
    # Postura do estudante:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15272&locale=pt_BR')
    # science:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15270&locale=pt_BR')
    # Social Studies:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15271&locale=pt_BR')
    # TE / makers:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15276&locale=pt_BR')
    # xadrez:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15277&locale=pt_BR')
    time.sleep(10)

    caminho_diarios_5B = Pastas.criar_pasta(quinto_b, destino_escolhido_usuario)
    Pastas.mover_arquivos(quinto_b, downloads, caminho_diarios_5B)

def baixar_diarios():

    root = tk.Tk()
    root.attributes('-topmost', True)  # mostrar a janela sobreposta a outras abertas
    # Obter as dimensões da tela
    largura_tela = root.winfo_screenwidth()
    altura_tela = root.winfo_screenheight()

    # Definir as dimensões da janela
    largura_janela = 400
    altura_janela = 400

    # Calcular a posição para centralizar
    posicao_x = (largura_tela - largura_janela) // 2
    posicao_y = (altura_tela - altura_janela) // 2

    # Definir a geometria da janela
    root.geometry(f"{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}")
    root.title("Download de Diários")

    descricao = tk.Label(root, text='Selecione qual turma deseja baixar os diários:', font=("Arial", 11, "bold"))
    descricao.pack()

    checkbox_frame = tk.Frame(root)
    checkbox_frame.pack()
    
    # def criar_checkboxes():
    primeiro_a_var = tk.BooleanVar()
    tk.Checkbutton(checkbox_frame, text="1A", variable=primeiro_a_var).pack()
    primeiro_b_var = tk.BooleanVar()
    tk.Checkbutton(checkbox_frame, text="1B", variable=primeiro_b_var).pack()

    segundo_a_var = tk.BooleanVar()
    tk.Checkbutton(checkbox_frame, text="2A", variable=segundo_a_var).pack()
    segundo_b_var = tk.BooleanVar()
    tk.Checkbutton(checkbox_frame, text="2B", variable=segundo_b_var).pack()
    segundo_c_var = tk.BooleanVar()
    tk.Checkbutton(checkbox_frame, text="2C", variable=segundo_c_var).pack()

    terceiro_a_var = tk.BooleanVar()
    tk.Checkbutton(checkbox_frame, text="3A", variable=terceiro_a_var).pack()
    terceiro_b_var = tk.BooleanVar()
    tk.Checkbutton(checkbox_frame, text="3B", variable=terceiro_b_var).pack()
    terceiro_c_var = tk.BooleanVar()
    tk.Checkbutton(checkbox_frame, text="3C", variable=terceiro_c_var).pack()

    quarto_a_var = tk.BooleanVar()
    tk.Checkbutton(checkbox_frame, text="4A", variable=quarto_a_var).pack()
    quarto_b_var = tk.BooleanVar()
    tk.Checkbutton(checkbox_frame, text="4B", variable=quarto_b_var).pack()

    quinto_a_var = tk.BooleanVar()
    tk.Checkbutton(checkbox_frame, text="5A", variable=quinto_a_var).pack()
    quinto_b_var = tk.BooleanVar()
    tk.Checkbutton(checkbox_frame, text="5B", variable=quinto_b_var).pack()

    todas_turmas_var = tk.BooleanVar()
    tk.Checkbutton(checkbox_frame, text="Todas", variable=todas_turmas_var).pack()


    def baixar_diarios_selecionados():
        root.iconify()

        if todas_turmas_var.get():
            [diarios_1A(),diarios_1B(),diarios_2A(),diarios_2B(),diarios_2C(),diarios_3A(),diarios_3B(),diarios_3C(),diarios_4A(),diarios_4B(),diarios_5A(),diarios_5B()]
        if primeiro_a_var.get():
            diarios_1A()
        if primeiro_b_var.get():
            diarios_1B()
        if segundo_a_var.get():
            diarios_2A()
        if segundo_b_var.get():
            diarios_2B()
        if segundo_c_var.get():
            diarios_2C()
        if terceiro_a_var.get():
            diarios_3A()
        if terceiro_b_var.get():
            diarios_3B()
        if terceiro_c_var.get():
            diarios_3C()
        if quarto_a_var.get():
            diarios_4A()
        if quarto_b_var.get():
            diarios_4B()
        if quinto_a_var.get():
            diarios_5A()
        if quinto_b_var.get():
            diarios_5B()

        root.quit()
        root.destroy()

    baixar_button = tk.Button(root, text="Baixar", command=baixar_diarios_selecionados)
    baixar_button.pack()

    root.mainloop()

# passo 2: solicitar ao usuário um local para salvar os arquivos baixados e armazena
destino_escolhido_usuario = selecionar_diretorio()
if destino_escolhido_usuario == None:
    messagebox.showwarning(title='Local não selecionado', message='OPERAÇÃO CANCELADA\nA pasta não foi selecionada!')
    navegador.close() 
else:
    downloads = pasta_downloads() # -> armazena o caminho da pasta 'Downloads' do usuário
    logar_he() # passo 3: entrar e logar no HE (o usuário não vê esse processo pois o navegador é minimizado)
    baixar_diarios() # passo 4: é criado uma interface com checkboxes tkinter, onde solicita ao usuário selecionar quais turmas quer baixar os diários.
                     # passo 5 e último: após selecionar e clicar no botão 'baixar', começa todo o processo automatizado definido nas funções.  
    time.sleep(3)
    navegador.close()
    messagebox.showwarning(title='Finish', message='O processo foi finalizado!')
