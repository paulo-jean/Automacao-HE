from selenium import webdriver
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

''' instâncias da classe Pastas com as turmas que serão usadas '''  
primeiro_a = Pastas('1 periodo Diarios/Diarios_1A','1A')
primeiro_b = Pastas('1 periodo Diarios/Diarios_1B','1B')
segundo_a = Pastas('1 periodo Diarios/Diarios_2A','2A')
segundo_b = Pastas('1 periodo Diarios/Diarios_2B','2B')
segundo_c = Pastas('1 periodo Diarios/Diarios_2C','2C')
terceiro_a = Pastas('1 periodo Diarios/Diarios_3A','3A')
terceiro_b = Pastas('1 periodo Diarios/Diarios_3B','3B')
terceiro_c = Pastas('1 periodo Diarios/Diarios_3C','3C')
quarto_a = Pastas('1 periodo Diarios/Diarios_4A','4A')
quarto_b = Pastas('1 periodo Diarios/Diarios_4B','4B')
quinto_a = Pastas('1 periodo Diarios/Diarios_5A','5A')
quinto_b = Pastas('1 periodo Diarios/Diarios_5B','5B')

# Passo 1: iniciando chrome
navegador = webdriver.Chrome()
navegador.implicitly_wait(10)

# opção de uso do navegador no modo incógnito:
#options = webdriver.ChromeOptions()
#options.add_argument("--incognito")
#navegador = webdriver.Chrome(options=options)

def selecionar_diretorio():
  try:
    messagebox.showinfo(message='Selecione a pasta onde deseja salvar os diários')
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
                            # Passo 1: coletar dados de login do usuario:
    # Passo 1-1: logar com usuario e senha na plataforma
                            # with pg.hold('alt'):
                            #     pg.press('tab')
                            # print('Digite seus dados de usuário e senha da plataforma HE:')
                            # if 'Created TensorFlow Lite XNNPACK delegate for CPU' == True: os.system('cls')
                            # usuario = input('Usuário: ')
                            # senha = input('Senha: ')
                            # os.system('cls')
                            # print('Agora aguarde a execução do programa...')
                            # time.sleep(3)
                            # with pg.hold('alt'):
                            #     pg.press('tab')

    navegador.get('https://sistemahe.com.br/')
    navegador.minimize_window()
    time.sleep(2)

    navegador.find_element(By.XPATH,
    '/html/body/div[2]/div/div[1]/div/div[2]/div/div/form/input[1]').send_keys("jmachado")
    navegador.find_element(By.XPATH,
    '/html/body/div[2]/div/div[1]/div/div[2]/div/div/form/input[2]').send_keys("stance@123")
    navegador.find_element(By.XPATH,
    '/html/body/div[2]/div/div[1]/div/div[2]/div/div/form/input[2]').send_keys(Keys.ENTER)

# url para Diários do primeiro período: https://sistemahe.com.br/config_periodos_diario_list?locale=pt_BR&periodo=1
def diarios_1A():

    # links que fazem o download direto dos diários - turma 1A:
    # ciências:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15040&locale=pt_BR')
    #Ed física e natação:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15009&locale=pt_BR')
    # História/Geografia:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15033&locale=pt_BR')
    # Inglês - Language:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15005&locale=pt_BR')
    # Língua Portuguesa:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15003&locale=pt_BR')
    # Matemática:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15004&locale=pt_BR')
    # Math:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15006&locale=pt_BR')
    # música:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15010&locale=pt_BR')
    # Postura do estudante:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15007&locale=pt_BR')
    # science:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15035&locale=pt_BR')
    # Social Studies:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15034&locale=pt_BR')
    # TE / makers:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15042&locale=pt_BR')
    # xadrez:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15011&locale=pt_BR')
    # Arte:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15008&locale=pt_BR')
    time.sleep(10)

    caminho_diarios_1A = Pastas.criar_pasta(primeiro_a, destino_escolhido_usuario)
    Pastas.mover_arquivos(primeiro_a, downloads, caminho_diarios_1A)

def diarios_1B():
    # links que fazem o download direto dos diários - turma 1B:
    # ciências:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15041&locale=pt_BR')
    #Ed física e natação:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15018&locale=pt_BR')
    # História/Geografia:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15036&locale=pt_BR')
    # Inglês - Language:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15014&locale=pt_BR')
    # Língua Portuguesa:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15012&locale=pt_BR')
    # Matemática:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15013&locale=pt_BR')
    # Math:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15015&locale=pt_BR')
    # música:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15019&locale=pt_BR')
    # Postura do estudante:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15016&locale=pt_BR')
    # science:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15038&locale=pt_BR')
    # Social Studies:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15037&locale=pt_BR')
    # TE / makers:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15043&locale=pt_BR')
    # xadrez:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15020&locale=pt_BR')
    # Arte:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15017&locale=pt_BR')
    time.sleep(10)

    # cria a pasta na área de trabalho
    try:
        os.mkdir(r'C:\Users\jmachado\Desktop\1 periodo Diarios\Diarios_1B') 
    except:
        print()
        
    # move os arquivos
    caminho_origem = r'C:\Users\jmachado\Downloads\*.pdf'
    caminho_destino = r'C:\Users\jmachado\Desktop\1 periodo Diarios\Diarios_1B'
    arquivos = glob.glob(caminho_origem)

    for arquivo in arquivos:
        if "1B" in arquivo:
            shutil.move(arquivo, caminho_destino)
def diarios_2A():
    # links que fazem o download direto dos diários - turma 2A:
    # ciências:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14902&locale=pt_BR')
    #Ed física e natação:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14910&locale=pt_BR')
    # Espanhol:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14911&locale=pt_BR')
    # História/Geografia:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14903&locale=pt_BR')
    # Inglês - Language:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14904&locale=pt_BR')
    # Língua Portuguesa:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14900&locale=pt_BR')
    # Matemática:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14901&locale=pt_BR')
    # Math:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14905&locale=pt_BR')
    # música:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14912&locale=pt_BR')
    # Postura do estudante:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14908&locale=pt_BR')
    # science:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14906&locale=pt_BR')
    # Social Studies:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14907&locale=pt_BR')
    # TE / makers:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15026&locale=pt_BR')
    # xadrez:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14913&locale=pt_BR')
    # Arte:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14909&locale=pt_BR')
    time.sleep(10)

    # cria a pasta na área de trabalho
    try:
        os.mkdir(r'C:\Users\jmachado\Desktop\1 periodo Diarios\Diarios_2A') 
    except:
        print()
        
    # move os arquivos
    caminho_origem = r'C:\Users\jmachado\Downloads\*.pdf'
    caminho_destino = r'C:\Users\jmachado\Desktop\1 periodo Diarios\Diarios_2A'
    arquivos = glob.glob(caminho_origem)

    for arquivo in arquivos:
        if "2A" in arquivo:
            shutil.move(arquivo, caminho_destino)
def diarios_2B():
    # links que fazem o download direto dos diários - turma 2B:
    # ciências:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14916&locale=pt_BR')
    #Ed física e natação:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14924&locale=pt_BR')
    # Espanhol:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14925&locale=pt_BR')
    # História/Geografia:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14917&locale=pt_BR')
    # Inglês - Language:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14918&locale=pt_BR')
    # Língua Portuguesa:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14914&locale=pt_BR')
    # Matemática:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14915&locale=pt_BR')
    # Math:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14919&locale=pt_BR')
    # música:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14926&locale=pt_BR')
    # Postura do estudante:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14922&locale=pt_BR')
    # science:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14920&locale=pt_BR')
    # Social Studies:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14921&locale=pt_BR')
    # TE / makers:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15027&locale=pt_BR')
    # xadrez:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14927&locale=pt_BR')
    # Arte:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14923&locale=pt_BR')
    time.sleep(10)

    # cria a pasta na área de trabalho
    try:
        os.mkdir(r'C:\Users\jmachado\Desktop\1 periodo Diarios\Diarios_2B') 
    except:
        print()
        
    # move os arquivos
    caminho_origem = r'C:\Users\jmachado\Downloads\*.pdf'
    caminho_destino = r'C:\Users\jmachado\Desktop\1 periodo Diarios\Diarios_2B'
    arquivos = glob.glob(caminho_origem)

    for arquivo in arquivos:
        if "2B" in arquivo:
            shutil.move(arquivo, caminho_destino)
def diarios_2C():
    # links que fazem o download direto dos diários - turma 2C:
    # ciências:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14930&locale=pt_BR')
    #Ed física e natação:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14938&locale=pt_BR')
    # Espanhol:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14939&locale=pt_BR')
    # História/Geografia:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14931&locale=pt_BR')
    # Inglês - Language:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14932&locale=pt_BR')
    # Língua Portuguesa:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14928&locale=pt_BR')
    # Matemática:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14929&locale=pt_BR')
    # Math:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14933&locale=pt_BR')
    # música:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14940&locale=pt_BR')
    # Postura do estudante:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14936&locale=pt_BR')
    # science:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14934&locale=pt_BR')
    # Social Studies:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14935&locale=pt_BR')
    # TE / makers:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15028&locale=pt_BR')
    # xadrez:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14941&locale=pt_BR')
    # Arte:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14937&locale=pt_BR')
    time.sleep(10)

    # cria a pasta na área de trabalho
    try:
        os.mkdir(r'C:\Users\jmachado\Desktop\1 periodo Diarios\Diarios_2C') 
    except:
        print()
        
    # move os arquivos
    caminho_origem = r'C:\Users\jmachado\Downloads\*.pdf'
    caminho_destino = r'C:\Users\jmachado\Desktop\1 periodo Diarios\Diarios_2C'
    arquivos = glob.glob(caminho_origem)

    for arquivo in arquivos:
        if "2C" in arquivo:
            shutil.move(arquivo, caminho_destino)
def diarios_3A():
    # links que fazem o download direto dos diários - turma 3A:
    # Arte:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14948&locale=pt_BR')
    # ciências:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14944&locale=pt_BR')
    #Ed física e natação:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14949&locale=pt_BR')
    # Espanhol:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14899&locale=pt_BR')
    # Geografia:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14946&locale=pt_BR')
    # História:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14945&locale=pt_BR')
    # Inglês - Language:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14895&locale=pt_BR')
    # Língua Portuguesa:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14942&locale=pt_BR')
    # Matemática:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14943&locale=pt_BR')
    # Math:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14896&locale=pt_BR')
    # música:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14950&locale=pt_BR')
    # Postura do estudante:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14947&locale=pt_BR')
    # science:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14897&locale=pt_BR')
    # Social Studies:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14898&locale=pt_BR')
    # TE / makers:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14951&locale=pt_BR')
    # xadrez:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14952&locale=pt_BR')
    time.sleep(10)

    # cria a pasta na área de trabalho
    try:
        os.mkdir(r'C:\Users\jmachado\Desktop\1 periodo Diarios\Diarios_3A') 
    except:
        print()
        
    # move os arquivos
    caminho_origem = r'C:\Users\jmachado\Downloads\*.pdf'
    caminho_destino = r'C:\Users\jmachado\Desktop\1 periodo Diarios\Diarios_3A'
    arquivos = glob.glob(caminho_origem)

    for arquivo in arquivos:
        if "3A" in arquivo:
            shutil.move(arquivo, caminho_destino)
def diarios_3B():
    # links que fazem o download direto dos diários - turma 3B:
    # Arte:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14963&locale=pt_BR')
    # ciências:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14955&locale=pt_BR')
    #Ed física e natação:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14964&locale=pt_BR')
    # Espanhol:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14965&locale=pt_BR')
    # Geografia:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14957&locale=pt_BR')
    # História:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14956&locale=pt_BR')
    # Inglês - Language:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14958&locale=pt_BR')
    # Língua Portuguesa:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14953&locale=pt_BR')
    # Matemática:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14954&locale=pt_BR')
    # Math:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14959&locale=pt_BR')
    # música:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14966&locale=pt_BR')
    # Postura do estudante:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14962&locale=pt_BR')
    # science:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14960&locale=pt_BR')
    # Social Studies:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14961&locale=pt_BR')
    # TE / makers:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14967&locale=pt_BR')
    # xadrez:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14968&locale=pt_BR')
    time.sleep(10)

    caminho_diarios_3B = Pastas.criar_pasta(terceiro_b, destino_escolhido_usuario)
    Pastas.mover_arquivos(terceiro_b, downloads, caminho_diarios_3B)
def diarios_3C():
    # links que fazem o download direto dos diários - turma 3C:
    # Arte:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15901&locale=pt_BR')
    # ciências:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15897&locale=pt_BR')
    #Ed física e natação:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15902&locale=pt_BR')
    # Espanhol:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15894&locale=pt_BR')
    # Geografia:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15899&locale=pt_BR')
    # História:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15898&locale=pt_BR')
    # Inglês - Language:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15890&locale=pt_BR')
    # Língua Portuguesa:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15895&locale=pt_BR')
    # Matemática:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15896&locale=pt_BR')
    # Math:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15891&locale=pt_BR')
    # música:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15903&locale=pt_BR')
    # Postura do estudante:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15900&locale=pt_BR')
    # science:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15892&locale=pt_BR')
    # Social Studies:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15893&locale=pt_BR')
    # TE / makers:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15904&locale=pt_BR')
    # xadrez:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15905&locale=pt_BR')
    time.sleep(10)

    # cria a pasta na área de trabalho
    try:
        os.mkdir(r'C:\Users\jmachado\Desktop\1 periodo Diarios\Diarios_3C') 
    except:
        print()
        
    # move os arquivos
    caminho_origem = r'C:\Users\jmachado\Downloads\*.pdf'
    caminho_destino = r'C:\Users\jmachado\Desktop\1 periodo Diarios\Diarios_3C'
    arquivos = glob.glob(caminho_origem)

    for arquivo in arquivos:
        if "3C" in arquivo:
            shutil.move(arquivo, caminho_destino)
def diarios_4A():
    # links que fazem o download direto dos diários - turma 4A:
    # Arte:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14975&locale=pt_BR')
    # ciências:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14971&locale=pt_BR')
    #Ed física e natação:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14976&locale=pt_BR')
    # Espanhol:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14977&locale=pt_BR')
    # Geografia:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14973&locale=pt_BR')
    # História:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14972&locale=pt_BR')
    # Inglês - Language:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14866&locale=pt_BR')
    # Língua Portuguesa:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14969&locale=pt_BR')
    # Matemática:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14970&locale=pt_BR')
    # Math:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14867&locale=pt_BR')
    # música:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14978&locale=pt_BR')
    # Postura do estudante:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14974&locale=pt_BR')
    # science:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14868&locale=pt_BR')
    # Social Studies:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14869&locale=pt_BR')
    # TE / makers:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14979&locale=pt_BR')
    # xadrez:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14980&locale=pt_BR')
    time.sleep(10)

    # cria a pasta na área de trabalho
    try:
        os.mkdir(r'C:\Users\jmachado\Desktop\1 periodo Diarios\Diarios_4A') 
    except:
        print()
        
    # move os arquivos
    caminho_origem = r'C:\Users\jmachado\Downloads\*.pdf'
    caminho_destino = r'C:\Users\jmachado\Desktop\1 periodo Diarios\Diarios_4A'
    arquivos = glob.glob(caminho_origem)

    for arquivo in arquivos:
        if "4A" in arquivo:
            shutil.move(arquivo, caminho_destino)
def diarios_4B():
    # links que fazem o download direto dos diários - turma 4B:
    # Arte:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14987&locale=pt_BR')
    # ciências:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14983&locale=pt_BR')
    #Ed física e natação:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14988&locale=pt_BR')
    # Espanhol:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14989&locale=pt_BR')
    # Geografia:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14985&locale=pt_BR')
    # História:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14984&locale=pt_BR')
    # Inglês - Language:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14870&locale=pt_BR')
    # Língua Portuguesa:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14981&locale=pt_BR')
    # Matemática:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14982&locale=pt_BR')
    # Math:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14871&locale=pt_BR')
    # música:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14990&locale=pt_BR')
    # Postura do estudante:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14986&locale=pt_BR')
    # science:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14872&locale=pt_BR')
    # Social Studies:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14873&locale=pt_BR')
    # TE / makers:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14991&locale=pt_BR')
    # xadrez:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14992&locale=pt_BR')
    time.sleep(10)

    # cria a pasta na área de trabalho
    try:
        os.mkdir(r'C:\Users\jmachado\Desktop\1 periodo Diarios\Diarios_4B') 
    except:
        print()
        
    # move os arquivos
    caminho_origem = r'C:\Users\jmachado\Downloads\*.pdf'
    caminho_destino = r'C:\Users\jmachado\Desktop\1 periodo Diarios\Diarios_4B'
    arquivos = glob.glob(caminho_origem)

    for arquivo in arquivos:
        if "4B" in arquivo:
            shutil.move(arquivo, caminho_destino)
def diarios_5A():
    # links que fazem o download direto dos diários - turma 5A:
    # Arte:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14994&locale=pt_BR')
    # ciências:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14878&locale=pt_BR')
    #Ed física e natação:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14995&locale=pt_BR')
    # Espanhol:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14883&locale=pt_BR')
    # Geografia:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14877&locale=pt_BR')
    # História:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14876&locale=pt_BR')
    # Inglês - Language:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14879&locale=pt_BR')
    # Língua Portuguesa:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14874&locale=pt_BR')
    # Matemática:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14875&locale=pt_BR')
    # Math:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14880&locale=pt_BR')
    # música:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15030&locale=pt_BR')
    # Postura do estudante:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14993&locale=pt_BR')
    # science:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14881&locale=pt_BR')
    # Social Studies:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14882&locale=pt_BR')
    # TE / makers:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14996&locale=pt_BR')
    # xadrez:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14997&locale=pt_BR')
    time.sleep(10)

    # cria a pasta na área de trabalho
    try:
        os.mkdir(r'C:\Users\jmachado\Desktop\1 periodo Diarios\Diarios_5A') 
    except:
        print()
        
    # move os arquivos
    caminho_origem = r'C:\Users\jmachado\Downloads\*.pdf'
    caminho_destino = r'C:\Users\jmachado\Desktop\1 periodo Diarios\Diarios_5A'
    arquivos = glob.glob(caminho_origem)

    for arquivo in arquivos:
        if "5A" in arquivo:
            shutil.move(arquivo, caminho_destino)
def diarios_5B():
    # links que fazem o download direto dos diários - turma 5B:
    # Arte:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14999&locale=pt_BR')
    # ciências:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14888&locale=pt_BR')
    #Ed física e natação:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15000&locale=pt_BR')
    # Espanhol:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14893&locale=pt_BR')
    # Geografia:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14887&locale=pt_BR')
    # História:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14886&locale=pt_BR')
    # Inglês - Language:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14889&locale=pt_BR')
    # Língua Portuguesa:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14884&locale=pt_BR')
    # Matemática:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14885&locale=pt_BR')
    # Math:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14890&locale=pt_BR')
    # música:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15031&locale=pt_BR')
    # Postura do estudante:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14998&locale=pt_BR')
    # science:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14891&locale=pt_BR')
    # Social Studies:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=14892&locale=pt_BR')
    # TE / makers:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15001&locale=pt_BR')
    # xadrez:
    navegador.get('https://sistemahe.com.br/impressao_diario?id=15002&locale=pt_BR')
    time.sleep(10)

    # cria a pasta na área de trabalho
    try:
        os.mkdir(r'C:\Users\jmachado\Desktop\1 periodo Diarios\Diarios_5B') 
    except:
        print()
        
    # move os arquivos
    caminho_origem = r'C:\Users\jmachado\Downloads\*.pdf'
    caminho_destino = r'C:\Users\jmachado\Desktop\1 periodo Diarios\Diarios_5B'
    arquivos = glob.glob(caminho_origem)

    for arquivo in arquivos:
        if "5B" in arquivo:
            shutil.move(arquivo, caminho_destino)


# passo 2: solicitar ao usuário um local para salvar os arquivos baixados e armazena
destino_escolhido_usuario = selecionar_diretorio()
if destino_escolhido_usuario == None:
    messagebox.showwarning(title='Pasta não selecionada', message='OPERAÇÃO CANCELADA!')
    navegador.close() 
downloads = pasta_downloads() # -> armazena o caminho da pasta 'Downloads' do usuário

# passo 3: entrar e logar no HE
logar_he()

# passo 4: baixar os diários por turma e disciplina, movendo-os para as suas pastas.
diarios_1A()
diarios_3B()


time.sleep(5)
messagebox.showinfo(message='O processo foi finalizado!')
navegador.close()

                                                                                    # with pg.hold('alt'):
                                                                                    #         pg.press('tab')
# comando de loop infinito para manter o navegador aberto até ser digitado 'sair'
# while True:
#     if input("Digite 'sair' para fechar o navegador: ").lower() == 'sair':
#         break
