import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext
import sys
from calculator import Calculator, TextRedirector
import time

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

    # def show_calculator(self):
    #     calculator_window = tk.Toplevel(self.master)
    #     calculator_window.title("Calculadora")

    #     # Substituir sys.stdout por um widget Text
    #     #output_text = tk.Text(calculator_window, wrap="none")
    #     #output_text.grid(row=0, column=0, padx=10, pady=10)
    #     #sys.stdout = TextRedirector(output_text, "stdout")
    #     calculator_app = Calculator(calculator_window, self.return_values)
    #     self.operation, self.values = calculator_app.return_values()
    #     return self.return_values()

    def show_calculator(self):
        calculator_window = tk.Toplevel(self.master)
        calculator_window.title("Calculadora")

        calculator_app = Calculator(calculator_window, self.on_calculator_close)

    def on_calculator_close(self, operation, values):
        self.operation = operation
        self.values = values
        print("Received values from calculator:", self.operation, self.values)


    # def button_click(self, value):
    #     current_text = self.entry.get()

    #     if value == 'C':
    #         self.entry.delete(0, tk.END)
    #     elif value == '=':
    #         try:
    #             operation, *values = current_text.split()
    #             values = list(map(float, values))
    #             self.operation = operation
    #             self.values = values
    #             self.return_values()
    #         except Exception as e:
    #             messagebox.showerror("Erro", "Erro ao calcular a expressão.")
    #     else:
    #         self.entry.insert(tk.END, value)


    def show_prime_input(self):
        input_value = simpledialog.askstring("Número Primo", "Digite o número:")
        if input_value is not None:
            try:
                number = int(input_value)
                self.operation = "is_prime"
                self.values = [number]
                return self.return_values()
            except ValueError:
                messagebox.showerror("Erro", "Digite um número válido e inteiro.")

    def show_cpf_input(self):
        input_value = simpledialog.askstring("Validar CPF", "Digite o CPF:")

        if input_value is not None:
            if len(input_value) == 11:
                self.operation = "valida_CPF"
                self.values = [input_value]
                return self.return_values()
            else:
                messagebox.showerror("Erro", "Forneça um CPF(somente número)")

    def show_news_input(self):
        input_value = simpledialog.askstring("Notícias Ifet", "Digite o número de notícias:")
        
        if input_value is not None:
            try:
                number = int(input_value)
                if number > 0:
                    self.operation = "last_news_if_barbacena"
                    self.values = [int(input_value)]
                    return self.return_values()
                else:
                    messagebox.showerror("Erro", "Digite um número maior que 0.")
            except ValueError:
                messagebox.showerror("Erro", "Digite um número válido e inteiro.")
    

    def return_values(self):
        print("Operação:", self.operation)
        print("Valores:", self.values)
        return self.operation, self.values
    
    def print_result(self, result):
        messagebox.showinfo("Resultado Operações:", "A operação: " + str(self.values[0]) + " " + str(self.operation) + " "+ str(self.values[1])+ " é igual a= " + str(result))
    
    def print_validate_CPF(self, result):
        messagebox.showinfo("Resultado CPF", "O cpf: " + str(self.values[0]) + " é válido= " + str(result))

    def print_prime(self, result):
        messagebox.showinfo("Resultado número primo", "O número: " + str(self.values[0]) + " é primo? " + str(result))

    def print_noticias(self, result):
    #     messagebox.showinfo("Resultado Notícias Ifet:", "Número de notícias pesquisadas: " + str(self.values[0]) + "\nResultado:\n" + str(result))
        self.master = tk.Tk()
        self.master.title("Resultado Notícias Ifet")

        # Adiciona uma área de texto com barra de rolagem
        text_area = scrolledtext.ScrolledText(self.master, wrap=tk.WORD, width=150, height=40)
        text_area.pack(expand=True, fill="both")

        # Adiciona o resultado à área de texto
        text_area.insert(tk.END, "Número de notícias pesquisadas: " + str(self.values[0]) + "\nResultado:\n" + str(result))

        self.master.mainloop()