// Classe responsável por verificar os diários do 2 período
class Check2P {
    // Verifica se há faltas (F ou FF) nos valores
    static verificarPresencaAluno(tables) {
        if (!tables || tables.length === 0) {
            return false;
        }
        
        for (const table of tables) {
            if (table.some(row => row.some(cell => 
                cell === 'F' || cell === 'FF'))) {
                return true;
            }
        }
        return false;
    }

    // Verifica se há marcações nas colunas de indicadores (ignorando a primeira coluna e duas primeiras linhas)
    static verificarIndicadores(table) {
        if (!table || table.length < 3) return false;
        
        // Examina a partir da terceira linha (índice 2)
        for (let i = 2; i < table.length; i++) {
            const row = table[i];
            // Ignora a primeira coluna (índice 0) e verifica se há alguma marcação nas demais colunas
            if (row && row.length > 1) {
                for (let j = 1; j < row.length; j++) {
                    // Verifica se há uma marcação específica (como "x", "X", "✓") 
                    // Só considera strings não vazias com características de marcação
                    const cell = row[j];
                    if (cell && typeof cell === 'string') {
                        const trimmed = cell.trim();
                        if (trimmed !== '' && 
                            (trimmed === 'P' || trimmed === 'S' || 
                             trimmed === 'I' || trimmed === 'RI' || 
                             trimmed === 'RA' || trimmed === 'PD' ||
                             trimmed === 'A' || trimmed === 'B' || 
                             trimmed === 'C' || trimmed === 'D')) {
                            return true;
                        }
                    }
                }
            }
        }
        return false;
    }

    // Verifica se há marcações nas colunas da síntese (ignorando a primeira coluna)
    static verificarSintese(table) {
        if (!table || table.length < 3) return false;
        
        // Verifica as colunas que devem ter marcações: "AU", "APS", "RCS" ou outras
        // Determina primeiro quais colunas são para marcações (a partir da coluna 1)
        let colsToCheck = [];
        
        // Se a tabela tiver cabeçalhos "AU", "APS", "RCS" ou similares
        if (table.length > 1 && table[1] && table[1].length > 1) {
            for (let j = 1; j < table[1].length; j++) {
                const headerCell = table[1][j];
                if (headerCell && typeof headerCell === 'string' && headerCell.trim() !== '') {
                    colsToCheck.push(j);
                }
            }
        } else {
            // Caso não encontre cabeçalhos, verifica todas as colunas após a primeira
            for (let j = 1; j < (table[0] ? table[0].length : 0); j++) {
                colsToCheck.push(j);
            }
        }
        
        // Examina as linhas começando da terceira (índice 2)
        for (let i = 2; i < table.length; i++) {
            const row = table[i];
            if (!row || row.length <= 1) continue;
            
            // Verifica apenas as colunas determinadas anteriormente
            for (const j of colsToCheck) {
                if (j >= row.length) continue;
                
                const cell = row[j];
                if (cell && typeof cell === 'string') {
                    const trimmed = cell.trim();
                    if (trimmed !== '' && 
                        (trimmed === 'P' || trimmed === 'S' || 
                         trimmed === 'RI' || trimmed === 'RA' ||
                         trimmed === 'PD' || trimmed === 'I' ||
                         /[A-Z]/.test(trimmed))) {
                        return true;
                    }
                }
            }
        }
        return false;
    }

    // Verifica se há texto nas células da tabela Postura do Estudante (ignorando a primeira linha e coluna)
    static verificarEixoPostura(table) {
        if (!table || table.length < 2) return false;
        
        // Examina a partir da segunda linha (índice 1)
        for (let i = 1; i < table.length; i++) {
            const row = table[i];
            // Ignora a primeira coluna (índice 0) e verifica se há texto nas demais colunas
            if (row && row.length > 1) {
                for (let j = 1; j < row.length; j++) {
                    // Verifica se há texto significativo (não apenas espaços ou caracteres isolados)
                    if (row[j] && typeof row[j] === 'string') {
                        const trimmed = row[j].trim();
                        // Verifica se é um texto com mais de um caractere ou um número
                        if (trimmed.length > 1 || /\d/.test(trimmed)) {
                            return true;
                        }
                    }
                }
            }
        }
        return false;
    }

    // Verifica se há texto com vogais (para conteúdo)
    static verificarEixo(content) {
        if (!content) return false;
        
        const vogais = ['a', 'e', 'i', 'o', 'u'];
        const contentLower = content.toLowerCase();
        return vogais.some(v => contentLower.includes(v));
    }

    // Extrai tabelas do PDF usando PDF.js
    static async extractTablesFromPdf(pdfFile) {
        try {
            const arrayBuffer = await pdfFile.arrayBuffer();
            const pdf = await pdfjsLib.getDocument({ data: arrayBuffer }).promise;
            
            const tables = {};
            
            // Processar cada página
            for (let pageNum = 1; pageNum <= pdf.numPages; pageNum++) {
                try {
                    const page = await pdf.getPage(pageNum);
                    const textContent = await page.getTextContent();
                    
                    // Identificar potenciais tabelas baseado no layout do texto
                    // Implementação simplificada, pois camelot não existe em JS
                    const items = textContent.items;
                    
                    // Agrupar por Y para identificar linhas
                    const rows = {};
                    for (const item of items) {
                        const y = Math.round(item.transform[5]); // Y position
                        
                        if (!rows[y]) {
                            rows[y] = [];
                        }
                        
                        rows[y].push(item.str);
                    }
                    
                    // Converter para formato de tabela (array de arrays)
                    const tableData = Object.values(rows).map(row => row);
                    
                    if (tableData.length > 0) {
                        if (!tables[pageNum]) {
                            tables[pageNum] = [];
                        }
                        tables[pageNum].push(tableData);
                    }
                } catch (e) {
                    console.error(`Erro ao processar página ${pageNum}:`, e);
                }
            }
            
            return tables;
        } catch (e) {
            console.error('Erro ao extrair tabelas:', e);
            return {};
        }
    }

    // Extrai texto do PDF usando PDF.js
    static async extractTextFromPdf(pdfFile) {
        try {
            const arrayBuffer = await pdfFile.arrayBuffer();
            const pdf = await pdfjsLib.getDocument({ data: arrayBuffer }).promise;
            
            const textContent = {};
            
            // Para cada página do PDF
            for (let pageNum = 1; pageNum <= pdf.numPages; pageNum++) {
                try {
                    const page = await pdf.getPage(pageNum);
                    const content = await page.getTextContent();
                    
                    // Concatenar todo o texto da página
                    textContent[pageNum] = content.items.map(item => item.str).join(' ');
                } catch (e) {
                    console.error(`Erro ao extrair texto da página ${pageNum}:`, e);
                    textContent[pageNum] = "";
                }
            }
            
            return textContent;
        } catch (e) {
            if (e.name === 'PasswordException') {
                return { error: `PDF ${pdfFile.name} criptografado e senha incorreta/não fornecida.` };
            }
            return { error: `Erro geral ao abrir/ler texto do PDF ${pdfFile.name}: ${e.message}` };
        }
    }

    // Método auxiliar para debugging - exibe conteúdo de tabelas encontradas
    static logTableInfo(tables, titulo) {
        console.log(`--- Tabela: ${titulo} ---`);
        if (tables && tables.length > 0) {
            for (let i = 0; i < tables.length; i++) {
                console.log(`Tabela #${i+1}:`);
                const table = tables[i];
                for (let j = 0; j < Math.min(table.length, 10); j++) {
                    console.log(`  Linha ${j}: ${JSON.stringify(table[j])}`);
                }
                if (table.length > 10) console.log("  ...");
            }
        } else {
            console.log("Nenhuma tabela encontrada");
        }
    }

    // Método principal que coordena a verificação
    static async verificacaoGeral(diarios, progressCallback, cancelToken) {
        const resultadosFinais = {};
        const totalDiarios = diarios.length;

        for (let i = 0; i < diarios.length; i++) {
            // Verifica se o cancelamento foi solicitado
            if (cancelToken.cancelled) {
                progressCallback({ status: "cancelled" });
                return null;
            }

            const diario = diarios[i];
            const nomeDiario = diario.name;
            
            // Reporta progresso
            progressCallback({
                processed: i,
                total: totalDiarios,
                filename: nomeDiario,
                status: "processing"
            });

            let statusDiario = {
                "Faltas": '❓',
                "Indicadores (Conceitos)": '❓',
                "Síntese": '❓',
                "Postura do Estudante": '❓',
                "Conteúdo desenvolvido em aula": '❓',
                "Avaliações": '❓',
                "Observações": ""
            };

            try {
                // Adiciona um pequeno delay para não congelar a interface
                await new Promise(resolve => setTimeout(resolve, 50));

                // Extrai tabelas e texto do PDF
                const tables = await this.extractTablesFromPdf(diario);
                const textContent = await this.extractTextFromPdf(diario);

                // Verifica se houve erro na extração de texto
                if (textContent && textContent.error) {
                    for (const key in statusDiario) {
                        if (key !== "Observações") {
                            statusDiario[key] = '❌';
                        }
                    }
                    statusDiario["Observações"] = textContent.error;
                    resultadosFinais[nomeDiario] = statusDiario;
                    
                    progressCallback({
                        processed: i + 1,
                        total: totalDiarios,
                        filename: nomeDiario,
                        status: "file_done"
                    });
                    continue;
                }

                // Verificação de Tabelas
                if (!tables || Object.keys(tables).length === 0) {
                    statusDiario["Observações"] = "Erro: Não foi possível extrair tabelas do PDF.";
                    statusDiario["Faltas"] = '❌';
                    statusDiario["Indicadores (Conceitos)"] = '❌';
                    statusDiario["Síntese"] = '❌';
                    statusDiario["Postura do Estudante"] = '❌';
                } else {
                    // Verificação de presença (Faltas)
                    try {
                        const dfListPresenca = [];
                        for (let page = 2; page <= 5; page++) {
                            if (tables[page]) {
                                dfListPresenca.push(...tables[page]);
                            }
                        }

                        if (dfListPresenca.length === 0) {
                            statusDiario["Faltas"] = '❓';
                            statusDiario["Observações"] += " Nenhuma tabela de presença encontrada. ";
                        } else if (this.verificarPresencaAluno(dfListPresenca)) {
                            statusDiario["Faltas"] = '✅';
                        } else {
                            statusDiario["Faltas"] = '❌';
                            statusDiario["Observações"] += " - Nenhuma falta lançada OU todos alunos presentes. Confirme com o Profº. ";
                        }
                    } catch (e) {
                        statusDiario["Faltas"] = '❌';
                        statusDiario["Observações"] += ` Erro ao verificar faltas: ${e.message}. `;
                    }

                    // Lógica para verificar páginas com tabelas
                    const paginasComTabelas = Object.keys(tables).map(Number).sort((a, b) => a - b);
                    let lastTablePageNum = null;
                    let secondLastPageNum = null;

                    if (paginasComTabelas.length >= 1) {
                        lastTablePageNum = paginasComTabelas[paginasComTabelas.length - 1];
                        
                        try {
                            let isAdaptado = false;
                            if (tables[lastTablePageNum]) {
                                for (const tbl of tables[lastTablePageNum]) {
                                    const tblStr = JSON.stringify(tbl);
                                    if (tblStr.toLowerCase().includes('currículo')) {
                                        isAdaptado = true;
                                        break;
                                    }
                                }
                            }
                            
                            if (isAdaptado && paginasComTabelas.length > 1) {
                                lastTablePageNum = paginasComTabelas[paginasComTabelas.length - 2];
                                if (paginasComTabelas.length > 2) {
                                    secondLastPageNum = paginasComTabelas[paginasComTabelas.length - 3];
                                }
                            } else if (paginasComTabelas.length > 1) {
                                secondLastPageNum = paginasComTabelas[paginasComTabelas.length - 2];
                            }
                        } catch (e) {
                            if (paginasComTabelas.length > 1) {
                                secondLastPageNum = paginasComTabelas[paginasComTabelas.length - 2];
                            }
                        }

                        // Verificar indicadores
                        if (secondLastPageNum !== null && tables[secondLastPageNum]) {
                            try {
                                // Busca pela tabela que contém "Indicadores" ou "Conceitos"
                                let dfIndicadores = null;
                                for (const table of tables[secondLastPageNum]) {
                                    const tableStr = JSON.stringify(table);
                                    if (tableStr.toLowerCase().includes('indicadores') || 
                                        tableStr.toLowerCase().includes('conceitos')) {
                                        dfIndicadores = table;
                                        break;
                                    }
                                }
                                
                                if (dfIndicadores && dfIndicadores.length > 2) {
                                    // Adiciona log para debug
                                    console.log("Verificando tabela de indicadores:");
                                    console.log(JSON.stringify(dfIndicadores.slice(0, 5)));
                                    
                                    if (this.verificarIndicadores(dfIndicadores)) {
                                        statusDiario["Indicadores (Conceitos)"] = '✅';
                                    } else {
                                        statusDiario["Indicadores (Conceitos)"] = '❌';
                                    }
                                } else {
                                    statusDiario["Indicadores (Conceitos)"] = '❌';
                                }
                            } catch (e) {
                                statusDiario["Indicadores (Conceitos)"] = '❌';
                                statusDiario["Observações"] += ` Erro ao processar tabela de indicadores: ${e.message}. `;
                            }
                        } else {
                            if (paginasComTabelas.length > 1) {
                                statusDiario["Indicadores (Conceitos)"] = '❓';
                                statusDiario["Observações"] += " Não foi possível localizar/processar a página de indicadores. ";
                            } else {
                                statusDiario["Indicadores (Conceitos)"] = 'N/A';
                            }
                        }

                        // Verificar síntese e eixo
                        if (lastTablePageNum !== null && tables[lastTablePageNum]) {
                            let dfSintese = null;
                            let dfEixo = null;
                            
                            try {
                                for (const table of tables[lastTablePageNum]) {
                                    const tableStr = JSON.stringify(table);
                                    if (tableStr.includes('Síntese')) {
                                        dfSintese = table;
                                    }
                                    if (tableStr.includes('Eixo de Formação da Postura')) {
                                        dfEixo = table;
                                    }
                                }
                                
                                // Verificar síntese - usando método melhorado
                                if (dfSintese) {
                                    // Adiciona log para debug
                                    console.log("Verificando tabela de síntese:");
                                    console.log(JSON.stringify(dfSintese.slice(0, 5)));
                                    
                                    if (dfSintese.length > 2) {
                                        if (this.verificarSintese(dfSintese)) {
                                            statusDiario["Síntese"] = '✅';
                                        } else {
                                            statusDiario["Síntese"] = '❌';
                                        }
                                    } else {
                                        statusDiario["Síntese"] = '❌';
                                    }
                                } else {
                                    statusDiario["Síntese"] = '❌';
                                    statusDiario["Observações"] += " - Tabela 'Síntese' não encontrada. ";
                                }
                                
                                // Verificar eixo (postura)
                                if (dfEixo) {
                                    // Adiciona log para debug
                                    console.log("Verificando tabela de postura:");
                                    console.log(JSON.stringify(dfEixo.slice(0, 5)));
                                    
                                    if (dfEixo.length > 1) {
                                        if (this.verificarEixoPostura(dfEixo)) {
                                            statusDiario["Postura do Estudante"] = '✅';
                                        } else {
                                            statusDiario["Postura do Estudante"] = '❌';
                                        }
                                    } else {
                                        statusDiario["Postura do Estudante"] = '❌';
                                    }
                                } else {
                                    statusDiario["Postura do Estudante"] = '❌';
                                    statusDiario["Observações"] += " - Tabela 'Eixo de Formação da Postura' não encontrada. ";
                                }
                                
                            } catch (e) {
                                statusDiario["Síntese"] = '❌';
                                statusDiario["Postura do Estudante"] = '❌';
                                statusDiario["Observações"] += ` Erro ao processar tabelas de Síntese/Postura: ${e.message}. `;
                            }
                        } else {
                            statusDiario["Síntese"] = '❓';
                            statusDiario["Postura do Estudante"] = '❓';
                            if (paginasComTabelas.length > 0) {
                                statusDiario["Observações"] += " Não foi possível localizar/processar a página de Síntese/Postura. ";
                            }
                        }
                        
                    } else {
                        statusDiario["Indicadores (Conceitos)"] = 'N/A';
                        statusDiario["Síntese"] = 'N/A';
                        statusDiario["Postura do Estudante"] = 'N/A';
                        if (statusDiario["Observações"] === "") {
                            statusDiario["Observações"] += " Erro: Nenhuma tabela encontrada no PDF. ";
                        }
                    }
                }

                // Verificação de Texto
                if (!textContent || Object.keys(textContent).length === 0) {
                    statusDiario["Conteúdo desenvolvido em aula"] = '❌';
                    statusDiario["Avaliações"] = '❌';
                    if (statusDiario["Observações"] === "") {
                        statusDiario["Observações"] = "Erro: Não foi possível extrair texto do PDF.";
                    } else if (!statusDiario["Observações"].includes("Erro")) {
                        statusDiario["Observações"] += " Erro na extração de texto. ";
                    }
                } else {
                    try {
                        // Concatenar todo o texto das páginas
                        const fullText = Object.values(textContent).filter(Boolean).join('\n');
                        const contentLower = fullText.toLowerCase();
                        
                        // Verificar conteúdo desenvolvido em aula
                        let conteudoPreenchido = false;
                        const contentMarker = "conteúdo desenvolvido em aula:";
                        const evaluationMarker = "avaliações:";
                        const diaryMarker = "diário de classe";
                        
                        const contentStartIndex = contentLower.indexOf(contentMarker);
                        
                        if (contentStartIndex !== -1) {
                            const contentTextStart = contentStartIndex + contentMarker.length;
                            const evaluationStartIndex = contentLower.indexOf(evaluationMarker, contentTextStart);
                            
                            const contentTextEnd = evaluationStartIndex !== -1 ? evaluationStartIndex : contentLower.length;
                            const conteudo = fullText.substring(contentTextStart, contentTextEnd).trim();
                            
                            if (this.verificarEixo(conteudo)) {
                                conteudoPreenchido = true;
                            }
                        }
                        
                        // Verificar avaliações
                        let avaliacoesPreenchidas = false;
                        const evaluationStartIndexGlobal = contentLower.indexOf(evaluationMarker);
                        
                        if (evaluationStartIndexGlobal !== -1) {
                            const evaluationTextStart = evaluationStartIndexGlobal + evaluationMarker.length;
                            const diaryStartIndex = contentLower.indexOf(diaryMarker, evaluationTextStart);
                            
                            const evaluationTextEnd = diaryStartIndex !== -1 ? diaryStartIndex : contentLower.length;
                            const avaliacoes = fullText.substring(evaluationTextStart, evaluationTextEnd).trim();
                            
                            if (this.verificarEixo(avaliacoes)) {
                                avaliacoesPreenchidas = true;
                            }
                        }
                        
                        statusDiario["Conteúdo desenvolvido em aula"] = conteudoPreenchido ? '✅' : '❌';
                        statusDiario["Avaliações"] = avaliacoesPreenchidas ? '✅' : '❌';
                        
                    } catch (e) {
                        statusDiario["Conteúdo desenvolvido em aula"] = '❌';
                        statusDiario["Avaliações"] = '❌';
                        statusDiario["Observações"] += ` Erro ao processar conteúdo/avaliações do texto: ${e.message}. `;
                    }
                }
                
            } catch (e) {
                for (const key in statusDiario) {
                    if (key !== "Observações") {
                        statusDiario[key] = '❌';
                    }
                }
                statusDiario["Observações"] = `ERRO GERAL ao processar o diário ${nomeDiario}: ${e.message}`;
            }
            
            statusDiario["Observações"] = statusDiario["Observações"].trim();
            resultadosFinais[nomeDiario] = statusDiario;
            
            // Reporta que este arquivo terminou
            progressCallback({
                processed: i + 1,
                total: totalDiarios,
                filename: nomeDiario,
                status: "file_done"
            });
        }
        
        // Sinaliza conclusão (se não foi cancelado antes)
        if (!cancelToken.cancelled) {
            progressCallback({ status: "completed" });
            return resultadosFinais;
        } else {
            return null;
        }
    }
}

// Configuração do worker do PDF.js
pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.4.120/pdf.worker.min.js';
