import tkinter as tk
from tkinter import messagebox, simpledialog

'''
    Monta a interface gráfica de uma calculadora simples
    com operações de "+", "-", "*" e "/".
    A interface é utilizada quando o usuário na interface principal
    preciona o botão de "Operações Matemáticas". 
'''
class Calculator:
    def __init__(self, master, callback):
        self.master = master
        self.callback = callback

        self.master.title("Calculadora")

        self.operation = ""
        self.values = []

        self.entry = tk.Entry(master, font=('Arial', 14))
        self.entry.grid(row=0, column=0, columnspan=4, pady=10)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+'
        ]

        row_val = 1
        col_val = 0
        for button in buttons:
            tk.Button(master, text=button, width=5, height=2, font=('Arial', 12),
                      command=lambda b=button: self.button_click(b)).grid(row=row_val, column=col_val, padx=5, pady=5)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        self.master.grid_columnconfigure(0, weight=1)
        self.center_window()
        self.master.update_idletasks()

    #Calcula o posicionamento e tamanho da interface gráfica e o tamanho da tela. 
    def center_window(self):
        width = 290
        height = 300
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.master.geometry(f"{width}x{height}+{x}+{y}")
    
    
    #Armazena todo o conteúdo escolhido pelo usuário
    def button_click(self, value):
       
        current_text = self.entry.get()
        
        # Precionando C o espaço preenchedo é deletado 
        if value == 'C':
            self.entry.delete(0, tk.END)
        elif value == '=':
            '''
                Quando o usuário preciona "=" separa-se o tipo da operação "+-*/" e os valores.

                OBS:
                        - Se o usuário digitar "10-12-15" o programa seguirá normalmente porém considerando 
                    só os 2 primeiros valores "10 e 12" é será assim com qualquer outra operação repetida.

                        - Se o usuário digitar "10-12*15" o programa irá considerar que a um erro porque temos 
                    dois operadores diferentes por isso a mensagem "Erro ao calcular a expressão" será printada 
                    na tela e nenhuma operação será realizada. 
            '''    
            try:
                # Extrai o sinal da operação
                operation = [char for char in current_text if char in "+-*/"][0]
                # Extraindo os valores
                values = list(map(float, current_text.split(operation)))

                self.operation = operation
                self.values = values

                self.callback(self.operation, self.values)
                self.close()

            except Exception as e:
                messagebox.showerror("Erro", "Erro ao calcular a expressão.")
                self.close()
        else:
            self.entry.insert(tk.END, value)

    def return_values(self):
        print("Operação:", self.operation)
        print("Valores:", self.values)
        return self.operation, self.values

    def close(self):
        self.master.destroy()


'''
    Classe Auxiliar que fará o redirecionamento da saída padrão
    "stdout" para um "widget" de texto do tkinter.
    Com isso as saídas que seriam exibidas no console agora são
    exibidas em um widget de texto na interface gráfica do usuário.
'''
class TextRedirector:
    def __init__(self, widget, tag="stdout"):
        # "text" ou "ScrolledText" onde o texto será exibido 
        self.widget = widget
        # String que identifica a tag para  texto a ser inserido. OBS(Pode ser usada para estilizar o texto também)
        self.tag = tag

    def write(self, str):
        self.widget.configure(state="normal")
        self.widget.insert("end", str, (self.tag,))
        self.widget.configure(state="disabled")
