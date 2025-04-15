// Classe para gerenciar a janela de progresso
class ProgressWindow {
    constructor() {
        // Elementos da interface
        this.progressContainer = document.getElementById('progress-container');
        this.progressBar = document.getElementById('progress-bar');
        this.progressText = document.getElementById('progress-text');
        this.statusLabel = document.getElementById('status-label');
        this.cancelButton = document.getElementById('cancel-btn');
        
        // Estado interno
        this.running = false;
        this.cancelToken = { cancelled: false };
        this.results = null;
        
        // Configurar evento de cancelamento
        this.cancelButton.addEventListener('click', () => this.cancelProcessing());
    }
    
    // Inicia o processamento dos diários
    async startProcessing(diarios) {
        if (this.running) return; // Evita iniciar múltiplas vezes
        
        this.running = true;
        this.cancelToken = { cancelled: false }; // Reset do token de cancelamento
        this.progressContainer.classList.remove('hidden');
        this.progressBar.style.width = '0%';
        this.progressText.textContent = '0%';
        this.statusLabel.textContent = 'Iniciando verificação...';
        
        // Função de callback para atualizar o progresso
        const progressCallback = (message) => {
            if (!this.running) return;
            
            if (message.status === "processing" || message.status === "file_done") {
                const processed = message.processed;
                const total = message.total;
                const filename = message.filename;
                const percentage = Math.round((processed / total) * 100);
                
                this.progressBar.style.width = `${percentage}%`;
                this.progressText.textContent = `${percentage}%`;
                
                if (message.status === "processing") {
                    this.statusLabel.textContent = `Processando ${processed + 1}/${total}: ${filename}...`;
                } else if (message.status === "file_done") {
                    this.statusLabel.textContent = `Concluído ${processed}/${total}: ${filename}`;
                }
            } else if (message.status === "completed") {
                this.finishProcessing(false);
            } else if (message.status === "cancelled") {
                this.finishProcessing(true);
            } else if (message.status === "error") {
                this.finishProcessing(true, message.message);
            }
        };
        
        try {
            // Executar a verificação dos PDFs
            this.results = await Check2P.verificacaoGeral(diarios, progressCallback, this.cancelToken);
        } catch (error) {
            console.error("Erro ao executar verificação:", error);
            this.finishProcessing(true, `Erro inesperado: ${error.message}`);
        }
    }
    
    // Cancela o processamento atual
    cancelProcessing() {
        if (!this.running) return;
        
        if (confirm("Tem certeza que deseja cancelar a verificação dos diários?")) {
            this.statusLabel.textContent = "Cancelando...";
            this.cancelToken.cancelled = true;
        }
    }
    
    // Finaliza o processamento (sucesso ou erro)
    finishProcessing(cancelled = false, errorMessage = null) {
        this.running = false;
        
        if (cancelled) {
            if (errorMessage) {
                this.statusLabel.textContent = `Erro: ${errorMessage}`;
                alert(`Ocorreu um erro: ${errorMessage}`);
            } else {
                this.statusLabel.textContent = "Verificação Cancelada.";
                alert("A verificação dos diários foi cancelada.");
            }
        } else {
            this.progressBar.style.width = '100%';
            this.progressText.textContent = '100%';
            this.statusLabel.textContent = `Verificação Concluída!`;
            
            setTimeout(() => {
                this.progressContainer.classList.add('hidden');
                // Exibir resultados
                if (typeof showResults === 'function') {
                    showResults(this.results);
                }
            }, 1000);
        }
    }
    
    // Retorna os resultados da verificação
    getResults() {
        return this.results;
    }
}