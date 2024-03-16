# Codigo do projetinho


import random
import tkinter as tk
from tkinter import messagebox

class JogoAdivinhacao:
    def __init__(self, root):
        self.numero = random.randint(1, 100)
        self.tentativas = 0

        self.label = tk.Label(root, text="Estou pensando em um número entre 1 e 100.")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.button = tk.Button(root, text="Adivinhe", command=self.adivinhar)
        self.button.pack()

    def adivinhar(self):
        palpite = self.entry.get()

        if not palpite.isdigit():
            messagebox.showinfo("Erro", "Por favor, digite um número válido.")
            return

        palpite = int(palpite)
        self.tentativas += 1

        if palpite == self.numero:
            messagebox.showinfo("Parabéns!", f"Você acertou o número em {self.tentativas} tentativas.")
        elif palpite < self.numero:
            messagebox.showinfo("Resultado", "Muito baixo! Tente novamente.")
        else:
            messagebox.showinfo("Resultado", "Muito alto! Tente novamente.")

if __name__ == "__main__":
    root = tk.Tk()
    jogo = JogoAdivinhacao(root)
    root.mainloop()
