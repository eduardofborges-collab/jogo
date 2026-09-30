import tkinter as tk
from PIL import Image, ImageTk, ImageDraw, ImageFont
from componentes.fase1 import Fase1


def interpolar_cor(cor_inicial, cor_final, passo, passos_totais=10):
    r1 = int(cor_inicial[1:3], 16)
    g1 = int(cor_inicial[3:5], 16)
    b1 = int(cor_inicial[5:7], 16)

    r2 = int(cor_final[1:3], 16)
    g2 = int(cor_final[3:5], 16)
    b2 = int(cor_final[5:7], 16)

    r = int(r1 + (r2 - r1) * (passo / passos_totais))
    g = int(g1 + (g2 - g1) * (passo / passos_totais))
    b = int(b1 + (b2 - b1) * (passo / passos_totais))

    return f"#{r:02x}{g:02x}{b:02x}"


def animar_fume_para_rosa(botao, bg_alvo, fg_alvo, passo=1):

    if not botao.winfo_exists():
        return

    if not hasattr(botao, "alvo"):
        return

    if botao.alvo != (bg_alvo, fg_alvo):
        return

    proximo_bg = interpolar_cor(
        botao.cget("bg"),
        bg_alvo,
        passo
    )

    proximo_fg = interpolar_cor(
        botao.cget("fg"),
        fg_alvo,
        passo
    )

    botao.config(
        bg=proximo_bg,
        fg=proximo_fg
    )

    if passo < 10:
        janela.after(
            15,
            lambda: animar_fume_para_rosa(
                botao,
                bg_alvo,
                fg_alvo,
                passo + 1
            )
        )


def mouse_entrou(e):
    e.widget.alvo = (
        "#8a00c4",
        "#ffffff"
    )

    animar_fume_para_rosa(
        e.widget,
        "#8a00c4",
        "#ffffff"
    )


def mouse_saiu(e):
    e.widget.alvo = (
        "#2E2E2E",
        "#ffffff"
    )

    animar_fume_para_rosa(
        e.widget,
        "#2E2E2E",
        "#ffffff"
    )


def iniciar_jogo():
    for widget in janela.winfo_children():
        widget.destroy()
    Fase1(
        janela,
        largura_tela,
        altura_tela
    )


def fechar_jogo():
    janela.destroy()

janela = tk.Tk()

janela.title("FUGA DA RAVE")
janela.state("zoomed")

largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

imagem_original = Image.open(
    r"C:\Users\Aluno\jogo2\imagens\background\telainicial\background.png"
)

imagem_redimensionada = imagem_original.resize(
    (largura_tela, altura_tela),
    Image.Resampling.LANCZOS
)

fonte = ImageFont.truetype(
    r"C:\Users\Aluno\jogo2\font\BrushGrunge.ttf",
    100
)

desenho = ImageDraw.Draw(
    imagem_redimensionada
)

desenho.text(
    (100, 120),
    "FUGA DA",
    font=fonte,
    fill="#ffffff"
)


fonte2 = ImageFont.truetype(
    r"C:\Users\Aluno\jogo2\font\BrushGrunge.ttf",
    180
)

desenho.text(
    (100, 230),
    "RAVE",
    font=fonte2,
    fill="#b000ff"
)
bg_imagem_telainicial = ImageTk.PhotoImage(
    imagem_redimensionada
)

bg_imagem_telainicial_label = tk.Label(
    janela,
    image=bg_imagem_telainicial
)

bg_imagem_telainicial_label.place(
    x=0,
    y=0,
    width=largura_tela,
    height=altura_tela
)

botao_jogar = tk.Button(
    janela,
    text="▶ JOGAR",
    command=iniciar_jogo,
    bd=0,
    bg="#2E2E2E",
    fg="#ffffff",
    font=("Arial", 16, "bold"),
    activebackground="#8a00c4",
    activeforeground="#ffffff",
    cursor="hand2",
    highlightthickness=0
)

botao_jogar.bind(
    "<Enter>",
    mouse_entrou
)

botao_jogar.bind(
    "<Leave>",
    mouse_saiu
)

botao_jogar.place(
    x=100,
    y=440,
    width=250,
    height=80
)

botao_configuracao = tk.Button(
    janela,
    text="⚙️ Configuração",
    command=fechar_jogo,
    bd=0,
    bg="#2E2E2E",
    fg="#ffffff",
    font=("Arial", 16, "bold"),
    activebackground="#8a00c4",
    activeforeground="#ffffff",
    cursor="hand2",
    highlightthickness=0
)

botao_configuracao.bind(
    "<Enter>",
    mouse_entrou
)

botao_configuracao.bind(
    "<Leave>",
    mouse_saiu
)

botao_configuracao.place(
    x=100,
    y=540,
    width=250,
    height=80
)

botao_instrucoes = tk.Button(
    janela,
    text="📖 Instruções",
    command=fechar_jogo,
    bd=0,
    bg="#2E2E2E",
    fg="#ffffff",
    font=("Arial", 16, "bold"),
    activebackground="#8a00c4",
    activeforeground="#ffffff",
    cursor="hand2",
    highlightthickness=0
)

botao_instrucoes.bind(
    "<Enter>",
    mouse_entrou
)

botao_instrucoes.bind(
    "<Leave>",
    mouse_saiu
)

botao_instrucoes.place(
    x=100,
    y=640,
    width=250,
    height=80
)
botao_sair = tk.Button(
    janela,
    text="⏼ SAIR",
    command=fechar_jogo,
    bd=0,
    bg="#2E2E2E",
    fg="#ffffff",
    font=("Arial", 16, "bold"),
    activebackground="#8a00c4",
    activeforeground="#ffffff",
    cursor="hand2",
    highlightthickness=0
)

botao_sair.bind(
    "<Enter>",
    mouse_entrou
)

botao_sair.bind(
    "<Leave>",
    mouse_saiu
)

botao_sair.place(
    x=100,
    y=740,
    width=250,
    height=80
)

janela.mainloop()