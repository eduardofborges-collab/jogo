import tkinter as tk
from PIL import Image, ImageTk
# IMPORTANTE: Importa o componente do outro arquivo
from componentes.jogador import Jogador 

class Fase1:
    def __init__(self, master, largura, altura):
        self.master = master
        self.largura = largura
        self.altura = altura
        self.teclas_pressionadas = set()

        # Canvas do jogo
        self.canvas = tk.Canvas(master, width=largura, height=altura, bd=0, highlightthickness=0)
        self.canvas.place(x=0, y=0)

        # Imagem de fundo da fase (substitua pela imagem real do cenário depois)
        img_original = Image.new("RGB", (largura, altura), "#0b0612") 
        self.bg_image = ImageTk.PhotoImage(img_original)
        self.canvas.create_image(0, 0, image=self.bg_image, anchor="nw")

        # Inicializa o componente do Jogador que está no outro arquivo
        self.jogador = Jogador(self.canvas, x=200, y=400)

        # Configura escuta do teclado
        self.master.bind("<KeyPress>", self.pressionou_tecla)
        self.master.bind("<KeyRelease>", self.soltou_tecla)

        # Loop de atualização física (FPS)
        self.loop_fase()

    def pressionou_tecla(self, e):
        tecla = e.keysym.lower() if len(e.keysym) == 1 else e.keysym
        self.teclas_pressionadas.add(tecla)

    def soltou_tecla(self, e):
        tecla = e.keysym.lower() if len(e.keysym) == 1 else e.keysym
        if tecla in self.teclas_pressionadas:
            self.teclas_pressionadas.remove(tecla)

    def loop_fase(self):
        if not self.canvas.winfo_exists(): return
        self.jogador.mover(self.teclas_pressionadas)
        self.master.after(16, self.loop_fase)
