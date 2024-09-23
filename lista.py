import tkinter as tk
from functions import *
from database.tables.produtos import *

def remover_produto(root,lista,prod,label_total):
    for widget in root.winfo_children():
        widget.destroy()
    indice=find_index(lista,'nome',prod)
    if len(lista)>0:
        lista.pop(indice)
        listar_produtos(root,lista,label_total)
    else:
        label_total['text']=f'R$: {0.00:.2f}'
        listar_produtos(root,lista,label_total)

def adicionar_produto(root,lista,prod,label_total):
    for widget in root.winfo_children():
        widget.destroy()
    indice=find_index(lista,'nome',prod)
    lista[indice]['quantidade']+=1
    preco=checar_valor_database(lista[indice]['nome'],lista[indice]['quantidade'])
    lista[indice]['preço']=preco
    listar_produtos(root,lista,label_total)

def diminuir_produto(root,lista,prod,label_total):
    for widget in root.winfo_children():
        widget.destroy()
    indice=find_index(lista,'nome',prod)
    quantidade=lista[indice]['quantidade']
    if quantidade >1:
        lista[indice]['quantidade']-=1
        preco=checar_valor_database(lista[indice]['nome'],lista[indice]['quantidade'])
        lista[indice]['preço']=preco
    else:
        lista.pop(indice)
    listar_produtos(root,lista,label_total)

def listar_produtos(root,lista,label_total):
    soma=0.00
    for widget in root.winfo_children():
        widget.destroy()
    frame_produtos=root 
    if len(lista)>0:
        for index,item in enumerate(lista):
            produto=item['nome']
            quantidade=item['quantidade']
            preço_unitario=item['preço']
            preço_total=preço_unitario*quantidade
            soma+=preço_total

            label_total['text']=f'R$:{soma:.2f}'

            label_quantidade=tk.Label(frame_produtos,text=quantidade)
            label_produtos=tk.Label(frame_produtos,text=produto)
            label_unitario=tk.Label(frame_produtos,text=f'{preço_unitario:.2f}',padx=8)
            label_subtotal=tk.Label(frame_produtos,text=f'{preço_total:.2f}',padx=8)

            botao_adicionar=tk.Button(frame_produtos, text='+',padx=8,background='green',foreground='black', command=lambda prod=produto: adicionar_produto(root,lista,prod,label_total))
            botao_diminuir=tk.Button(frame_produtos,text='-',padx=8,background='yellow',foreground='white', command=lambda prod=produto: diminuir_produto(root,lista,prod,label_total))
            botao_remover=tk.Button(frame_produtos,text='remover',padx=8,background='red',foreground='white', command=lambda prod=produto: remover_produto(root,lista,prod,label_total))

            label_quantidade.grid(row=index,column=0)
            label_produtos.grid(row=index,column=1)
            label_unitario.grid(row=index,column=2)
            label_subtotal.grid(row=index,column=3)

            botao_diminuir.grid(row=index,column=4)
            botao_adicionar.grid(row=index,column=5)
            botao_remover.grid(row=index,column=6)

    frame_produtos.grid(row=4,column=0,columnspan=6)
    return frame_produtos
