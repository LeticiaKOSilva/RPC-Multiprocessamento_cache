import tkinter as tk
from tkinter import messagebox, simpledialog
import sys
from calculator import Calculator, TextRedirector

class Interface_RPC:
    def __init__(self, master):
        self.master = master
        self.master.title("Sistemas Distribuídos")

        # Adiciona um rótulo
        label = tk.Label(master, text="Escolha uma das opções abaixo:")
        label.grid(row=0, column=3, columnspan=4, padx=10, pady=10)

        # Adiciona os botões iniciais
        btn_prime = tk.Button(master, text="Número Primo", command=self.show_prime_input)
        btn_prime.grid(row=1, column=5, padx=10, pady=5)

        btn_cpf = tk.Button(master, text="Validar CPF", command=self.show_cpf_input)
        btn_cpf.grid(row=2, column=5, padx=10, pady=5)

        btn_news = tk.Button(master, text="Notícias Ifet", command=self.show_news_input)
        btn_news.grid(row=3, column=5, padx=10, pady=5)

        btn_calc = tk.Button(master, text="Operações Matemáticas", command=self.show_calculator)
        btn_calc.grid(row=4, column=5, padx=10, pady=5)

        self.operation = ""
        self.values = []
        # Centraliza a janela e atualiza as dimensões
        self.center_window()
        self.master.update_idletasks()

    def center_window(self):
        width = 300
        height = 230
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.master.geometry(f"{width}x{height}+{x}+{y}")

    def show_calculator(self):
        calculator_window = tk.Toplevel(self.master)
        calculator_window.title("Calculadora")

        # Substituir sys.stdout por um widget Text
        #output_text = tk.Text(calculator_window, wrap="none")
        #output_text.grid(row=0, column=0, padx=10, pady=10)
        #sys.stdout = TextRedirector(output_text, "stdout")
        calculator_app = Calculator(calculator_window)


    def button_click(self, value):
        current_text = self.entry.get()

        if value == 'C':
            self.entry.delete(0, tk.END)
        elif value == '=':
            try:
                operation, *values = current_text.split()
                values = list(map(float, values))
                self.operation = operation
                self.values = values
                self.return_values()
            except Exception as e:
                messagebox.showerror("Erro", "Erro ao calcular a expressão.")
        else:
            self.entry.insert(tk.END, value)

    def return_values(self):
        print("Operação:", self.operation)
        print("Valores:", self.values)

    def show_prime_input(self):
        input_value = simpledialog.askstring("Número Primo", "Digite o número:")
        try:
            number = int(input_value)
            self.operation = "is_prime"
            self.values = [number]
            self.return_values()
        except ValueError:
            messagebox.showerror("Erro", "Digite um número válido e inteiro.")

    def show_cpf_input(self):
        input_value = simpledialog.askstring("Validar CPF", "Digite o CPF:")
        if len(input_value) == 11:
            self.operation = "valida_CPF"
            self.values = [input_value]
            self.return_values()
        else:
            messagebox.showerror("Erro", "Forneça um CPF(somente número)")

    def show_news_input(self):
        input_value = simpledialog.askstring("Notícias Ifet", "Digite o número de notícias:")
        try:
            number = int(input_value)
            if number > 0:
                self.operation = "last_news_if_barbacena"
                self.values = [int(input_value)]
                self.return_values()
            else:
                messagebox.showerror("Erro", "Digite um número maior que 0.")
        except ValueError:
            messagebox.showerror("Erro", "Digite um número válido e inteiro.")
    
