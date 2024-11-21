import tkinter as tk
from tkinter import PhotoImage

# Função para criar a tela

class Tela:
    def CriarTela(nome, tamanho, fundo, texto, op1, op2, op3, op4):

        # Cria a janela principal
        janela = tk.Tk()
        janela.title(nome)  # Título da janela
        janela.geometry(tamanho)  # Tamanho da janela

        # Carregar a imagem de fundo
        imagem_fundo = PhotoImage(file=fundo)  # Substitua "fundo.png" pelo caminho da sua imagem
        fundo_label = tk.Label(janela, image=imagem_fundo)
        fundo_label.place(relwidth=1, relheight=1)  # Faz a imagem ocupar toda a tela

        # Fala do narrador (Texto no topo)
        fala = tk.Label(janela, text=texto, font=("Arial", 16), bg="white", fg="black", wraplength=750)
        fala.pack(pady=20)

        # Função que será chamada quando um botão for clicado
        def opcao_clicada(opcao):
            texto_inferior.config(text=f"Você escolheu a opção: {opcao}")

        # Botões de opções
        botoes_frame = tk.Frame(janela, bg="white")
        botoes_frame.pack(pady=50)

        opcoes = [
            op1,
            op2,
            op3,
            op4
        ]
        
        for opcao in opcoes:
            botao = tk.Button(botoes_frame, text=opcao, font=("Arial", 14), command=lambda opcao=opcao: opcao_clicada(opcao))
            botao.pack(side="top", pady=10, fill="x", padx=50)

        # Texto no canto inferior
        texto_inferior = tk.Label(janela, text="Escolha uma das opções acima", font=("Arial", 12), bg="white", fg="black")
        texto_inferior.pack(side="bottom", pady=10)

        # Exibir a janela
        janela.mainloop()

