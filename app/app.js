// Elementos da interface
const fileInput = document.getElementById('file-input');
const selectedFilesDiv = document.getElementById('selected-files');
const startButton = document.getElementById('start-btn');
const resultsContainer = document.getElementById('results-container');
const resultsContent = document.getElementById('results-content');
const downloadReportBtn = document.getElementById('download-report-btn');
const newCheckBtn = document.getElementById('new-check-btn');

// Instanciar o gerenciador de progresso
const progressWindow = new ProgressWindow();

// Variáveis globais
let selectedFiles = [];

// Evento para seleção de arquivos
fileInput.addEventListener('change', (event) => {
    const files = event.target.files;
    
    if (files.length === 0) {
        selectedFilesDiv.innerHTML = '<p>Nenhum arquivo selecionado</p>';
        startButton.disabled = true;
        return;
    }
    
    // Filtrar apenas arquivos PDF
    selectedFiles = Array.from(files).filter(file => file.type === 'application/pdf');
    
    if (selectedFiles.length === 0) {
        selectedFilesDiv.innerHTML = '<p>Nenhum arquivo PDF selecionado</p>';
        startButton.disabled = true;
        return;
    }
    
    // Exibir arquivos selecionados
    selectedFilesDiv.innerHTML = '<p><strong>Arquivos selecionados:</strong></p>';
    selectedFiles.forEach(file => {
        selectedFilesDiv.innerHTML += `<p>• ${file.name}</p>`;
    });
    
    startButton.disabled = false;
});

// Evento para iniciar verificação
startButton.addEventListener('click', async () => {
    if (selectedFiles.length === 0) {
        alert('Selecione pelo menos um arquivo PDF.');
        return;
    }
    
    startButton.disabled = true;
    
    // Limpar resultados anteriores
    resultsContainer.classList.add('hidden');
    resultsContent.innerHTML = '';
    
    // Iniciar processamento
    await progressWindow.startProcessing(selectedFiles);
});

// Função para exibir resultados
function showResults(results) {
    if (!results || Object.keys(results).length === 0) {
        return;
    }
    
    resultsContent.innerHTML = '';
    
    // Adicionar informações de cada diário verificado
    for (const [nomeDiario, statusInfo] of Object.entries(results)) {
        const fileResultDiv = document.createElement('div');
        fileResultDiv.className = 'file-result';
        
        const fileNameDiv = document.createElement('div');
        fileNameDiv.className = 'file-name';
        fileNameDiv.textContent = nomeDiario;
        fileResultDiv.appendChild(fileNameDiv);
        
        // Adicionar linha separadora
        const separator = document.createElement('hr');
        fileResultDiv.appendChild(separator);
        
        // Adicionar status de cada item verificado
        for (const [chave, valor] of Object.entries(statusInfo)) {
            if (chave !== "Observações") {
                const statusItem = document.createElement('div');
                statusItem.className = 'status-item';
                
                const statusLabel = document.createElement('div');
                statusLabel.className = 'status-label';
                statusLabel.textContent = chave;
                
                const statusValue = document.createElement('div');
                statusValue.className = 'status-value';
                
                if (valor === '✅') {
                    statusValue.className += ' status-pass';
                } else if (valor === '❌') {
                    statusValue.className += ' status-fail';
                } else if (valor === '❓') {
                    statusValue.className += ' status-unknown';
                } else if (valor === 'N/A') {
                    statusValue.className += ' status-na';
                }
                
                statusValue.textContent = valor;
                
                statusItem.appendChild(statusLabel);
                statusItem.appendChild(statusValue);
                fileResultDiv.appendChild(statusItem);
            }
        }
        
        // Adicionar observações se houver
        if (statusInfo["Observações"]) {
            const observationsDiv = document.createElement('div');
            observationsDiv.className = 'observations';
            observationsDiv.textContent = `Observações: ${statusInfo["Observações"]}`;
            fileResultDiv.appendChild(observationsDiv);
        }
        
        resultsContent.appendChild(fileResultDiv);
    }
    
    // Exibir container de resultados
    resultsContainer.classList.remove('hidden');
    
    // Rolar para exibir os resultados
    resultsContainer.scrollIntoView({ behavior: 'smooth' });
}

// Evento para baixar relatório
downloadReportBtn.addEventListener('click', () => {
    const results = progressWindow.getResults();
    
    if (!results || Object.keys(results).length === 0) {
        alert('Não há resultados para gerar relatório.');
        return;
    }
    
    // Criar texto do relatório
    let reportText = `Relatório de Verificação dos Diários de Classe\n`;
    reportText += `${'='.repeat(50)}\n\n`;
    
    for (const [nomeDiario, statusInfo] of Object.entries(results)) {
        reportText += `Arquivo: ${nomeDiario}\n`;
        reportText += `${'-'.repeat(nomeDiario.length + 9)}\n`;
        
        for (const [chave, valor] of Object.entries(statusInfo)) {
            if (chave !== "Observações") {
                reportText += `- ${chave}: ${valor}\n`;
            }
        }
        
        if (statusInfo["Observações"]) {
            reportText += `- Observações: ${statusInfo["Observações"]}\n`;
        }

        reportText += `\n${'='.repeat(50)}\n\n`;
    }
    
    // Criar blob e link para download
    const blob = new Blob([reportText], { type: 'text/plain;charset=utf-8' });
    const url = URL.createObjectURL(blob);
    
    const a = document.createElement('a');
    a.href = url;
    a.download = 'relatorio_verificacao_diarios.txt';
    document.body.appendChild(a);
    a.click();
    
    // Limpeza
    setTimeout(() => {
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
    }, 0);
});

// Evento para nova verificação
newCheckBtn.addEventListener('click', () => {
    // Limpar seleção de arquivos
    fileInput.value = '';
    selectedFiles = [];
    selectedFilesDiv.innerHTML = '<p>Nenhum arquivo selecionado</p>';
    
    // Esconder resultados
    resultsContainer.classList.add('hidden');
    
    // Desabilitar botão de iniciar
    startButton.disabled = true;
    
    // Rolar para o topo
    window.scrollTo({ top: 0, behavior: 'smooth' });
});

// Exibir mensagem de boas-vindas
document.addEventListener('DOMContentLoaded', () => {
    alert('Bem-vindo ao Verificador de Diários PDF - Checker 2.0!\n\nPara iniciar, selecione os arquivos PDF que deseja verificar.');
});