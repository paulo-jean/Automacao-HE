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

            Argumentos passados para a função:
            
        '''
        caminho_completo = os.path.join(origem, self._caminho)
        try:
            os.makedirs(caminho_completo)
        except: print()
        return caminho_completo
    
    def mover_arquivos(self, pasta_downloads, destino):
        ''' função para mover os diarios baixados da pasta Downloads
            para a pasta criada da respectiva turma.

            Argumentos passados para a função:
            pasta_downloads = pasta local de Downloads da máquina do usuário (que será coletada numa def através da biblioteca Pathlib).
            destino = é a pasta criada com o destino final escolhido pelo user, para onde será movido e armazenados os arquivos pdf's baixados automaticamente.
            self._turma = recebe um argumento da variável guardada na criação do objeto instanciado,
            que fará a separação exata de quais os arquivos pdf's que precisam ser movidos,
            e não somente qualquer ou todos os arquivos pdf's da pasta downloads do usuário.
        '''
        try:
            caminho_origem = f'{pasta_downloads}//*.pdf'
            arquivos = glob.glob(caminho_origem)

            for arquivo in arquivos:
                if self._turma in arquivo:
                    shutil.move(arquivo, destino)
        except: print()
