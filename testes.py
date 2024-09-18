import tkinter as tk
from database.crud import *

class Listar_itens():
    def __init__(self, root,lista):
        self.root = root
        self.root.title("Exemplo de Frame com Grid")
        self.frame = None
        self.items = lista 
        self.create_frame()

    def create_frame(self):
        if self.frame:
            self.frame.destroy()
        self.frame = tk.Frame(self.root)
        self.frame.grid(row=3,column=0,columnspan=6)

        for index, item in enumerate(self.items):
            produto=item['nome']
            quantidade=item['quantidade']
            preço_unitario=item['preço']
            preço_total=preço_unitario*quantidade
    
            quantidade_label= tk.Label(self.frame,text=quantidade)
            item_label = tk.Label(self.frame, text=produto)
            valor_unitario=tk.Label(self.frame,text=preço_unitario)
            total_label=tk.Label(self.frame,text=preço_total)
            diminuir_button=tk.Button(self.frame,text='-',command=lambda item=index: self.diminuir_quantidade(item))
            adicionar_button=tk.Button(self.frame,text='+',command=lambda item=index: self.adicionar_quantidade(item))
            remove_button = tk.Button(self.frame, text="Remover", command=lambda i=index: self.remove_item(i))

            quantidade_label.grid(row=index,column=0)
            item_label.grid(row=index, column=1, padx=10, pady=5)
            valor_unitario.grid(row=index,column=2)
            total_label.grid(row=index,column=3)
            diminuir_button.grid(row=index,column=4)
            adicionar_button.grid(row=index,column=5)
            remove_button.grid(row=index, column=6, padx=10, pady=5)

    def remove_item(self, index):
        del self.items[index]
        self.create_frame() 

    def adicionar_quantidade(self,item):
        preco=checar_valor_database(self.items[item]['nome'],self.items[item]['quantidade'])
        self.items[item]['quantidade']+=1
        self.items[item]['preço']=preco
        self.create_frame()

    def diminuir_quantidade(self,item):
        if self.items[item]['quantidade']>1:
            self.items[item]['quantidade']-=1
            preco=checar_valor_database(self.items[item]['nome'],self.items[item]['quantidade'])
            self.items[item]['preço']=preco

        else:
            self.remove_item(item)
        self.create_frame()
