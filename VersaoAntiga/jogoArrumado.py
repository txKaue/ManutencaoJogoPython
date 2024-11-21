import random

def mostrar_intro():
    print("\nBem-vindo à Aventura em Texto!")
    print("Você está em uma floresta escura. Uma trilha se estende ao norte e outra ao leste.")

def obter_comando():
    comando = input("\nPara onde você vai? (norte, sul, leste, oeste, voltar, sair): ").lower()
    return comando

def processar_comando(comando, localizacao, inventario):
    if comando == "norte":
        if localizacao == "floresta":
            localizacao = "cabana"
            print("\nVocê encontra uma cabana abandonada.")
        else:
            print("\nVocê não pode ir para o norte daqui.")
    elif comando == "leste":
        if localizacao == "floresta":
            localizacao = "rio"
            print("\nVocê chega a um rio de águas turbulentas.")
        else:
            print("\nVocê não pode ir para o leste daqui.")
    elif comando == "voltar":
        if localizacao == "cabana":
            if "chave" in inventario:
                print("\nVocê volta para a floresta. A chave que você encontrou ainda está no seu inventário.")
            else:
                print("\nVocê volta para a cabana abandonada.")
            localizacao = "floresta"
        elif localizacao == "rio":
            print("\nVocê volta para a floresta escura.")
            localizacao = "floresta"
        elif localizacao == "tesouro":
            print("\nVocê já encontrou o tesouro. Não há mais nada para fazer aqui.")
            localizacao = "floresta"
        else:
            print("\nVocê não pode voltar daqui.")
    elif comando == "sul" or comando == "oeste":
        print("\nVocê não pode ir para essa direção daqui.")
    elif comando == "sair":
        print("\nObrigado por jogar!")
        return "sair", localizacao, inventario
    else:
        print("\nComando inválido.")
    return comando, localizacao, inventario

def explorar_localizacao(localizacao, inventario):
    if localizacao == "cabana":
        if "chave" not in inventario:
            print("\nDentro da cabana, você encontra uma chave enferrujada.")
            inventario.append("chave")
        else:
            print("\nVocê já encontrou a chave na cabana. Não há mais nada de interessante aqui.")
    elif localizacao == "rio":
        print("\nHá uma ponte frágil sobre o rio.")
        if "chave" in inventario:
            print("Você usa a chave para destravar um mecanismo na ponte e atravessá-la.")
            localizacao = "tesouro"
            print("\nVocê encontrou um tesouro escondido! Parabéns!")
        else:
            print("Você precisa encontrar uma maneira de atravessar o rio.")
    elif localizacao == "tesouro":
        print("\nVocê já encontrou o tesouro escondido aqui. Não há mais nada para fazer.")
    return localizacao, inventario

def jogar():
    localizacao = "floresta"
    inventario = []
    mostrar_intro()

    while True:
        comando = obter_comando()
        comando, localizacao, inventario = processar_comando(comando, localizacao, inventario)
        if comando == "sair":
            break
        localizacao, inventario = explorar_localizacao(localizacao, inventario)

jogar()
