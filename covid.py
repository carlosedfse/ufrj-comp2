from tkinter import CENTER, Label, Tk, Entry, Button, PhotoImage
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
from tkinter.font import BOLD
from datetime import datetime

### Autor: Carlos Eduardo Freitas da Silva
### Objetivo: Trabalho final de Computação II.

"""Aplicativo para analisar a diferença de mortes entre o Brasil e alguns países de primeiro mundo.
O usuário deve inserir os dados do lado esquerdo e posteriormente clicar na bandeira de cada um dos
países para realizar a comparação. O resultado será exibido no canto inferior direito."""


"""Fórmula para calcular a diferença de mortes entre o Brasil e outros países
Para atualizar os valores, basta alterar o número de mortes (primeiro valor da divisão interna)
e o tamanho da população (segundo valor da divisão interna)"""
class MortesPaises:

    def franca(br, br2) -> int:
        return (br/br2 - 132000/67390000) * br2

    def alemanha(br, br2) -> int:
        return (br/br2 - 120000/68240000) * br2

    def espanha(br, br2) -> int:
        return (br/br2 - 95606/47350000) * br2

    def suica(br, br2) -> int:
        return (br/br2 - 12915/8637000) * br2



"""Construtor básico do aplicativo, irá posicionar cada label, entry e botões. Irá explicitar a fonte a ser utilizada,
as cores e o tamanho. Por fim, definir o conteúdo dos textos, a rota das imagens e quais funções utilizar em cada botão."""
class Aplicativo(ttk.Frame):
    def __init__(self, builder):
        super().__init__(builder)

        #### Bandeiras para inserir nos botões ###
        self.franca_flag = PhotoImage(file="./images/franca.png")
        self.alemanha_flag = PhotoImage(file="./images/alemanha.png")
        self.espanha_flag = PhotoImage(file="./images/espanha.png")
        self.suica_flag = PhotoImage(file="./images/suica.png")


        ### Valores de entrada ###
        self.msg1 = Label(text="Vítimas da Covid 19 no Brasil", font=("Century Gothic", 11, BOLD), bg="MIDNIGHTBLUE", fg="White")
        self.msg1.place(x=20, y=20)

        self.msg2 = Label(text="Tamanho da população", font=("Century Gothic", 11, BOLD), bg="MIDNIGHTBLUE", fg="White")
        self.msg2.place(x=20, y=100)

        self.vitimas = tk.StringVar()
        self.input_vitimas = ttk.Entry(width=17, textvariable=self.vitimas, font=("Century Gothic", 15, BOLD, ))
        self.input_vitimas.place(x=20, y=50)

        self.populacao = tk.StringVar()
        self.input_populacao = ttk.Entry(width=17, textvariable=self.populacao, font=("Century Gothic", 15, BOLD))
        self.input_populacao.place(x=20, y=130)


        ### Valores de saída ###
        self.resposta_label = Label(text="Vidas que poderiam ser salvas", font=("Century Gothic", 11, BOLD), bg="MIDNIGHTBLUE", fg="White")
        self.resposta_label.place(x=400, y=240)

        self.resposta_output = Entry(width=20, bg="GREEN", font=("Century Gothic", 16, BOLD))
        self.resposta_output.place(x=380, y=270, height=60)


        #### Posicionamneto dos botões e comandos a serem utilizados na classe Diferencas###
        self.franca_button = Button(image=self.franca_flag, command=lambda: Diferencas.franca_diferenca(self.input_vitimas.get(), self.input_populacao.get(), self.resposta_output))
        self.franca_button.place(x=390, y=50)

        self.alemanha_button = Button(image=self.alemanha_flag, command=lambda: Diferencas.alemanha_diferenca(self.input_vitimas.get(), self.input_populacao.get(), self.resposta_output))
        self.alemanha_button.place(x=460, y=50)

        self.espanha_button = Button(image=self.espanha_flag, command=lambda: Diferencas.espanha_diferenca(self.input_vitimas.get(), self.input_populacao.get(), self.resposta_output))
        self.espanha_button.place(x=530, y=50)

        self.suica_button = Button(image=self.suica_flag, command=lambda: Diferencas.suica_diferenca(self.input_vitimas.get(), self.input_populacao.get(), self.resposta_output))
        self.suica_button.place(x=625, y=50)

        ### Texto da área das bandeiras ###
        self.paises_label = Label(text="Comparação com outros países", font=("Century Gothic", 11, BOLD), bg="MIDNIGHTBLUE", fg="White")
        self.paises_label.place(x=400, y=20)


"""Recebe os dados da classe Aplicativo e confere se o valor inserido é um valor inteiro, caso não seja, retorna um erro para
o usuário. Caso seja um valor inteiro, a função irá chamar a função da classe MortesPaises para comparar os dados do input
com os valores fixos de cada uma das funções."""
class Diferencas:

    def franca_diferenca(vitimas: str, populacao: str, entry: Entry):
        try:
            entry.delete(0, 'end')
            valor_vitima = int(vitimas)
            valor_populacao = int(populacao)
            resposta = int(MortesPaises.franca(valor_vitima, valor_populacao))
            entry.insert(0, resposta)
        except ValueError:
            showerror(title='Error', message="O programa suporta apenas números inteiros")


    def alemanha_diferenca(vitimas: str, populacao: str, entry: Entry): 
        try:
            entry.delete(0, 'end')
            valor_vitima = int(vitimas)
            valor_populacao = int(populacao)
            resposta = int(MortesPaises.alemanha(valor_vitima, valor_populacao))
            entry.insert(0, resposta)
        except ValueError:
            showerror(title='Error', message="O programa suporta apenas números inteiros")

    def espanha_diferenca(vitimas: str, populacao: str, entry: Entry):
        try:
            entry.delete(0, 'end')
            valor_vitima = int(vitimas)
            valor_populacao = int(populacao)
            resposta = int(MortesPaises.espanha(valor_vitima, valor_populacao))
            entry.insert(0, resposta)
        except ValueError:
            showerror(title='Error', message="O programa suporta apenas números inteiros")

    def suica_diferenca(vitimas: str, populacao: str, entry: Entry):
        try:
            entry.delete(0, 'end')
            valor_vitima = int(vitimas)
            valor_populacao = int(populacao)
            resultado = int(MortesPaises.suica(valor_vitima, valor_populacao))
            entry.insert(0, resultado)
        except ValueError:
            showerror(title='Error', message="O programa suporta apenas números inteiros")


"""Construtor do aplicativo"""
class Builder(tk.Tk):
    def __init__(self):
        super().__init__()

        ### Buildando configurações básicas do APP ###
        self.title("Brasil    X    Mundo")
        self.geometry("720x400")
        self.configure(bg="MIDNIGHTBLUE")
        self.resizable(width=False, height=False)


        ### Buildando configurações do relógio digital ###
        self.relogio = self
        self.relogio_label = Label(self.relogio, font=("Century Gothic", 26, BOLD), bg="MIDNIGHTBLUE", fg="White")
        self.relogio_label.place(x=50, y=270)
        self.tictac()

    ### Atualização dos segundos, minutos e horas ###
    def tictac(self):
        hora = datetime.now()
        self.relogio_label['text'] = hora.strftime("%H:%M:%S")
        self.relogio.after(1000, self.tictac)


"""Inicializa o aplicativo"""
if __name__ == "__main__":
    app = Builder()
    Aplicativo(app)
    app.mainloop()