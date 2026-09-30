import tkinter as tk


class Vida:
    def __init__(self, janela, callback_game_over):

        self.callback_game_over = callback_game_over

        self.vidas = 4

        self.label = tk.Label(
            janela,
            text="♥ ♥ ♥",
            font=("Arial", 30, "bold"),
            bg="#080817",
            fg="red"
        )

        self.label.place(
            x=20,
            y=60
        )

        self.label.lift()

    def perder_vida(self):

        if self.vidas > 0:
            self.vidas -= 1

        coracoes = "♥ " * self.vidas

        self.label.config(
            text=coracoes
        )

        if self.vidas == 0:
            self.callback_game_over()
            return True

        return False