import tkinter as tk
from database.produtos import produtos as dt
from database.crud import *
from colors import vendas
from tkinter import ttk
from functions import *
from lista import *
from testes import *

def finalizar_venda(lista,frame,total):

    def valor_do_sinal():
        contato=input_contato.get()
        sinal=int(input_sinal.get())
        return {'sinal':sinal,'contato':contato}

    total=0.00
    for item in lista:
        total+= (item['quantidade']*item['preço'])/2

    root=tk.Tk()
    root.geometry('300x300')
    root.title('finalizar venda')

    label_recomendado_1=tk.Label(root,text='Recomendado')
    label_recomendado=tk.Label(root,text=f'R$: {total:.2f}')    
    label_sinal=tk.Label(root,text='Sinal')
    input_sinal=tk.Entry(root)
    label_resta=tk.Label(root,text='Resta')
    label_contato=tk.Label(root,text='contato')
    input_contato=tk.Entry(root)
    button_confirmar=tk.Button(root,text='Confirmar',background='green', command= lambda: (criar_pedido(root,lista,valor_do_sinal()),listar_produtos(frame,[],total)))

    label_recomendado_1.grid(row=0,column=0)
    label_recomendado.grid(row=1,column=0)
    label_sinal.grid(row=0,column=1)
    input_sinal.grid(row=1,column=1)
    label_resta.grid(row=0,column=2)
    label_contato.grid(row=0,column=3)
    input_contato.grid(row=1,column=3)
    button_confirmar.grid(row=2,column=0)
    root.mainloop()

def calcular_total(lista,frame_total):
    total=0.00
    for item in lista:
        total+=item['quantidade']*item['preço']
    frame_total['text']=f'{total:.2f}'


def frame_vendas(root):
    total=0.00
    def selecionar_opcao(label_total):
        quantidade = entry_unidades.get()
        prod=opcao_selecionada.get()
        preco=checar_valor_database(prod,quantidade)
        if(len(lista)==0):
            lista.append({
                "nome":prod,
                "quantidade":int(quantidade),
                "preço": preco
            })
        else:
            find=-1
            for index,produto in enumerate(lista):
                if(produto['nome']==prod):
                    find=int(index)
                    lista[index]['quantidade']+= int(quantidade)
                    lista[index]['preço']=checar_valor_database(prod,lista[index]['quantidade'])
                    break
                
            if(find==-1):
                lista.append({
                    "nome":prod,
                    "quantidade":int(quantidade),
                    'preço': preco
                })
        listar_produtos(frame,lista,label_total)

    lista=[]
    opcoes = ["selecionar"]

    for i in dt:
        opcoes.append(i['nome'])

    opcao_selecionada = tk.StringVar()
    opcao_selecionada.set(opcoes[0])
    frame=tk.Frame(root,background=vendas,height=600,width=600)
    label_unidades=tk.Label(frame,text="unidades",background=vendas)
    entry_unidades=tk.Entry(frame,width=10)
    label_produto=tk.Label(frame,text="produto",width=20)
    menu_opcoes = ttk.OptionMenu(frame, opcao_selecionada, *opcoes)
    botao_adicionar=tk.Button(frame,text='+',background="#7CFC00",foreground="#98FB98",command=lambda: (selecionar_opcao(label_total)))
    botao_finalizar=tk.Button(frame,text="finalizar",background='#B0E0E6',command=lambda:finalizar_venda(lista,frame,label_total))
    label_total=tk.Label(frame,text=f'R$: {total:.2f}')

    quantidade=tk.Label(frame,text='QTD')
    produto=tk.Label(frame,text='PRODUTO')
    valor_unitario=tk.Label(frame,text='UNIT')
    sub_total=tk.Label(frame,text='SUB TOTAL')

    label_unidades.grid(row=0,column=0)
    entry_unidades.grid(row=1,column=0)

    label_produto.grid(row=0,column=1)
    menu_opcoes.grid(row=1,column=1)

    botao_adicionar.grid(row=1,column=2)
    botao_finalizar.grid(row=1,column=3)
    label_total.grid(row=1,column=4)

    quantidade.grid(row=3,column=0)
    produto.grid(row=3,column=1)
    valor_unitario.grid(row=3,column=2)
    sub_total.grid(row=3,column=3)

    return frame
