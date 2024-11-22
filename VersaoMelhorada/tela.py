import tkinter as tk
from tkinter import PhotoImage

class Tela:
    # Função para criar a tela
    def CriarTela(titulo, tamanho, fundo, texto, op1, op2, op3, op4):
        # Cria a janela principal
        janela = tk.Tk()
        janela.title(titulo)  # Título da janela
        janela.geometry(tamanho)  # Tamanho da janela
        janela.config(bg="black")  # Fundo da janela preto

        # Título (centralizado)
        titulo_label = tk.Label(janela, text=titulo, font=("Arial", 20), bg="black", fg="white")
        titulo_label.pack(pady=20)

        # Carregar a imagem de fundo com o parâmetro 'fundo'
        imagem_fundo = PhotoImage(file=fundo)  # Aqui usamos o parâmetro 'fundo' para carregar a imagem
        imagem_fundo = imagem_fundo.subsample(2, 2)  # Diminuindo a imagem pela metade (ajustando o tamanho)
        
        # Exibindo a imagem de fundo
        imagem_label = tk.Label(janela, image=imagem_fundo, bg="black")
        imagem_label.pack(pady=20)  # Espaço entre o título e a imagem

        # Fala do narrador (Texto no topo)
        fala = tk.Label(janela, text=texto, font=("Arial", 16), bg="black", fg="white", wraplength=750)
        fala.pack(pady=20)

        # Função que será chamada quando um botão for clicado
        def opcao_clicada(opcao):
            texto_inferior.config(text=f"Você escolheu a opção: {opcao}")

        # Botões de opções: duas opções em cima e duas embaixo
        botoes_frame = tk.Frame(janela, bg="black")
        botoes_frame.pack(pady=30)  # Espaço entre a imagem e as opções

        # Criando os botões
        opcoes = [op1, op2, op3, op4]

        # Determinando o tamanho do maior texto (para garantir que todos os botões sejam do mesmo tamanho)
        maior_texto = max(opcoes, key=len)
        largura_botao = len(maior_texto)  # Largura com base no tamanho do maior texto
        altura_botao = 2  # Definindo uma altura fixa para os botões

        # Primeira linha (duas opções)
        linha_1 = tk.Frame(botoes_frame, bg="black")
        linha_1.pack(side="top", pady=10)
        
        # Botões com bordas e fundo, todos com o mesmo tamanho
        botao_1 = tk.Button(linha_1, text=opcoes[0], font=("Arial", 14), command=lambda opcao=opcoes[0]: opcao_clicada(opcao),
                             bd=2, highlightthickness=1, relief="raised", bg="lightblue", fg="black", width=largura_botao, height=altura_botao)
        botao_1.pack(side="left", padx=20)

        botao_2 = tk.Button(linha_1, text=opcoes[1], font=("Arial", 14), command=lambda opcao=opcoes[1]: opcao_clicada(opcao),
                             bd=2, highlightthickness=1, relief="raised", bg="lightblue", fg="black", width=largura_botao, height=altura_botao)
        botao_2.pack(side="left", padx=20)

        # Segunda linha (duas opções)
        linha_2 = tk.Frame(botoes_frame, bg="black")
        linha_2.pack(side="top", pady=10)
        
        botao_3 = tk.Button(linha_2, text=opcoes[2], font=("Arial", 14), command=lambda opcao=opcoes[2]: opcao_clicada(opcao),
                             bd=2, highlightthickness=1, relief="raised", bg="lightblue", fg="black", width=largura_botao, height=altura_botao)
        botao_3.pack(side="left", padx=20)

        botao_4 = tk.Button(linha_2, text=opcoes[3], font=("Arial", 14), command=lambda opcao=opcoes[3]: opcao_clicada(opcao),
                             bd=2, highlightthickness=1, relief="raised", bg="lightblue", fg="black", width=largura_botao, height=altura_botao)
        botao_4.pack(side="left", padx=20)

        # Texto no canto inferior (centralizado)
        texto_inferior = tk.Label(janela, text="Texto padrão no rodapé", font=("Arial", 12), bg="black", fg="white")
        texto_inferior.pack(side="bottom", pady=20, fill="x", anchor="s")

        # Exibir a janela
        janela.mainloop()