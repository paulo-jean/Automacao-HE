import camelot
import pdfplumber
#from ghostscript import Ghostscript
import pandas as pd

class Check:

    def verificar_presenca_aluno(df_list):
        for df in df_list:
            if 'F' or 'FF' in df.values:
                return True

        return False

    def verificar_indicadores(content):
        l = ['A','B','C','D']
        for i in l:
            if i in str(content):
                return True
            else:
                return False

    def verificar_sintese(content):
        indicadores = ['P','S','I','RI','RA','PD']
        for i in indicadores:
            if i in str(content):
                return True
            else:
                return False

    def verificar_eixo(content):
        ''' vogais '''
        vogais = ['a','e','i','o']
        for v in vogais:
            if v in str(content):
                return True
            else:
                return False

    def verificacao_geral(diarios: list):
        resultados = []
        for diario in diarios:
            verificacoes = []
            
            try:
                pagina_oito = camelot.read_pdf(diario, pages='8')
                df8_eixo = pagina_oito[1].df
                df8_eixo = df8_eixo.drop([0], axis=1)
                df8_sintese = pagina_oito[0].df
                df8_sintese = df8_sintese.drop([0], axis=1)
                df8_sintese = df8_sintese.drop([0,1], axis=0)
                resultado_sintese = Check.verificar_sintese(df8_sintese)
                resultado_eixo = Check.verificar_eixo(df8_eixo)
                if not resultado_sintese:
                    verificacoes.append("síntese não preenchida")
                if not resultado_eixo:
                    verificacoes.append("eixo não preenchido")
            except:
                verificacoes.append("erro ao verificar síntese e eixo")

            try:
                pagina_sete = camelot.read_pdf(diario, pages='7')
                df7 = pagina_sete[0].df
                df7 = df7.drop([0], axis=1)
                df7 = df7.drop([0], axis=0)
                resultado_indicadores = Check.verificar_indicadores(df7)
                if not resultado_indicadores:
                    verificacoes.append("indicadores não preenchidos")
            except:
                verificacoes.append("erro ao verificar indicadores")

            try:
                pagina_seis = pdfplumber.open(diario).pages[5]
                texto_pag6 = pagina_seis.extract_text().split('Avaliações:')[1]
                resultado_conteudos = Check.verificar_eixo(texto_pag6)
                if not resultado_conteudos:
                    verificacoes.append("conteúdos ou avaliações não preenchidos")
            except:
                verificacoes.append("erro ao verificar conteúdos/avaliações")

            pages = camelot.read_pdf(diario, pages='2-4')
            df2 = [page.df.drop([0], axis=1) for page in pages]
            resultado_faltas = Check.verificar_presenca_aluno(df2)

            if not resultado_faltas:
                verificacoes.append("faltas não preenchidas")

            if verificacoes:
                verificacao = f'{diario} - ❌ ({", ".join(verificacoes)})'
            else:
                verificacao = f'{diario} - ✅'

            print(verificacao)
            resultados.append(verificacao)
        return '\n'.join(resultados)

class Check2P:

    def verificar_presenca_aluno(df_list):
        for df in df_list:
            if 'F' or 'FF' in df.values:
                return True

        return False

    def verificar_indicadores(content):
        l = ['A','B','C','D']
        for i in l:
            if i in str(content):
                return True
            else:
                return False

    def verificar_sintese(content):
        indicadores = ['P','S','I','RI','RA','PD']
        for i in indicadores:
            if i in str(content):
                return True
            else:
                return False

    def verificar_eixo(content):
        ''' vogais '''
        vogais = ['a','e','i','o']
        for v in vogais:
            if v in str(content):
                return True
            else:
                return False

    def verificacao_geral(diarios: list):
        resultados = []
        for diario in diarios:
            verificacoes = []
            
            try:
                pagina_oito = camelot.read_pdf(diario, pages='8')
                df8_eixo = pagina_oito[1].df
                df8_eixo = df8_eixo.drop([0], axis=1)
                df8_sintese = pagina_oito[0].df
                df8_sintese = df8_sintese.drop([0], axis=1)
                df8_sintese = df8_sintese.drop([0,1], axis=0)
                resultado_sintese = Check2P.verificar_sintese(df8_sintese)
                resultado_eixo = Check2P.verificar_eixo(df8_eixo)
                if not resultado_sintese:
                    verificacoes.append("síntese não preenchida")
                if not resultado_eixo:
                    verificacoes.append("eixo não preenchido")
            except:
                verificacoes.append("erro ao verificar síntese e eixo")

            try:
                pagina_sete = camelot.read_pdf(diario, pages='7')
                df7 = pagina_sete[0].df
                df7 = df7.drop([0], axis=1)
                df7 = df7.drop([0], axis=0)
                resultado_indicadores = Check2P.verificar_indicadores(df7)
                if not resultado_indicadores:
                    verificacoes.append("indicadores não preenchidos")
            except:
                verificacoes.append("erro ao verificar indicadores")

            try:
                pagina_seis = pdfplumber.open(diario).pages[5]
                texto_pag6 = pagina_seis.extract_text().split('Avaliações:')[1]
                resultado_conteudos = Check2P.verificar_eixo(texto_pag6)
                if not resultado_conteudos:
                    verificacoes.append("conteúdos ou avaliações não preenchidos")
            except:
                verificacoes.append("erro ao verificar conteúdos/avaliações")

            pages = camelot.read_pdf(diario, pages='2-5')
            df2 = [page.df.drop([0], axis=1) for page in pages]
            resultado_faltas = Check2P.verificar_presenca_aluno(df2)

            if not resultado_faltas:
                verificacoes.append("faltas não preenchidas")

            if verificacoes:
                verificacao = f'{diario} - ❌ ({", ".join(verificacoes)})'
            else:
                verificacao = f'{diario} - ✅'

            print(verificacao)
            resultados.append(verificacao)
        return '\n'.join(resultados)

class Check3P:

    def verificar_presenca_aluno(df_list):
        for df in df_list:
            if 'F' or 'FF' in df.values:
                return True

        return False

    def verificar_indicadores(content):
        l = ['A','B','C','D']
        for i in l:
            if i in str(content):
                return True
            else:
                return False

    def verificar_sintese(content):
        indicadores = ['P','S','I','RI','RA','PD']
        for i in indicadores:
            if i in str(content):
                return True
            else:
                return False

    def verificar_eixo(content):
        ''' vogais '''
        vogais = ['a','e','i','o']
        for v in vogais:
            if v in str(content):
                return True
            else:
                return False

    def verificacao_geral(diarios: list):
        resultados = []
        for diario in diarios:
            verificacoes = []
            
            try:
                pagina_nove = camelot.read_pdf(diario, pages='9')
                df9 = pagina_nove[0].df
                df9 = df9.drop([0,1,2], axis=1)
                df9 = df9.drop([0], axis=0)
                resultado_indicadores_4mencao = Check3P.verificar_indicadores(df9)
                if not resultado_indicadores_4mencao:
                    verificacoes.append("4ª menção não preenchida")
            except:
                verificacoes.append("erro ao verificar os Resultados Finais")
            
            try:
                pagina_oito = camelot.read_pdf(diario, pages='8')
                df8_eixo = pagina_oito[1].df
                df8_eixo = df8_eixo.drop([0], axis=1)
                df8_sintese = pagina_oito[0].df
                df8_sintese = df8_sintese.drop([0], axis=1)
                df8_sintese = df8_sintese.drop([0,1], axis=0)
                resultado_sintese = Check3P.verificar_sintese(df8_sintese)
                resultado_eixo = Check3P.verificar_eixo(df8_eixo)
                if not resultado_sintese:
                    verificacoes.append("síntese não preenchida")
                if not resultado_eixo:
                    verificacoes.append("eixo não preenchido")
            except:
                verificacoes.append("erro ao verificar síntese e eixo")

            try:
                pagina_sete = camelot.read_pdf(diario, pages='7')
                df7 = pagina_sete[0].df
                df7 = df7.drop([0], axis=1)
                df7 = df7.drop([0], axis=0)
                resultado_indicadores = Check3P.verificar_indicadores(df7)
                if not resultado_indicadores:
                    verificacoes.append("indicadores não preenchidos")
            except:
                verificacoes.append("erro ao verificar indicadores")

            try:
                pagina_seis = pdfplumber.open(diario).pages[5]
                texto_pag6 = pagina_seis.extract_text().split('Avaliações:')[1]
                resultado_conteudos = Check3P.verificar_eixo(texto_pag6)
                if not resultado_conteudos:
                    verificacoes.append("conteúdos ou avaliações não preenchidos")
            except:
                verificacoes.append("erro ao verificar conteúdos/avaliações")

            pages = camelot.read_pdf(diario, pages='2-5')
            df2 = [page.df.drop([0], axis=1) for page in pages]
            resultado_faltas = Check3P.verificar_presenca_aluno(df2)

            if not resultado_faltas:
                verificacoes.append("faltas não preenchidas")

            if verificacoes:
                verificacao = f'{diario} - ❌ ({", ".join(verificacoes)})'
            else:
                verificacao = f'{diario} - ✅'

            print(verificacao)
            resultados.append(verificacao)
        return '\n'.join(resultados)


