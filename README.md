# Downloader Automático de Diários do Sistema HE + Verificador de Diários Escolares

Este projeto Python facilita o download de diários de classe do Sistema HE, automatizando o processo de login e download para várias turmas. Chega de clicar em um monte de links! 🎉
E juntamente com o Script de Verificação dos Diários, feito também em Python, que verifica e valida os diários escolares em PDF, garantindo que informações essenciais como faltas, indicadores, sínteses e avaliações estejam preenchidas, retornando ao usuário um relatório indicando quais tabelas não foram preenchidas. Ele automatiza o processo de verificação, poupando tempo e esforço. 🚀

## Como surgiu 🧐

Considero este como sendo o meu primeiro grande projeto solo em desenvolvimento, que idealizei enquanto trilhava meus primeiros passos na programação estudando Python.
O projeto foi criado pensando na rotina do meu atual gestor na empresa onde trabalho como Analista de Suporte, onde ele precisa durante o final de cada trimestre baixar diversos arquivos em PDF de um sistema interno, são ao todo, cerca de 170 arquivos de PDF.
Há muito o que melhorar ainda, eu sei, mas tenho orgulho desse primeiro projeto, como sendo meu primeiro passo nesse universo do desenvolvimento, aprendi muitos conceitos que talvez levaria mais tempo para assimilar se estudasse de forma convencional, o que me fez entender o poder de aplicar o conhecimento na prática com desafios reais, para resolver problemas reais.

## Downloader Automático ⏬
### Como Funciona ⚙️

O script usa o `Selenium` para automatizar um navegador web (Chrome), fazer login no Sistema HE e baixar os diários em PDF para cada turma selecionada. Ele organiza os arquivos baixados em pastas separadas por turma dentro de um diretório escolhido pelo usuário.

**Passo a passo:**

1. **Seleção do Destino:** Uma caixa de diálogo solicita ao usuário que escolha o diretório onde os diários serão salvos.
2. **Login Automático:** O script acessa o Sistema HE e faz login com as credenciais fornecidas (*atualmente fixas no código, idealmente, seriam parametrizáveis ou solicitadas ao usuário*). O navegador é minimizado durante esse processo.
3. **Seleção das Turmas:** Uma interface gráfica com caixas de seleção (checkboxes) permite ao usuário escolher quais turmas deseja baixar os diários ou selecionar todas de uma vez.
4. **Download e Organização:** Após a seleção, o script baixa os diários de cada turma selecionada, usando links predefinidos. Os PDFs são salvos na pasta de Downloads do usuário e, em seguida, movidos para as pastas correspondentes às turmas dentro do diretório escolhido no primeiro passo.
5. **Finalização:** Uma mensagem de aviso informa ao usuário que o processo foi concluído.

## Verificador de Diários (checker) 🔎 
### Como funciona ⚙️

Atualmente, existem duas versões, a primeira desenvolvida em python, e a mais recente em Javascript e depois exportada como uma versão Desktop utilizando Electron.
O script python utiliza as bibliotecas `pdfplumber`, `PyPDF` e `camelot` para extrair tabelas e texto dos PDFs dos diários. Em seguida, aplica uma série de verificações para garantir que os campos obrigatórios estejam preenchidos corretamente. Os resultados da verificação são salvos em um arquivo de texto. 
Já na versão Web com Javascript, ele usa bibliotecas de leitura para PDFs compatíveis com a linguagem, além de visuais estilizados com CSS e HTML para abrir em uma página web para melhorar a experiência do usuário.

**Passo a passo:**

1. **Extração de Dados:** O script extrai tabelas e texto de cada página do PDF do diário.
2. **Verificação de Presença:** Verifica se as faltas dos alunos foram marcadas nas tabelas de presença (páginas 2-5).
3. **Verificação de Indicadores:** Verifica se os indicadores (A, B, C, D, RI) foram preenchidos na penúltima página com tabelas.
4. **Verificação de Síntese e Eixo:** Verifica se a síntese e o eixo de formação foram preenchidos na última página com tabelas (com tratamento especial para currículos adaptados).
5. **Verificação de Conteúdos e Avaliações:** Verifica se os conteúdos e avaliações foram preenchidos, buscando por "Avaliações:" em todas as páginas.
6. **Geração de Relatório:** Os resultados da verificação são exibidos no console e salvos em um arquivo TXT chamado "diarios verificados.txt" no diretório atual. O arquivo é aberto automaticamente após a execução do script (versão python).

## Tecnologias e Bibliotecas Utilizadas 📚

* **Javascript/CSS/HTML:** Linguagem de programação principal.
* **Python:** Linguagem de programação principal.
* **Selenium:** Para automatizar a interação com o navegador web.
* **WebDriverManager:** Para gerenciar automaticamente o driver do Chrome.
* **Tkinter:** Para criar a interface gráfica com caixas de seleção.
* **Pathlib/OS/Glob:** Para manipulação de arquivos, caminhos de arquivos e diretórios.
* **Pdfplumber:** Para extrair texto e tabelas de PDFs.
* **Camelot:** Uma biblioteca para extração de tabelas em PDF.
* **Pandas:** Famosa biblioteca para manipulação de Data Frames.

## Possíveis Melhorias 🛠️

Downloader ⏬
* **Credenciais de Login:** Implementar a entrada de usuário e senha para maior segurança.
* **Links Dinâmicos:** Buscar os links de download dinamicamente, em vez de usar links fixos, para maior flexibilidade e adaptação a mudanças no Sistema HE.
* **Tratamento de Erros:** Aprimorar o tratamento de erros para lidar com possíveis problemas, como falha no login ou links inválidos.
* **Interface Gráfica:** Aperfeiçoar a interface gráfica, tornando-a mais intuitiva e visualmente agradável.
* **Configurações:** Permitir ao usuário configurar opções como o navegador a ser usado e o tempo de espera entre os downloads.

Verificador de Diários 🔎
* **Tratamento de Erros:** Aprimorar o tratamento de erros para fornecer mensagens mais informativas e lidar com diferentes tipos de PDFs.
* **Flexibilidade:** Tornar o script mais flexível para lidar com diferentes formatos de diários, permitindo ao usuário configurar as páginas e campos a serem verificados. Podendo aqui ser incluído um método usando alguma IA para ler os PDFs.
* **Relatórios Mais Detalhados:** Gerar relatórios mais detalhados, incluindo informações sobre as linhas e colunas específicas com problemas.

## Contribuições 🤝

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

