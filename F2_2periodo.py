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

''' instâncias da classe Pastas com as turmas que serão usadas '''  
sexto_a = Pastas('3 periodo Diarios/Diarios_6A','6A')
sexto_b = Pastas('3 periodo Diarios/Diarios_6B','6B')
setimo_a = Pastas('3 periodo Diarios/Diarios_7A','7A')
setimo_b = Pastas('3 periodo Diarios/Diarios_7B','7B')
oitavo_a = Pastas('3 periodo Diarios/Diarios_8A','8A')
oitavo_b = Pastas('3 periodo Diarios/Diarios_8B','8B')
nono_a = Pastas('3 periodo Diarios/Diarios_9A','9A')

# instânciando o serviço de atualização automatica da versao do navegador Chrome
# Passo 1: iniciando chrome
c_options = webdriver.ChromeOptions()
c_options.add_argument('--headless')
navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=c_options)
navegador.minimize_window()

def selecionar_diretorio():
  try:
    messagebox.showinfo(message='Selecione o local para salvar os diários')
    caminho_local = filedialog.askdirectory(
      initialdir='../',
      title='Selecione o local para salvar'
      )
    if caminho_local == '':
        caminho_local = None
  except: print()

  return caminho_local

def caminho_downloads():
    home = Path.home()
    downloads = home / 'Downloads'
    return downloads

def logar_he():
    ''' '''
    # Passo 1-1: logar com usuario e senha na plataforma
    #navegador.minimize_window()
    navegador.get('https://sistemahe.com.br/')
    time.sleep(2)

    navegador.find_element(By.XPATH,
    '/html/body/div[2]/div/div[1]/div/div[2]/div/div/form/input[2]').send_keys(os.getenv('HE_USER'))
    navegador.find_element(By.XPATH,
    '/html/body/div[2]/div/div[1]/div/div[2]/div/div/form/input[3]').send_keys(os.getenv('HE_PASS'))
    navegador.find_element(By.XPATH,
    '/html/body/div[2]/div/div[1]/div/div[2]/div/div/form/div/input').send_keys(Keys.ENTER)

def diarios_6A():
    # links que fazem o download direto dos diários - turma 6A:
    links = [
    'https://sistemahe.com.br/impressao_diario?id=15053&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15132&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15051&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15045&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15110&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15047&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15046&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15141&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15044&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15049&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15052&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15050&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15048&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15054&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15128&locale=pt_BR'
]
    for link in links:
        navegador.get(link)
    
    time.sleep(10)

    caminho_completo_6A = Pastas.criar_pasta(sexto_a, destino_escolhido_usuario)
    Pastas.mover_arquivos(sexto_a, pasta_downloads, caminho_completo_6A)

def diarios_6B():
    # links que fazem o download direto dos diários - turma 6B:
    links = [
    'https://sistemahe.com.br/impressao_diario?id=15097&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15135&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15115&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15102&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15278&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15109&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15055&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15126&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15302&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15096&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15134&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15137&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15313&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15111&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15130&locale=pt_BR'
]
    for link in links:
        navegador.get(link)
    time.sleep(10)

    caminho_completo_6B = Pastas.criar_pasta(sexto_b, destino_escolhido_usuario)
    Pastas.mover_arquivos(sexto_b, pasta_downloads, caminho_completo_6B)
    
def diarios_7A():
    # links que fazem o download direto dos diários - turma 7A:
    links = [
    'https://sistemahe.com.br/impressao_diario?id=15098&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15061&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15064&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15103&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15058&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15060&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15059&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15057&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15056&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15063&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15107&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15118&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15062&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15065&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15119&locale=pt_BR'
]
    for link in links:
        navegador.get(link)
    time.sleep(10)

    caminho_completo_7A = Pastas.criar_pasta(setimo_a, destino_escolhido_usuario)
    Pastas.mover_arquivos(setimo_a, pasta_downloads, caminho_completo_7A)

def diarios_7B():
    # links que fazem o download direto dos diários - turma 2B:
    links = [
    'https://sistemahe.com.br/impressao_diario?id=15099&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15279&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15116&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15106&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15133&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15114&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15066&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15138&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15136&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15067&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15127&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15139&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15314&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15112&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15131&locale=pt_BR'
]
    for link in links:
        navegador.get(link)
    time.sleep(10)

    caminho_completo_7B = Pastas.criar_pasta(setimo_b, destino_escolhido_usuario)
    Pastas.mover_arquivos(setimo_b, pasta_downloads, caminho_completo_7B)

def diarios_8A():
    # links que fazem o download direto dos diários - turma 8A:
    links = [
    'https://sistemahe.com.br/impressao_diario?id=15100&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15073&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15077&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15104&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15070&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15072&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15071&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15108&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15069&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15068&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15075&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15076&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15074&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15078&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15120&locale=pt_BR'
]
    for link in links:
        navegador.get(link)
    time.sleep(10)

    caminho_completo_8A = Pastas.criar_pasta(oitavo_a, destino_escolhido_usuario)
    Pastas.mover_arquivos(oitavo_a, pasta_downloads, caminho_completo_8A)

def diarios_8B():
    # links que fazem o download direto dos diários - turma 8B:
    links = [
    'https://sistemahe.com.br/impressao_diario?id=15101&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15298&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15083&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15105&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15081&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15122&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15082&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15123&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15080&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15079&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15117&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15140&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15125&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15113&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15129&locale=pt_BR'
]
    for link in links:
        navegador.get(link)
    time.sleep(10)

    caminho_completo_8B = Pastas.criar_pasta(oitavo_b, destino_escolhido_usuario)
    Pastas.mover_arquivos(oitavo_b, pasta_downloads, caminho_completo_8B)

def diarios_9A():
    # links que fazem o download direto dos diários - turma 9A:
    links = [
    'https://sistemahe.com.br/impressao_diario?id=15124&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15089&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15093&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15086&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15088&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15087&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15094&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15085&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15084&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15091&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15092&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15090&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15095&locale=pt_BR',
    'https://sistemahe.com.br/impressao_diario?id=15121&locale=pt_BR'
]
    for link in links:
        navegador.get(link)
    time.sleep(10)

    caminho_completo_9A = Pastas.criar_pasta(nono_a, destino_escolhido_usuario)
    Pastas.mover_arquivos(nono_a, pasta_downloads, caminho_completo_9A)

def baixar_diarios():

    root = tk.Tk()
    root.attributes('-topmost', True)  # mostrar a janela sobreposta a outras abertas
    # Obter as dimensões da tela
    largura_tela = root.winfo_screenwidth()
    altura_tela = root.winfo_screenheight()

    # Definir as dimensões da janela
    largura_janela = 400
    altura_janela = 300

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
    tk.Checkbutton(checkbox_frame, text="6A", variable=primeiro_a_var).pack()
    primeiro_b_var = tk.BooleanVar()
    tk.Checkbutton(checkbox_frame, text="6B", variable=primeiro_b_var).pack()

    segundo_a_var = tk.BooleanVar()
    tk.Checkbutton(checkbox_frame, text="7A", variable=segundo_a_var).pack()
    segundo_b_var = tk.BooleanVar()
    tk.Checkbutton(checkbox_frame, text="7B", variable=segundo_b_var).pack()

    terceiro_a_var = tk.BooleanVar()
    tk.Checkbutton(checkbox_frame, text="8A", variable=terceiro_a_var).pack()
    terceiro_b_var = tk.BooleanVar()
    tk.Checkbutton(checkbox_frame, text="8B", variable=terceiro_b_var).pack()
    
    quarto_a_var = tk.BooleanVar()
    tk.Checkbutton(checkbox_frame, text="9A", variable=quarto_a_var).pack()

    todas_turmas_var = tk.BooleanVar()
    tk.Checkbutton(checkbox_frame, text="Todas", variable=todas_turmas_var).pack()


    def baixar_diarios_selecionados():
        root.iconify()

        if todas_turmas_var.get():
            [diarios_6A(),diarios_6B(),diarios_7A(),diarios_7B(),diarios_8A(),diarios_8B(),diarios_9A()]
        if primeiro_a_var.get():
            diarios_6A()
        if primeiro_b_var.get():
            diarios_6B()
        if segundo_a_var.get():
            diarios_7A()
        if segundo_b_var.get():
            diarios_7B()
        if terceiro_a_var.get():
            diarios_8A()
        if terceiro_b_var.get():
            diarios_8B()
        if quarto_a_var.get():
            diarios_9A()

        root.quit()

    baixar_button = tk.Button(root, text="Baixar", command=baixar_diarios_selecionados)
    baixar_button.pack()

    root.mainloop()

#passo 2: solicitar ao usuário um local para salvar os arquivos baixados e armazena
destino_escolhido_usuario = selecionar_diretorio()
if destino_escolhido_usuario == None:
    messagebox.showwarning(title='Erro 0x001', message='OPERAÇÃO CANCELADA\nA pasta não foi selecionada!')
    navegador.close()
else:
    pasta_downloads = caminho_downloads() # -> armazena o caminho da pasta 'Downloads' do usuário
    logar_he() # passo 3: entrar e logar no HE (o usuário não vê esse processo pois o navegador é minimizado)
    baixar_diarios()# passo 4: é criado uma interface com checkboxes tkinter, onde solicita ao usuário selecionar quais turmas quer baixar os diários.
                     # passo 5 e último: após selecionar e clicar no botão 'baixar', começa todo o processo automatizado definido nas funções.
    time.sleep(5)
    messagebox.showwarning(title='Finish', message='O processo foi finalizado!')
    navegador.close()
