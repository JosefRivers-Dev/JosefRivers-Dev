import tkinter as tk
from tkinter import messagebox

class Calculadora:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculadora")

        # Entrada de texto
        self.entrada = tk.Entry(self.root, width=35, borderwidth=5)
        self.entrada.grid(row=0, column=0, columnspan=4)

        # Botones
        self.botones = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for boton in self.botones:
            tk.Button(self.root, text=boton, width=5, command=lambda boton=boton: self.click_boton(boton)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Botón de borrar
        tk.Button(self.root, text="C", width=21, command=self.borrar).grid(row=row_val, column=0, columnspan=4)

    def click_boton(self, boton):
        if boton == '=':
            try:
                resultado = eval(self.entrada.get())
                self.entrada.delete(0, tk.END)
                self.entrada.insert(tk.END, str(resultado))
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            self.entrada.insert(tk.END, boton)

    def borrar(self):
        self.entrada.delete(0, tk.END)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    calculadora = Calculadora()
    calculadora.run()