from tela import Tela

##Início básico

titulo = "Jogo RPG"
tamanho = "800x800"
fundo = "./assets/floresta.png"
texto = "Você está em uma floresta escura. Uma trilha se estende ao norte e outra ao leste."
op1 = "Ir para o Norte"
op2 = "Ir para o Sul"
op3 = "Ir para o Leste"
op4 = "Ir para o Oeste"

tela = Tela(titulo, tamanho, fundo, texto, op1, op2, op3, op4)

