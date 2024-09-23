import tkinter as tk

# Configuração da interface gráfica
root = tk.Tk()
root.geometry("300x200")

# Frame footer
frame_footer = tk.Frame(root, bg="lightgrey", height=50)
frame_footer.grid(row=1, column=0, sticky="ew")
frame_footer.grid_propagate(False)

# Criação do StringVar com valor padrão
text_var = tk.StringVar(value="Texto padrão")

# Criação do Entry com o StringVar
entry_receber_total = tk.Entry(frame_footer, textvariable=text_var)
button=tk.Button(frame_footer,command=lambda: print(entry_receber_total.get())).grid()
entry_receber_total.pack(pady=10)

# Configuração do grid para expandir o conteúdo
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop()
