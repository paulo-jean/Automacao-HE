import os
import shutil
import glob

class Pastas:

    def __init__(self, caminho, turma):
        self._caminho = caminho
        self._turma = turma

    def __str__(self):
        return f'{self._caminho} - {self._turma}'
    
    def criar_pasta(self, origem):
        ''' função para criar a pasta dos diarios da respectiva turma.
        '''
        caminho_completo = os.path.join(origem, self._caminho)
        try:
            os.makedirs(caminho_completo)
        except: print()
        return caminho_completo
    
    def mover_arquivos(self, pasta_downloads, destino):
        ''' função para mover os diarios baixados, da pasta Downloads
            para a pasta criada da respectiva turma.
        '''
        try:
            caminho_origem = f'{pasta_downloads}//*.pdf'
            arquivos = glob.glob(caminho_origem)

            for arquivo in arquivos:
                if self._turma in arquivo:
                    shutil.move(arquivo, destino)
        except: print()

primeiro_a = Pastas('1 periodo Diarios/Diarios_1A','1A')
primeiro_b = Pastas('1 periodo Diarios/Diarios_1B','1B')
segundo_a = Pastas('1 periodo Diarios/Diarios_2A','2A')
segundo_b = Pastas('1 periodo Diarios/Diarios_2B','2B')
terceiro_a = Pastas('1 periodo Diarios/Diarios_2A','2A')
terceiro_b = Pastas('1 periodo Diarios/Diarios_2B','2B')
terceiro_c = Pastas('1 periodo Diarios/Diarios_2A','2A')
quarto_a = Pastas('1 periodo Diarios/Diarios_2B','2B')
quarto_b = Pastas('1 periodo Diarios/Diarios_2B','2B')
quinto_a = Pastas('1 periodo Diarios/Diarios_2B','2B')
quinto_b = Pastas('1 periodo Diarios/Diarios_2B','2B')