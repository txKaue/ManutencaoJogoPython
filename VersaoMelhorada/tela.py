import tkinter as tk
from tkinter import Label
from tkinter import PhotoImage
from PIL import Image, ImageTk
from time import sleep

class Tela:
    # Função para criar a tela
    def __init__(self, titulo, tamanho, fundo, texto, op1, op2, op3, op4, player):
        # Cria a janela principal
        self.janela = tk.Tk()
        self.janela.title(titulo)  # Título da janela
        self.janela.geometry(self.getPosicao(tamanho))  # Tamanho da janela
        self.janela.config(bg="black")  # Fundo da janela preto

        # Título (centralizado)
        self.titulo_label = tk.Label(self.janela, text=titulo, font=("Arial", 20), bg="black", fg="white")
        self.titulo_label.pack(pady=20)

        # Ajustando o tamanho da imagem
        imagem_fundo = Image.open(fundo)
        imagem_fundo = imagem_fundo.resize((200, 200))  # Ajuste do tamanho da imagem

        # Convertendo a imagem para um formato compatível com o Tkinter
        self.imagem_fundo_tk = ImageTk.PhotoImage(imagem_fundo)

        # Exibindo a imagem de fundo
        self.imagem_label = tk.Label(self.janela, image=self.imagem_fundo_tk, bg="black")
        self.imagem_label.pack(pady=20)  # Espaço entre o título e a imagem

        # Fala do narrador (Texto no topo)
        self.fala = tk.Label(self.janela, text=texto, font=("Arial", 16), bg="black", fg="white", wraplength=750)
        self.fala.pack(pady=20)

        # Texto no canto inferior (centralizado)
        self.texto_inferior = tk.Label(self.janela, text="Texto padrão no rodapé", font=("Arial", 12), bg="black", fg="white")
        self.texto_inferior.pack(side="bottom", pady=20, fill="x", anchor="s")

        # Botões de opções: duas opções em cima e duas embaixo
        botoes_frame = tk.Frame(self.janela, bg="black")
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
        self.botao_1 = tk.Button(linha_1, text=opcoes[0], font=("Arial", 14),
                    command=lambda opcao=opcoes[0]: self.opcao_clicada(self.botao_1.cget("text"), player),  # Chamando a função com self
                    bd=2, highlightthickness=1, relief="raised", bg="lightblue", fg="black",
                    width=largura_botao, height=altura_botao)
        self.botao_1.pack(side="left", padx=20)

        self.botao_2 = tk.Button(linha_1, text=opcoes[1], font=("Arial", 14),
                     command=lambda opcao=opcoes[1]: self.opcao_clicada(self.botao_2.cget("text"), player),  # Usar self para chamar o método
                     bd=2, highlightthickness=1, relief="raised", bg="lightblue", fg="black",
                     width=largura_botao, height=altura_botao)
        self.botao_2.pack(side="left", padx=20)

        # Segunda linha (duas opções)
        linha_2 = tk.Frame(botoes_frame, bg="black")
        linha_2.pack(side="top", pady=10)

        self.botao_3 = tk.Button(linha_2, text=opcoes[2], font=("Arial", 14),
                     command=lambda opcao=opcoes[2]: self.opcao_clicada(self.botao_3.cget("text"), player),  # Usar self para chamar o método
                     bd=2, highlightthickness=1, relief="raised", bg="lightblue", fg="black",
                     width=largura_botao, height=altura_botao)
        self.botao_3.pack(side="left", padx=20)

        self.botao_4 = tk.Button(linha_2, text=opcoes[3], font=("Arial", 14),
                     command=lambda opcao=opcoes[3]: self.opcao_clicada(self.botao_4.cget("text"), player),  # Usar self para chamar o método
                     bd=2, highlightthickness=1, relief="raised", bg="lightblue", fg="black",
                     width=largura_botao, height=altura_botao)
        self.botao_4.pack(side="left", padx=20)

        # Exibir a janela
        self.janela.mainloop()

    def opcao_clicada(self, opcao, player):
    
        ## Se estiver na floresta

        if player.getLocal() == "floresta":
            print(opcao)
            if opcao == "Ir para o Norte":
                texto = "Você chega até uma velha cabana abandonada."
                self.AtualizarBotoes(["Olhar janela", "Entrar na cabana"])

                self.fala.config(text=texto)
                player.setLocal("cabanaFora")
                self.MudaFundo("./assets/cabanaFora.png")
            elif opcao == "Ir para o Leste":
                texto = "Você encontra uma ponte misteriosa com uma grade impedindo a passagem."
                self.AtualizarBotoes(["Passar pela ponte", "Observar grade"])
                self.fala.config(text=texto)
                player.setLocal("ponte")
                self.MudaFundo("./assets/ponte.png")
            elif opcao == "Voltar":
                #self.texto_inferior.config(text=f"Você não tem para onde voltar")
                textoAntigo = self.fala.cget('text')
                texto = "Você não tem para onde voltar"
                self.fala.config(text=texto)
                self.fala.after(1000, lambda: self.fala.config(text=textoAntigo))
            elif opcao == "Sair":
                self.janela.destroy()





        elif player.getLocal() == "cabanaFora":
            print(opcao)
            if opcao == "Olhar janela":
                texto = "Você olha pela janela e não consegue ver nada."
                self.fala.config(text=texto)
                self.AtualizarBotoes(["Bater na janela", "Chamar alguém"])
                self.MudaFundo("./assets/janelaCabana.png")
                player.setLocal("janelaCabana")

            elif opcao == "Entrar na cabana":
                player.setLocal("cabanaDentro")
                if (player.temItem("chave")):
                    texto = "Dentro da cabana você encontra somente uma poltrona velha."
                    self.fala.config(text=texto)
                    self.AtualizarBotoes(["Não fazer nada", "Chamar alguém"])
                    self.MudaFundo("./assets/cabanaDentro.png")
                else:
                    self.AtualizarBotoes(["Pegar chave", "Chamar alguém"])
                    texto = "Dentro da cabana você encontra uma chave em uma poltrona velha."
                    self.fala.config(text=texto)
                    self.MudaFundo("./assets/cabanaDentro.png")

            elif opcao == "Voltar":
                self.AtualizarBotoes(["Ir para o Norte", "Ir para o Leste"])
                texto = "Você volta para a floresta."
                self.fala.config(text=texto)
                player.setLocal("floresta")
                self.MudaFundo("./assets/floresta.png")
            elif opcao == "Sair":
                self.janela.destroy()



        elif player.getLocal() == "janelaCabana":
            print(opcao)
            if opcao == "Bater na janela":
                #player.setLocal("janelaCabana")
                self.MudaFundo("./assets/janelaCabana.png")
                textoAntigo = self.fala.cget('text')
                texto = "Você bate na janela e nada acontece"
                self.fala.config(text=texto)
                self.fala.after(1000, lambda: self.fala.config(text=textoAntigo))

            elif opcao == "Chamar alguém":
                #player.setLocal("cabanaDentro")
                #self.MudaFundo("./assets/ponte.png")
                textoAntigo = self.fala.cget('text')
                texto = "Você chama alguém e nada acontece"
                self.fala.config(text=texto)
                self.fala.after(1000, lambda: self.fala.config(text=textoAntigo))

            elif opcao == "Voltar":
                self.AtualizarBotoes(["Olhar janela", "Entrar na cabana"])
                texto = "Você volta para a porta da cabana."
                self.fala.config(text=texto)
                player.setLocal("cabanaFora")
                self.MudaFundo("./assets/cabanaFora.png")

            elif opcao == "Sair":
                self.janela.destroy()


        ############# DENTRO DA CABANA AQUI ################
        elif player.getLocal() == "cabanaDentro":
            print(opcao)
            if opcao == "Pegar chave":
                textoAntigo = self.fala.cget('text')
                texto = "Você pega a chave. Não há mais nada aqui."
                self.fala.config(text=texto)
                player.addItem("chave")
                self.AtualizarBotoes(["Não fazer nada", "Chamar alguém"])

            elif opcao == "Chamar alguém":
                textoAntigo = self.fala.cget('text')
                texto = "Você chama alguém e nada acontece"
                self.fala.config(text=texto)
                self.fala.after(1000, lambda: self.fala.config(text=textoAntigo))

            elif opcao == "Voltar":
                self.AtualizarBotoes(["Olhar janela", "Entrar na cabana"])
                texto = "Você volta para a porta da cabana."
                self.fala.config(text=texto)
                player.setLocal("cabanaFora")
                self.MudaFundo("./assets/cabanaFora.png")
            
            elif opcao == "Não fazer nada":
                textoAntigo = self.fala.cget('text')
                texto = "Você não faz nada."
                self.fala.config(text=texto)

            elif opcao == "Sair":
                self.janela.destroy()




        elif player.getLocal() == "ponte":
            print(opcao)
            if opcao == "Observar grade":
                player.setLocal("portao")
                self.MudaFundo("./assets/cadeado.png")
            elif opcao == "Passar":
                # Adicionar verificação da chave
                #player.setLocal("tesouro")
                #self.MudaFundo("./assets/ponte.png")
                textoAntigo = self.fala.cget('text')
                texto = "Você precisa de uma chave"
                self.fala.config(text=texto)
                self.fala.after(1000, lambda: self.fala.config(text=textoAntigo))
            elif opcao == "Voltar":
                self.AtualizarBotoes(["Ir para o Norte", "Ir para o Leste"])
                texto = "Você volta para a floresta."
                self.fala.config(text=texto)
                player.setLocal("floresta")
                self.MudaFundo("./assets/floresta.png")
            elif opcao == "Sair":
                self.janela.destroy()
                
    def MudaFundo(self, img):
        # Carregar a nova imagem de fundo
        imagem_fundo = Image.open(img)
        imagem_fundo = imagem_fundo.resize((200, 200))  # Ajustando o tamanho da imagem

        # Converter a imagem para o formato do Tkinter
        imagem_fundo_tk = ImageTk.PhotoImage(imagem_fundo)

        # Atualizar a imagem do Label de fundo
        self.imagem_label.config(image=imagem_fundo_tk)
        # Manter a referência da imagem para evitar que seja descartada
        self.imagem_label.image = imagem_fundo_tk

    def iniciar(self):
        self.janela.mainloop()

    def getPosicao(self, tamanho):
        # Criando uma instância temporária de Tk() para pegar as dimensões da tela
        janela_temporaria = tk.Tk()

        # Obtendo as dimensões da tela
        largura_tela = janela_temporaria.winfo_screenwidth()
        altura_tela = janela_temporaria.winfo_screenheight()

        # Fechar a instância temporária para não aparecer na tela
        janela_temporaria.destroy()

        # Obtendo as dimensões da janela a partir do parâmetro 'tamanho' (no formato "largura x altura")
        largura_janela = int(tamanho.split('x')[0])
        altura_janela = int(tamanho.split('x')[1])

        # Calculando a posição para centralizar a janela
        x = (largura_tela - largura_janela) // 2
        y = (altura_tela - altura_janela) // 2

        # Retorna a string de posição da janela
        posicao = f"{tamanho}+{x}+{y-35}"

        return posicao
    
    def AtualizarBotoes(self, novos_textos):

        if len(novos_textos) == 2:  # Verifica se a lista contém exatamente 4 elementos
            # Atualiza o texto de cada botão
            self.botao_1.config(text=novos_textos[0])
            self.botao_2.config(text=novos_textos[1])

