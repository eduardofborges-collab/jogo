import tkinter as tk
from PIL import Image, ImageTk


class Jogador:
    def __init__(self, canvas, x, y):
        self.canvas = canvas

        self.x = x
        self.y = y

        self.velocidade = 8

        imagem = Image.open(
            r"C:\Users\Aluno\jogo2\imagens\personagem.png"
        )

        imagem = imagem.resize((200,400))

        self.imagem = ImageTk.PhotoImage(imagem)

        self.id = canvas.create_image(
            self.x,
            self.y,
            image=self.imagem,
            anchor="nw"
        )

    def mover(self, teclas):

        if "a" in teclas or "left" in teclas:
            self.x -= self.velocidade

        if "d" in teclas or "right" in teclas:
            self.x += self.velocidade

        self.canvas.coords(
            self.id,
            self.x,
            self.y
        )