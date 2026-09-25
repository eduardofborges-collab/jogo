import tkinter as tk
# Importa as classes construídas nos arquivos da pasta componentes
from componentes.menu import MenuPrincipal
from componentes.fase1 import Fase1

class AplicativoJogo:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("FUGA DA RAVE")
        self.janela.state('zoomed')

        self.largura_tela = self.janela.winfo_screenwidth()
        self.altura_tela = self.janela.winfo_screenheight()

        # Inicia a aplicação exibindo o componente MenuPrincipal
        self.menu = MenuPrincipal(self.janela, self.largura_tela, self.altura_tela, self.mudar_para_fase1)
        
        self.janela.bind("<Escape>", lambda e: self.janela.destroy())

    def mudar_para_fase1(self):
        self.menu.destruir()  # Apaga o menu completamente
        self.fase1 = Fase1(self.janela, self.largura_tela, self.altura_tela)  # Instancia a Fase 1

    def iniciar(self):
        self.janela.mainloop()

if __name__ == "__main__":
    jogo = AplicativoJogo()
    jogo.iniciar()
