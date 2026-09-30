import tkinter as tk

from componentes.menu import MenuPrincipal
from componentes.fase1 import Fase1


class AplicativoJogo:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("FUGA DA RAVE")
        self.janela.state('zoomed')

        self.largura_tela = self.janela.winfo_screenwidth()
        self.altura_tela = self.janela.winfo_screenheight()

        self.menu = MenuPrincipal(
            self.janela,
            self.largura_tela,
            self.altura_tela,
            self.mudar_para_fase1
        )

        self.janela.bind(
            "<Escape>",
            lambda e: self.janela.destroy()
        )

    def mudar_para_fase1(self):
        self.menu.destruir()

        self.fase1 = Fase1(
            self.janela,
            self.largura_tela,
            self.altura_tela
        )

    def iniciar(self):
        self.janela.mainloop()


if __name__ == "__main__":
    jogo = AplicativoJogo()
    jogo.iniciar()