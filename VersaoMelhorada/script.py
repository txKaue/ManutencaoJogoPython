from tela import Tela
from time import sleep
from player import Player

titulo = "Jogo RPG"
tamanho = "800x700"
fundo = "./assets/mato.png"
texto = "Você está em uma floresta escura. Uma trilha se estende ao norte e outra ao leste."
op1 = "Ir para o Norte"
op2 = "Ir para o Leste"
op3 = "Voltar"
op4 = "Sair"

player = Player("Kauê")
tela = Tela(titulo, tamanho, fundo, texto, op1, op2, op3, op4, player)

