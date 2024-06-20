import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext
import sys
from calculator import Calculator, TextRedirector
import time

'''
    Interface gráfica principal do programa na parte do cliente.
    
    Possui os botões: 
    -Número primo
    -Validar CPF
    - Notícia do Ifet
    - Operações Matemáticas
    -Sair

    Por essa interface ser a principal o programa no lado do cliente só acabará 
    quando o usuário fechar essa inteface. Existem 2 flags de saáda, sendo eles:
    o botão "Sair" e o "X" posicionado no canto direito da interface.
'''
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

        btn_exit = tk.Button(master, text="Sair", command=self.exit)
        btn_exit.grid(row=5, column=5, padx=10, pady=5)

        self.operation_callback = None
        self.operation = ""
        self.values = []
        # Centraliza a janela e atualiza as dimensões
        self.center_window()
        self.master.update_idletasks()

    
    #Posiciona a janela no centro da tela
    def center_window(self):
        #Cálculo da largura e altura da janela
        width = 300
        height = 230
        #Cálculo da largura e altura da tela
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        #Cálculo das coordenadas para que a janela fique centralizada
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        #Definição da geometria da janela
        self.master.geometry(f"{width}x{height}+{x}+{y}")

    ''' 
        Define um callback, que será acionado somente quando uma operação da interface
        for precionada pelo usuário, com isso a lógica por traz das operções funciona
        corretamente sem ser necessário fechar a interface principal.
    '''
    def set_operation_callback(self, callback):
        self.operation_callback = callback

    def show_calculator(self):
        calculator_window = tk.Toplevel(self.master)
        calculator_window.title("Calculadora")
        calculator_app = Calculator(calculator_window, self.on_calculator_close)

    def on_calculator_close(self, operation, values):
        self.operation = operation
        self.values = values
        print("Received values from calculator:", self.operation, self.values)
        if self.operation_callback:
            self.operation_callback(self.operation, self.values)

    def exit(self):
        try:
            self.master.destroy()
        except Exception as e:
            print("Erro ao tentar encerrar a interface!")
        finally:
            sys.exit(0)
        
    def show_prime_input(self):
        input_value = simpledialog.askstring("Número Primo", "Digite o número:")
        if input_value is not None:
            try:
                number = int(input_value)
                self.operation = "is_prime"
                self.values = [number]
                if self.operation_callback:
                    self.operation_callback(self.operation, self.values)
            except ValueError:
                messagebox.showerror("Erro", "Digite um número válido e inteiro.")

    def show_cpf_input(self):
        input_value = simpledialog.askstring("Validar CPF", "Digite o CPF:")

        if input_value is not None:
            if len(input_value) == 11:
                self.operation = "valida_CPF"
                self.values = [input_value]
                if self.operation_callback:
                    self.operation_callback(self.operation, self.values)
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
                    if self.operation_callback:
                        self.operation_callback(self.operation, self.values)
                else:
                    messagebox.showerror("Erro", "Digite um número maior que 0.")
            except ValueError:
                messagebox.showerror("Erro", "Digite um número válido e inteiro.")
    
    def return_values(self):
        print("Operação:", self.operation)
        print("Valores:", self.values)
        return self.operation, self.values
    
    def print_result(self, result):
        messagebox.showinfo("Resultado Operações:", "A operação: " + str(self.values[0]) + " " + str(self.operation) + " " + str(self.values[1]) + " é igual a= " + str(result))
    
    def print_validate_CPF(self, result):
        messagebox.showinfo("Resultado CPF", "O cpf: " + str(self.values[0]) + " é válido= " + str(result))

    def print_prime(self, result):
        messagebox.showinfo("Resultado número primo", "O número: " + str(self.values[0]) + " é primo? " + str(result))

    def print_noticias(self, result):
        result_window = tk.Toplevel(self.master)
        result_window.title("Resultado Notícias Ifet")

        # Adiciona uma área de texto com barra de rolagem
        text_area = scrolledtext.ScrolledText(result_window, wrap=tk.WORD, width=150, height=40)
        text_area.pack(expand=True, fill="both")

        # Adiciona o resultado à área de texto
        text_area.insert(tk.END, "Número de notícias pesquisadas: " + str(self.values[0]) + "\nResultado:\n" + str(result))
        result_window.mainloop()
