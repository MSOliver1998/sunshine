import tkinter as tk
from database.tables.catalogo import *
from colors import vendas
from functions import *
from lista import *
from widgets.menu_option import *
from widgets.options import options

def finalizar_venda(frame,lista):

    total=0.00
    for item in lista:
        total+=item['quantidade']*item['preço']

    def gerar_pedido():
        contato=input_contato.get()
        nome=input_nome.get()
        sinal=float(input_sinal.get())
        pedido={'sinal':sinal,'nome':nome,'contato':contato,"produtos":lista[:],'total':total}
        for widgets in frame.winfo_children():
            widgets.destroy()
        lista.clear()
        return pedido

    root=tk.Tk()
    root.geometry('300x300')
    root.title('finalizar venda')
    label_recomendado_1=tk.Label(root,text='Recomendado')
    label_recomendado=tk.Label(root,text=f'R$: {total/2:.2f}')    
    label_sinal=tk.Label(root,text='Sinal')
    input_sinal=tk.Entry(root,width=8)
    label_nome=tk.Label(root,text='Nome')
    input_nome=tk.Entry(root)
    label_contato=tk.Label(root,text='Contato')
    input_contato=tk.Entry(root)
    button_confirmar=tk.Button(root,text='Confirmar',background='green', command= lambda: (criar_pedido(root,**gerar_pedido())))

    label_recomendado_1.grid(row=0,column=0)
    label_recomendado.grid(row=1,column=0)
    label_sinal.grid(row=0,column=1)
    input_sinal.grid(row=1,column=1)
    label_nome.grid(row=0,column=2)
    input_nome.grid(row=1,column=2)
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
    global options

    def selecionar_opcao(label_total,frame):
        quantidade = entry_unidades.get()
        prod=opcao_selecionada.get()
        opcao_selecionada.set(opcao_selecionada.get())
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

    frame=tk.Frame(root,background=vendas,height=600,width=600)
    menu,opcao_selecionada=menu_option(frame)
    label_unidades=tk.Label(frame,text="unidades",background=vendas)
    entry_unidades=tk.Entry(frame,width=10)
    label_produto=tk.Label(frame,text="produto",width=20)
    menu_opcoes = menu
    options.append(menu_opcoes)
    frame_lista_de_produtos=tk.Frame(frame)
    botao_adicionar=tk.Button(frame,text='+',background="#7CFC00",foreground="#98FB98",command=lambda: (selecionar_opcao(label_total,frame_lista_de_produtos)))
    botao_finalizar=tk.Button(frame,text="finalizar",background='#B0E0E6',command=lambda: finalizar_venda(frame_lista_de_produtos,lista))
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
