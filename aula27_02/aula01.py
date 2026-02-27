while True:
    estados = input().split()
    inicial = input()
    aceitacao = input().split()
    alfabeto = input().split()
    transcricao = {}

    for i in range(0, len(estados)):
        linha = input().split()
        transcricao[linha[0]] = {
            alfabeto[0] : linha[1],
            alfabeto[1] : linha[2],
        }

    print(estados)
    print(inicial)
    print(aceitacao)
    print(alfabeto)
    print(transcricao)

    palavras = input().split()

    atual = inicial

    for palavra in palavras:
        for caracter in palavra:
            if caracter not in alfabeto:
                atual = None
                break
            atual = transcricao[atual][caracter]
        if atual in aceitacao:
            print("aceita")
        else:
            print("rejeita")
        atual = inicial