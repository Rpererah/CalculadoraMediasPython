import tkinter as tk

class CalculadoraMedias:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Médias Escolares")

        self.inputs = []
        self.labels = []
        self.criar_interface()

    def criar_interface(self):
        # Criação de widgets
        tk.Label(self.root, text="Digite as notas:").grid(row=0, column=0, columnspan=2)

        # Adiciona o primeiro input com label
        self.adicionar_input()

        # Botão para calcular média
        tk.Button(self.root, text="Calcular Média", command=self.calcular_media).grid(row=3, column=2, columnspan=2)

        self.resultado_label = tk.Label(self.root, text="")
        self.resultado_label.grid(row=2, column=3, columnspan=2)

        # Botão para adicionar mais inputs
        tk.Button(self.root, text="Adicionar Nota", command=self.adicionar_input).grid(row=1, column=2)

        # Botão para remover o último input
        tk.Button(self.root, text="Remover Última Nota", command=self.remover_ultima_nota).grid(row=2, column=2)

    def adicionar_input(self):
        novo_label = tk.Label(self.root, text=f"Nota {len(self.inputs) + 1}:")
        novo_label.grid(row=len(self.inputs) + 1, column=0)

        novo_input = tk.Entry(self.root)
        novo_input.grid(row=len(self.inputs) + 1, column=1)
        
        self.labels.append(novo_label)
        self.inputs.append(novo_input)

    def remover_ultima_nota(self):
        if self.inputs:
            self.labels[-1].destroy()
            self.inputs[-1].destroy()

            del self.labels[-1]
            del self.inputs[-1]

    def calcular_media(self):
        notas = [float(entry.get()) for entry in self.inputs if entry.get()]
        if notas:
            media = sum(notas) / len(notas)
            self.resultado_label.config(text=f"Média: {media:.2f}")
        else:
            self.resultado_label.config(text="Adicione pelo menos uma nota.")

# Inicializa a aplicação
root = tk.Tk()
app = CalculadoraMedias(root)
root.mainloop()
