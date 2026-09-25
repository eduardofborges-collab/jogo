import tkinter as tk

class Jogador:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.velocidade = 8
        
        self.id = canvas.create_rectangle(
            self.x, self.y, self.x + 50, self.y + 50,
            fill="#ff0055", outline="#ffffff", width=2
        )

    def mover(self, teclas):
        if "w" in teclas or "up" in teclas: self.y -= self.velocidade
        if "s" in teclas or "down" in teclas: self.y += self.velocidade
        if "a" in teclas or "left" in teclas: self.x -= self.velocidade
        if "d" in teclas or "right" in teclas: self.x += self.velocidade
        
        self.canvas.coords(self.id, self.x, self.y, self.x + 50, self.y + 50)
