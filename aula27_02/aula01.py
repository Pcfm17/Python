# Loop infinito para processar múltiplos autômatos
while True:
    # Entrada 1: Lista de estados do autômato
    estados = input().split()
    
    # Entrada 2: Estado inicial (ponto de partida)
    inicial = input()
    
    # Entrada 3: Estados de aceitação (estados finais que aceitam a palavra)
    aceitacao = input().split()
    
    # Entrada 4: Alfabeto (símbolos válidos aceitos pelo autômato)
    alfabeto = input().split()
    
    # Dicionário para armazenar as transições do autômato
    # Estrutura: {estado: {símbolo: próximo_estado}}
    transcricao = {}

    # Leitura das transições para cada estado
    for i in range(0, len(estados)):
        linha = input().split()
        # Armazena as transições de um estado para cada símbolo do alfabeto
        transcricao[linha[0]] = {
            alfabeto[0] : linha[1],  # Transição para o primeiro símbolo
            alfabeto[1] : linha[2],  # Transição para o segundo símbolo
        }

    # Exibição das informações configuradas
    print(estados)
    print(inicial)
    print(aceitacao)
    print(alfabeto)
    print(transcricao)

    # Entrada das palavras a serem testadas no autômato
    palavras = input().split()

    # Processa cada palavra
    for palavra in palavras:
        # Estado atual começa no estado inicial
        atual = inicial
        
        # Percorre cada caractere da palavra
        for caracter in palavra:
            # Verifica se o caractere está no alfabeto
            if caracter not in alfabeto:
                # Caractere inválido: marca como rejeitado
                atual = None
                break
            # Realiza a transição de estado
            atual = transcricao[atual][caracter]
        
        # Verifica se terminou em um estado de aceitação
        if atual in aceitacao:
            print("aceita")
        else:
            print("rejeita")
        
        # Reseta o estado para processar a próxima palavra
        atual = inicial