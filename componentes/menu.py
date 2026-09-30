import tkinter as tk
from PIL import Image, ImageTk, ImageDraw, ImageFont

class MenuPrincipal:
    class MenuPrincipal:
     def __init__(self, master, largura, altura, callback_iniciar):
        self.master = master
        self.largura = largura
        self.altura = altura
        self.callback_iniciar = callback_iniciar
        self.widgets = []
        
        imagem_original = Image.open(r"C:\Users\Aluno\jogo2\imagens\background\telainicial\background.png")
        imagem_redimensionada = imagem_original.resize((largura, altura), Image.Resampling.LANCZOS)
        
        fonte = ImageFont.truetype(r"C:\Users\Aluno\jogo2\font\BrushGrunge.ttf", 100)
        desenho = ImageDraw.Draw(imagem_redimensionada)
        desenho.text((100, 120), "FUGA DA", font=fonte, fill="#ffffff")
        
        fonte2 = ImageFont.truetype(r"C:\Users\Aluno\jogo2\font\BrushGrunge.ttf", 180)
        desenho.text((100, 230), "RAVE", font=fonte2, fill="#b000ff")
        
        self.bg_image = ImageTk.PhotoImage(imagem_redimensionada)
        self.bg_label = tk.Label(master, image=self.bg_image)
        self.bg_label.place(x=0, y=0, width=largura, height=altura)
        self.widgets.append(self.bg_label)

        self.criar_botao("▶ JOGAR", 440, self.iniciar)
        self.criar_botao("⚙️ CONFIGURAÇÕES", 540, lambda: print("Configurações"))
        self.criar_botao("📖 INSTRUÇÕES", 640, lambda: print("Instruções"))
        self.criar_botao("⏼ SAIR", 740, master.destroy)

    def criar_botao(self, texto, pos_y, comando):
        btn = tk.Button(
            self.master, text=texto, command=comando, bd=0, bg="#2E2E2E", fg="#ffffff",
            font=("Arial", 16, "bold"), activebackground="#8a00c4", activeforeground="#ffffff",
            cursor="hand2", highlightthickness=0
        )
        btn.bind("<Enter>", self.mouse_entrou)
        btn.bind("<Leave>", self.mouse_saiu)
        btn.place(x=100, y=pos_y, width=250, height=80)
        self.widgets.append(btn)

    def interpolar_cor(self, cor_ini, cor_fim, passo, passos=10):
        r1, g1, b1 = int(cor_ini[1:3], 16), int(cor_ini[3:5], 16), int(cor_ini[5:7], 16)
        r2, g2, b2 = int(cor_fim[1:3], 16), int(cor_fim[3:5], 16), int(cor_fim[5:7], 16)
        r = int(r1 + (r2 - r1) * (passo / passos))
        g = int(g1 + (g2 - g1) * (passo / passos))
        b = int(b1 + (b2 - b1) * (passo / passos))
        return f"#{r:02x}{g:02x}{b:02x}"

    def animar_cor(self, botao, bg_alvo, fg_alvo, passo=1):
        if not hasattr(botao, "alvo") or botao.alvo != (bg_alvo, fg_alvo): return
        botao.config(bg=self.interpolar_cor(botao.cget("bg"), bg_alvo, passo),
                     fg=self.interpolar_cor(botao.cget("fg"), fg_alvo, passo))
        if passo < 10:
            self.master.after(15, lambda: self.animar_cor(botao, bg_alvo, fg_alvo, passo + 1))

    def mouse_entrou(self, e): e.widget.alvo = ("#8a00c4", "#ffffff"); self.animar_cor(e.widget, "#8a00c4", "#ffffff")
    def mouse_saiu(self, e): e.widget.alvo = ("#2E2E2E", "#ffffff"); self.animar_cor(e.widget, "#2E2E2E", "#ffffff")

    def iniciar(self):
        self.destruir()
        self.callback_iniciar()

    def destruir(self):
        for widget in self.widgets:
            widget.destroy()