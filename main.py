import random
import string

def create_word_search(words, size):
    # Inicializa a grade com espaços vazios
    grid = [[' ' for _ in range(size)] for _ in range(size)]
    
    # Definindo direções para inserir palavras
    directions = ['horizontal', 'vertical', 'diagonal', 'diagonal_rev', 'diagonal_up', 'diagonal_up_rev']
    
    for word in words:
        placed = False
        while not placed:
            direction = random.choice(directions)
            if direction == 'horizontal':
                row = random.randint(0, size-1)
                col = random.randint(0, size-len(word))
                if all(grid[row][col+i] in (' ', letter) for i, letter in enumerate(word)):
                    for i, letter in enumerate(word):
                        grid[row][col+i] = letter
                    placed = True
            elif direction == 'vertical':
                row = random.randint(0, size-len(word))
                col = random.randint(0, size-1)
                if all(grid[row+i][col] in (' ', letter) for i, letter in enumerate(word)):
                    for i, letter in enumerate(word):
                        grid[row+i][col] = letter
                    placed = True
            elif direction == 'diagonal':
                row = random.randint(0, size-len(word))
                col = random.randint(0, size-len(word))
                if all(grid[row+i][col+i] in (' ', letter) for i, letter in enumerate(word)):
                    for i, letter in enumerate(word):
                        grid[row+i][col+i] = letter
                    placed = True
            elif direction == 'diagonal_rev':
                row = random.randint(0, size-len(word))
                col = random.randint(len(word)-1, size-1)
                if all(grid[row+i][col-i] in (' ', letter) for i, letter in enumerate(word)):
                    for i, letter in enumerate(word):
                        grid[row+i][col-i] = letter
                    placed = True
            elif direction == 'diagonal_up':
                row = random.randint(len(word)-1, size-1)
                col = random.randint(0, size-len(word))
                if all(grid[row-i][col+i] in (' ', letter) for i, letter in enumerate(word)):
                    for i, letter in enumerate(word):
                        grid[row-i][col+i] = letter
                    placed = True
            elif direction == 'diagonal_up_rev':
                row = random.randint(len(word)-1, size-1)
                col = random.randint(len(word)-1, size-1)
                if all(grid[row-i][col-i] in (' ', letter) for i, letter in enumerate(word)):
                    for i, letter in enumerate(word):
                        grid[row-i][col-i] = letter
                    placed = True
    
    # Preenche os espaços vazios com letras aleatórias
    for i in range(size):
        for j in range(size):
            if grid[i][j] == ' ':
                grid[i][j] = "#" #random.choice(string.ascii_uppercase)
                
    
    return grid

def print_grid(grid):
    for row in grid:
        print(' '.join(row))

# Lista de palavras (pode ser expandida para 200 palavras)
words = [
    "SUSTENTÁVEL", "ACESSÓRIO", "ACOLHIMENTO", "ADMINISTRAÇÃO", "ADVOCACIA", "ALGORITMO", "ANÁLISE", "ANIMAÇÃO", "APLICATIVO", "APRENDIZ", "ARQUITETURA", "ARTE", "ARTIFICIAL", "ATHON", "ATHON", "ATHON", "ATHON", "ATHON", "ATHON", "ATHON", "ATHON", "ATHON", "ATHON", "ATHON", "AUDIOVISUAL", "AUTOMAÇÃO", "BIG DATA", "BRANDING", "CÂMERA", "CARREIRA", "CIBERSEGURANÇA", "CINEMA", "CINEMATOGRAFIA", "CIRCUITO", "CIVIL", "CIVIL", "CLIENTE", "COMÉRCIO", "COMPETENCIA", "COMPOSIÇÃO", "COMPUTAÇÃO", "COMPUTADOR", "COMERCIAL", "COMUNICAÇÃO", "CONECTIVIDADE", "CONFECÇÃO", "CONSTITUIÇÃO", "CONSTRUÇÃO", "CONTABILIDADE", "CONTRATO", "CONTROLE", "COSTURA", "CRIATIVIDADE", "CRIPTOGRAFIA", "CULTURA", "DADOS", "DESENVOLVEDOR", "DESENVOLVIMENTO", "DESFILE", "DESIGN", "DIGITAL", "DIREITO", "DOCUMENTÁRIO", "ECOMMERCE", "ECONOMIA", "EDIÇÃO", "EDIFÍCIO", "EFEITOS", "EMAIL", "EMPATIA", "EMPREENDEDOR", "EMPREGABILIDADE", "EMPREGO", "ENGENHARIA", "ENSAIO", "ESCULTURA", "ESTÁGIO", "ESTAMPAGEM", "ESTILO", "ESTRATÉGIA", "ESTRUTURA", "ESTÚDIO", "ESTUDOS", "ÉTICA", "EXPORTAÇÃO", "EXPOSIÇÃO", "FACULDADE", "FILME", "FINANÇAS", "FLASH", "FINANCEIRO", "FOCO", "FOTOGRAFIA", "FOTÓGRAFO", "FUNIL", "GESTÃO", "GOOGLE", "GRAVURA", "HABILIDADE", "HIDRÁULICA", "ILUMINAÇÃO", "IMPORTAÇÃO", "IMPRESSÃO", "INFLUENCIADOR", "INFORMAÇÃO", "INOVAÇÃO", "INSTALAÇÃO", "INTELIGÊNCIA", "INTELIGÊNCIA", "INTERFACE", "INTERIORES", "INTERNET", "INVESTIMENTO", "JORNAL", "JORNALISMO", "JUSTIÇA", "LEI", "LENTE", "LIDERANÇA", "LOCUTOR", "LOGÍSTICA", "MANUFATURA", "MAQUETE", "MARCA", "MARKETING", "MECÂNICA", "MERCADO", "MÍDIA", "MOBILE", "MODA", "MODELAGEM", "MOTIVAÇÃO", "NEGOCIAÇÃO", "NEGÓCIOS", "NETWORKING", "NOTÍCIA", "PAISAGISMO", "PENAL", "PENALIDADE", "PERFORMANCE", "PERSONA", "PESQUISA", "PESSOAS", "PINTURA", "PLANEJAMENTO", "PORTFÓLIO", "POSICIONAMENTO", "PROCESSADOR", "PROCESSO", "PRODUÇÃO", "PRODUTO", "PROGRAMAÇÃO", "PROJETO", "PROPAGANDA", "PUBLICIDADE", "QUALIDADE", "RÁDIO", "REDAÇÃO", "REDES", "RETRATO", "REVISTA", "ROBÓTICA", "ROTEIRO", "SEGMENTAÇÃO", "SEGURANÇA", "SERVIÇO", "SOCIAL", "SOFTWARE", "SOM", "SUSTENTABILIDADE", "SUSTENTÁVEL", "TECIDO", "TECNOLOGIA", "TECNOLOGIA", "TELEVISÃO", "TENDÊNCIA", "TERMODINÂMICA", "TRANSPORTE", "TREND", "TRIBUNAL", "URBANISMO", "VENDAS", "VÍDEO", "VITRINISMO", "WEB", "DIVERSIDADE", "PERTENCIMENTO", "SONHOS", "CONQUISTAS", "TRABALHO", "EXPERTISE", "ESPECIALISTA", "CURSOS", "LIVROS", "ESTÉTICA", "INTERNACIONAL", "CONEXÃO", "SISTEMA", "VIVENCIAS", "ATENDIMENTO" 
]

# Tamanho da grade
size = 60

# Cria a caça-palavras
grid = create_word_search(words, size)

# Imprime a caça-palavras
print_grid(grid)
