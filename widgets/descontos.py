import tkinter as tk

def adicionar_desconto(frame):
    row = len(frame.winfo_children()) // 3 + 1
    if row<20:
        entry_quantidade = tk.Entry(frame,width=8)
        entry_valor = tk.Entry(frame,width=8)
        button_excluir = tk.Button(frame, text='-', background='red')

        def excluir(entry_quantidade=entry_quantidade, entry_valor=entry_valor, button_excluir=button_excluir):
            entry_quantidade.destroy()
            entry_valor.destroy()
            button_excluir.destroy()

        button_excluir.config(command=excluir)

        entry_quantidade.grid(row=row, column=0)
        entry_valor.grid(row=row, column=1)
        button_excluir.grid(row=row, column=2)