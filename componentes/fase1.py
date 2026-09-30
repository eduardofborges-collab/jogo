import tkinter as tk
from PIL import Image, ImageTk

from componentes.score import Score
from componentes.spawner import Spawner
from componentes.jogador import Jogador
from componentes.vida import Vida


class Fase1:

    def __init__(self, master, largura, altura):

        self.master = master
        self.largura = largura
        self.altura = altura

        self.teclas_pressionadas = set()

        self.jogo_terminou = False
        self.after_id = None

        self.canvas = tk.Canvas(
            master,
            width=largura,
            height=altura,
            bd=0,
            highlightthickness=0
        )

        self.canvas.place(
            x=0,
            y=0
        )

        img_original = Image.open(
            r"C:\Users\Aluno\jogo2\imagens\background\fase1\background.png"
        )

        img_original = img_original.resize(
            (largura, altura),
            Image.Resampling.LANCZOS
        )

        self.bg_image = ImageTk.PhotoImage(
            img_original
        )

        self.canvas.create_image(
            0,
            0,
            image=self.bg_image,
            anchor="nw"
        )

        self.jogador = Jogador(
            self.canvas,
            x=150,
            y=altura - 450
        )

        self.score = Score(
            self.master
        )

        self.vida = Vida(
            self.master,
            self.game_over
        )

        self.spawner = Spawner(
            self.canvas,
            self.score,
            self.vida
        )

        self.master.bind(
            "<KeyPress>",
            self.pressionou_tecla
        )

        self.master.bind(
            "<KeyRelease>",
            self.soltou_tecla
        )

        self.loop_fase()

    def pressionou_tecla(self, e):

        tecla = e.keysym.lower()

        self.teclas_pressionadas.add(
            tecla
        )

    def soltou_tecla(self, e):

        tecla = e.keysym.lower()

        if tecla in self.teclas_pressionadas:

            self.teclas_pressionadas.remove(
                tecla
            )

    def loop_fase(self):

        if self.jogo_terminou:
            return

        if not self.canvas.winfo_exists():
            return

        self.jogador.mover(
        self.teclas_pressionadas
    )

        self.spawner.mover()

        if self.jogo_terminou:
            return

        self.spawner.verificar_colisao(
        self.jogador
    )

        self.after_id = self.master.after(
        16,
        self.loop_fase
    )

    def game_over(self):

        self.jogo_terminou = True
        
        if self.after_id is not None:

            self.master.after_cancel(
                self.after_id
            )

            self.after_id = None
        
        self.master.destroy()