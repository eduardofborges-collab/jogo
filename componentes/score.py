import tkinter as tk


class Score:
    def __init__(self, canvas):
        self.valor = 0

        self.label = tk.Label(
            canvas,
            text="Score: 0",
            font=("Arial", 20, "bold"),
            fg="white",
            bg="#080817"
        )

        self.label.place(x=20, y=20)
        self.label.lift()

    def adicionar(self, pontos=1):
        self.valor += pontos
        self.label.config(
            text=f"Score: {self.valor}"
        )