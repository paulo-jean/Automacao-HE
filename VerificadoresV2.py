import camelot
import pdfplumber
import pandas as pd
import glob
import os


# classe responsável por verificar os diários do 2 período
class Check2P:
    
    @staticmethod
    def verificar_presenca_aluno(df_list):
        for df in df_list:
            if 'F' in df.values or 'FF' in df.values:
                return True
        return False

    @staticmethod
    def verificar_indicadores(content):
        return any(i in str(content) for i in ['A', 'B', 'C', 'D', 'RI'])

    @staticmethod
    def verificar_sintese(content):
        indicadores = ['P', 'S', 'I', 'RI', 'RA', 'PD']
        return any(i in str(content) for i in indicadores)

    @staticmethod
    def verificar_eixo(content):
        vogais = ['a', 'e', 'i', 'o']
        return any(v in str(content).lower() for v in vogais)

    @staticmethod
    def extract_tables_from_pdf(pdf_path):
        tables = {}
        try:
            with pdfplumber.open(pdf_path) as pdf:
                for page_num, page in enumerate(pdf.pages, 1):
                    try:
                        page_tables = camelot.read_pdf(pdf_path, pages=str(page_num))
                        if page_tables:
                            tables[page_num] = page_tables
                    except Exception as e:
                        print(f"Erro ao extrair tabelas da página {page_num}: {str(e)}")
        except Exception as e:
            print(f"Erro ao abrir o PDF {pdf_path}: {str(e)}")
        return tables

    @staticmethod
    def extract_text_from_pdf(pdf_path):
        text_content = {}
        with pdfplumber.open(pdf_path) as pdf:
            for page_num, page in enumerate(pdf.pages, 1):
                text_content[page_num] = page.extract_text()
        return text_content

    @classmethod
    def verificacao_geral(cls, diarios: list):
        resultados = []
        for diario in diarios:
            verificacoes = []

            try:
                tables = cls.extract_tables_from_pdf(diario)
                #tabula_tables = tabula.read_pdf(diario, pages="all")
                text_content = cls.extract_text_from_pdf(diario)

                if not tables:
                    verificacoes.append("Não foi possível extrair tabelas do PDF")
                else:
                    # Verificar presença de alunos (páginas 2-5)
                    df_list = [table.df.drop([0], axis=1) for page in range(2, 6) for table in tables.get(page, [])]
                    if not df_list:
                        verificacoes.append("Não foi possível encontrar tabelas de presença")
                    elif not cls.verificar_presenca_aluno(df_list):
                        verificacoes.append("faltas não preenchidas")

                    # Verificar indicadores (penúltima página com tabelas)
                    if len(tables) > 1:
                      second_last_page = sorted(tables.keys())[-2]
                      #if len(tables[second_last_page]) >= 2:
                      try:
                        df_indicadores = tables[second_last_page][0].df # ISSUE resolver -> resolvido!
                        if len(df_indicadores.index) > 1 and len(df_indicadores.columns) > 1:
                          df_indicadores = df_indicadores.drop([0], axis=1).drop([0], axis=0)
                          if not cls.verificar_indicadores(df_indicadores):
                            verificacoes.append("indicadores não preenchidos")
                        else:
                          verificacoes.append("tabela de indicadores vazia ou mal formatada")
                      except:
                        verificacoes.append("tabela de indicadores vazia ou mal formatada")

                    # Verificar síntese e eixo (última página com tabelas) -> minha versão
                    if len(tables) > 1:
                        last_table_page = sorted(tables.keys())[-1]
                        # verificar se a ultima pag é curriculo adaptado:
                        if 'currículo' in str(tables[last_table_page][0].df.values).lower().split():
                            #print('** CURRICULO ADAPTADO **')
                            last_table_page = sorted(tables.keys())[-2]

                        #if len(math_tables[last_table_page]) >= 2:
                        try:
                            if 'Síntese' in tables[last_table_page][0].df.values:
                                df_sintese = tables[last_table_page][0].df
                            elif 'Síntese' in tables[last_table_page][1].df.values:
                                df_sintese = tables[last_table_page][1].df
                        except:
                            pass #verificacoes.append("tabela de síntese vazia ou mal formatada")
                        try:
                            if 'Eixo de Formação da Postura de Estudante' in tables[last_table_page][0].df.values:
                                df_eixo = tables[last_table_page][0].df
                            elif 'Eixo de Formação da Postura de Estudante' in tables[last_table_page][1].df.values:
                                df_eixo = tables[last_table_page][1].df
                        except:
                            pass #verificacoes.append("tabela de postura vazia ou mal formatada")


                        try:
                            if len(df_sintese.index) > 1 and len(df_sintese.columns) > 1:
                                df_sintese = df_sintese.drop([0], axis=1).drop([0], axis=0)
                                if not cls.verificar_sintese(df_sintese):
                                    verificacoes.append("síntese não preenchida")
                            else: verificacoes.append("tabela de síntese vazia ou mal formatada")
                        except:
                            verificacoes.append("tabela de síntese vazia ou mal formatada")
                        try:
                            if len(df_eixo.index) > 1 and len(df_eixo.columns) > 1:
                                df_eixo = df_eixo.drop([0], axis=1).drop([0], axis=0)
                                if not cls.verificar_eixo(df_eixo):
                                    verificacoes.append("eixo não preenchido")
                            else: verificacoes.append("tabela de postura vazia ou mal formatada")
                        except:
                            verificacoes.append("tabela eixo vazia ou mal formatada")
                        # else:
                        #   verificacoes.append("tabela de síntese/eixo vazia ou mal formatada")

                # Verificar conteúdos e avaliações (procurar em todas as páginas)
                conteudos_found = False
                for page_text in text_content.values():
                    if 'Avaliações:' in page_text:
                        texto_conteudos = page_text.split('Avaliações:')[1]
                        if cls.verificar_eixo(texto_conteudos):
                            conteudos_found = True
                            #break
                        else: verificacoes.append("Conteúdos ou avaliações não preenchidos")
                if not conteudos_found:
                    verificacoes.append("tabela de conteúdos ou avaliações não encontrados")

            except Exception as e:
                verificacoes.append(f"erro ao processar o diário: {str(e)}")

            if verificacoes:
                verificacao = f'{diario} - ❌ ({", ".join(verificacoes)})'
            else:
                verificacao = f'{diario} - ✅'

            print(verificacao)
            resultados.append(verificacao)

        return '\n'.join(resultados)

# classe responsável por verificar os diários do 3 período  
class Check3P:
    
    @staticmethod
    def verificar_presenca_aluno(df_list):
        for df in df_list:
            if 'F' in df.values or 'FF' in df.values:
                return True
        return False

    @staticmethod
    def verificar_indicadores(content):
        return any(i in str(content) for i in ['A', 'B', 'C', 'D', 'RI'])

    @staticmethod
    def verificar_sintese(content):
        indicadores = ['P', 'S', 'I', 'RI', 'RA', 'PD']
        return any(i in str(content) for i in indicadores)

    @staticmethod
    def verificar_eixo(content):
        vogais = ['a', 'e', 'i', 'o']
        return any(v in str(content).lower() for v in vogais)

    @staticmethod
    def extract_tables_from_pdf(pdf_path):
        tables = {}
        try:
            with pdfplumber.open(pdf_path) as pdf:
                for page_num, page in enumerate(pdf.pages, 1):
                    try:
                        page_tables = camelot.read_pdf(pdf_path, pages=str(page_num))
                        if page_tables:
                            tables[page_num] = page_tables
                    except Exception as e:
                        print(f"Erro ao extrair tabelas da página {page_num}: {str(e)}")
        except Exception as e:
            print(f"Erro ao abrir o PDF {pdf_path}: {str(e)}")
        return tables

    @staticmethod
    def extract_text_from_pdf(pdf_path):
        text_content = {}
        with pdfplumber.open(pdf_path) as pdf:
            for page_num, page in enumerate(pdf.pages, 1):
                text_content[page_num] = page.extract_text()
        return text_content

    @classmethod
    def verificacao_geral(cls, diarios: list):
        resultados = []
        for diario in diarios:
            verificacoes = []

            try:
                tables = cls.extract_tables_from_pdf(diario)
                text_content = cls.extract_text_from_pdf(diario)

                if not tables:
                    verificacoes.append("Não foi possível extrair tabelas do PDF")
                else:
                    # Verificar presença de alunos (páginas 2-5)
                    df_list = [table.df.drop([0], axis=1) for page in range(2, 6) for table in tables.get(page, [])]
                    if not df_list:
                        verificacoes.append("Não foi possível encontrar tabelas de presença")
                    elif not cls.verificar_presenca_aluno(df_list):
                        verificacoes.append("faltas não preenchidas")

                    # Verificar indicadores (penúltima página com tabelas)
                    if len(tables) > 1:
                      third_last_page = sorted(tables.keys())[-3] ##
                      #if len(tables[second_last_page]) >= 2:
                      try:
                        df_indicadores = tables[third_last_page][0].df # ISSUE resolver -> resolvido!
                        if len(df_indicadores.index) > 1 and len(df_indicadores.columns) > 1:
                          df_indicadores = df_indicadores.drop([0], axis=1).drop([0], axis=0)
                          if not cls.verificar_indicadores(df_indicadores):
                            verificacoes.append("indicadores não preenchidos")
                        else:
                          verificacoes.append("tabela de indicadores vazia ou mal formatada")
                      except:
                        verificacoes.append("tabela de indicadores vazia ou mal formatada")

                    # Verificar síntese e eixo (última página com tabelas) -> minha versão
                    if len(tables) > 1:
                        second_last_page = sorted(tables.keys())[-2]
                        # verificar se a ultima pag é curriculo adaptado:
                        if 'currículo' in str(tables[second_last_page][0].df.values).lower().split():
                            #print('** CURRICULO ADAPTADO **')
                            second_last_page = sorted(tables.keys())[-2]

                        #if len(math_tables[last_table_page]) >= 2:
                        try:
                            if 'Síntese' in tables[second_last_page][0].df.values:
                                df_sintese = tables[second_last_page][0].df
                            elif 'Síntese' in tables[second_last_page][1].df.values:
                                df_sintese = tables[second_last_page][1].df
                        except:
                            pass #verificacoes.append("tabela de síntese vazia ou mal formatada")
                        try:
                            if 'Eixo de Formação da Postura de Estudante' in tables[second_last_page][0].df.values:
                                df_eixo = tables[second_last_page][0].df
                            elif 'Eixo de Formação da Postura de Estudante' in tables[second_last_page][1].df.values:
                                df_eixo = tables[second_last_page][1].df
                        except:
                            pass #verificacoes.append("tabela de postura vazia ou mal formatada")


                        try:
                            if len(df_sintese.index) > 1 and len(df_sintese.columns) > 1:
                                df_sintese = df_sintese.drop([0], axis=1).drop([0], axis=0)
                                if not cls.verificar_sintese(df_sintese):
                                    verificacoes.append("síntese não preenchida")
                            else: verificacoes.append("tabela de síntese vazia ou mal formatada")
                        except:
                            verificacoes.append("tabela de síntese vazia ou mal formatada")
                        try:
                            if len(df_eixo.index) > 1 and len(df_eixo.columns) > 1:
                                df_eixo = df_eixo.drop([0], axis=1).drop([0], axis=0)
                                if not cls.verificar_eixo(df_eixo):
                                    verificacoes.append("eixo não preenchido")
                            else: verificacoes.append("tabela de postura vazia ou mal formatada")
                        except:
                            verificacoes.append("tabela eixo vazia ou mal formatada")
                        # else:
                        #   verificacoes.append("tabela de síntese/eixo vazia ou mal formatada")
                    

                    # Verificar 4 menção *3 tri* (última página com tabelas)

                    if len(tables) > 1:
                        last_table_page = sorted(tables.keys())[-1]
                        if len(tables[last_table_page]) >= 1:
                            df_4mencao = tables[last_table_page][0].df
                            try:
                                if len(df_4mencao.index) > 1 and len(df_4mencao.columns) > 1:
                                    df_4mencao = df_4mencao.drop([0,1,2,3], axis=1).drop([0], axis=0)
                                    if not cls.verificar_indicadores(df_4mencao):
                                        verificacoes.append("4 menção não preenchida")
                            except:
                                verificacoes.append("Tabela de resultados finais vazia/mal formatada")
                        else:
                            verificacoes.append("Tabela de resultados finais vazia/mal formatada")

                # Verificar conteúdos e avaliações (procurar em todas as páginas)
                conteudos_found = False
                for page_text in text_content.values():
                    if 'Avaliações:' in page_text:
                        texto_conteudos = page_text.split('Avaliações:')[1]
                        if cls.verificar_eixo(texto_conteudos):
                            conteudos_found = True
                            #break
                        else: verificacoes.append("Conteúdos ou avaliações não preenchidos")
                if not conteudos_found:
                    verificacoes.append("tabela de conteúdos ou avaliações não encontrados")

            except Exception as e:
                verificacoes.append(f"erro ao processar o diário: {str(e)}")

            if verificacoes:
                verificacao = f'{diario} - ❌ ({", ".join(verificacoes)})'
            else:
                verificacao = f'{diario} - ✅'

            print(verificacao)
            resultados.append(verificacao)

        return '\n'.join(resultados)

caminho_local = os.getcwd() # captura o local path, necessário para o funcionamento atual do script 

#lista_diarios = []
# Faz a leitura de todos os arquivos pdf no diretório capturado onde estão os diários desejados para a análise
# e armazena na variável *diarios.
try:
    arquivos = f'{caminho_local}//*.pdf'
    diarios = glob.glob(arquivos)
    # for d in diarios:
    #     lista_diarios.append(d)
except Exception as e3:
    print(f'erro: {e3}')

# cria variável contendo arquivo de texto a ser criado no mesmo diretório capturado.
criar_txt = f'{caminho_local}//diarios verificados.txt' 

try: # cria o txt escrevendo ou reescrevendo o resultado das verificações dos diários e cria um iterável com with open
    with open(criar_txt, 'w+', encoding='utf-8') as arquivo: 
        checked = Check3P.verificacao_geral(diarios) # passa para a função da classe a lista dos diários e armazena o resultado
        arquivo.write(checked) # passa o resultado das verificações como argumento a ser escrito no txt
except Exception as e4:
    print(f'erro: {e4}')

os.startfile(criar_txt) # abre o relatório criado em txt