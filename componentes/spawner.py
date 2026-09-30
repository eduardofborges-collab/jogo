import random


class Spawner:
    def __init__(self, canvas, score, vida):
        self.canvas = canvas
        self.score = score
        self.vida = vida

        self.velocidade = 3
        self.item = None

        self.criar_item()

    def criar_item(self):
        x = random.randint(100, 900)
        y = 100

        self.item = self.canvas.create_oval(
            x,
            y,
            x + 30,
            y + 30,
            fill="#00ff88",
            outline=""
        )

    def mover(self):

        self.canvas.move(
            self.item,
            0,
            self.velocidade
        )

        pos = self.canvas.coords(self.item)

        if pos[1] > self.canvas.winfo_height():

            self.canvas.delete(self.item)

            acabou = self.vida.perder_vida()

            if acabou:
                return

            self.criar_item()

    def verificar_colisao(self, jogador):

        jogador_pos = self.canvas.coords(jogador.id)
        item_pos = self.canvas.coords(self.item)

        jogador_x = jogador_pos[0]
        jogador_y = jogador_pos[1]

        jogador_x2 = jogador_x + 200
        jogador_y2 = jogador_y + 400

        item_x1 = item_pos[0]
        item_y1 = item_pos[1]
        item_x2 = item_pos[2]
        item_y2 = item_pos[3]

        if (
            jogador_x2 > item_x1
            and jogador_x < item_x2
            and jogador_y2 > item_y1
            and jogador_y < item_y2
        ):
            self.canvas.delete(self.item)

            self.score.adicionar()

            self.criar_item()