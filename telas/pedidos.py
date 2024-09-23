import tkinter as tk
from colors import pedidos
from database.tables.pedidos import *
from PIL import ImageTk, Image
import os

def alterar_valores(pedido,valor_recebido,*frames):
    label_sinal,label_restante=frames

    if float(valor_recebido)>pedido['valor_total']-pedido['valor_sinal']:
        valor_recebido=pedido['valor_total']-pedido['valor_sinal']
    pedido['valor_sinal']+=float(valor_recebido)
    
    label_sinal.config(text=f'Sinal:\nR${pedido['valor_sinal']:.2f}')
    label_restante.config(text=f'Resta:\nR${pedido['valor_total']-pedido['valor_sinal']:.2f}')

    receber_sinal(pedido['id'],valor_recebido)

def detalhar_pedido(pedido):
    caminho_imagem = os.path.join(os.path.dirname(__file__),'..', 'assets', 'logo.png')
    img=None

    root=tk.Tk()
    root.geometry('300x300')
    root.title('PEDIDO')
    frame_cabecalho=tk.Frame(root)

    frame_informacoes=tk.Frame(frame_cabecalho)
    label_data=tk.Label(frame_informacoes,text=f'Data: {pedido['data_do_pedido'].strftime("%d/%m/%Y")}')
    label_nome=tk.Label(frame_informacoes,text=f'Nome: {pedido['cliente']}')
    label_contato=tk.Label(frame_informacoes,text=f'Contato: {pedido['contato']}')
    label_total=tk.Label(frame_informacoes,text=f'Total:\nR${pedido['valor_total']:.2f}',padx=5)
    label_sinal=tk.Label(frame_informacoes,text=f'Sinal:\nR${pedido['valor_sinal']:.2f}',padx=5)
    label_resta=tk.Label(frame_informacoes,text=f'Resta:\nR${pedido['valor_total']-pedido['valor_sinal']:.2f}',padx=5)

    frame_produtos=tk.Frame(root,pady=18)

    for index,item in enumerate(pedido['produtos']):
        for produto in lista_de_produtos:
            if item[2]==produto['id']:
                label_quantidade=tk.Label(frame_produtos,text=item[3])
                label_produto=tk.Label(frame_produtos,text=f'{produto['nome']}')
                label_preco=tk.Label(frame_produtos,text=f'R$:{item[4]:.2f}')
                label_sub_total=tk.Label(frame_produtos,text=f'R$: {item[4]*item[3]:.2f}')

    frame_footer=tk.Frame(root,background='red')
    text_var = tk.StringVar(value=f'{pedido['valor_total']-pedido['valor_sinal']:.2f}')
    entry_receber_total = tk.Entry(frame_footer, textvariable=text_var,width=18)
    button_receber_restante=tk.Button(frame_footer,text='receber', command=lambda: alterar_valores(pedido,entry_receber_total.get(),label_sinal,label_resta))

    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(0, weight=1)

    frame_informacoes.grid(row=0,column=2)
    label_data.grid(row=0,column=0)
    label_nome.grid(row=1,column=0)
    label_contato.grid(row=1,column=1)
    label_total.grid(row=2,column=0)
    label_sinal.grid(row=2,column=1)
    label_resta.grid(row=2,column=2)

    frame_produtos.grid(row=1,column=0,sticky='wesn')
    label_quantidade.grid(row=index,column=0)
    label_produto.grid(row=index,column=1)
    label_preco.grid(row=index,column=2)
    label_sub_total.grid(row=index,column=3)

    frame_footer.grid(row=4,column=0,sticky='we')
    entry_receber_total.grid(row=0,column=0)
    button_receber_restante.grid(row=0,column=1)

    try:
        img = ImageTk.PhotoImage(Image.open(caminho_imagem))
        label_logo = tk.Label(frame_cabecalho, image=img)
        label_logo.grid(row=0,column=0)
    except Exception as e:
        print(f"Erro ao abrir a imagem: {e}")
 
    label_loja=tk.Label(frame_cabecalho,text='Sunshine')
    label_loja.grid(row=0,column=1)
    frame_cabecalho.grid(row=0,column=0)

def listar_pedidos(frame):
    global lista_de_pedidos

    for widget in frame.winfo_children():
        widget.destroy()

    for index,pedido in enumerate(lista_de_pedidos):
        label_cliente=tk.Label(frame,text=f'{pedido['cliente'].capitalize()}',padx=10)
        label_total=tk.Label(frame,text=f'R$:{pedido['valor_total']:.2f}',padx=10)
        label_sinal=tk.Label(frame,text=f'R$:{(pedido['valor_total']-pedido['valor_sinal']):.2f}',padx=10)
        label_data=tk.Label(frame,text=f'{pedido['data_do_pedido'].strftime("%d/%m/%Y %H:%M")}',padx=10)
        button_detalhes=tk.Button(frame,text='Detalhes')
        button_detalhes.config(command=lambda ped=pedido: detalhar_pedido(ped))

        label_cliente.grid(row=index,column=0)
        label_total.grid(row=index,column=1)
        label_sinal.grid(row=index,column=2)
        label_data.grid(row=index,column=3)
        button_detalhes.grid(row=index,column=4)

    return  frame

def frame_pedidos(root):
    select_all_pedidos()
    frame = tk.Frame(root, background=pedidos)

    # Header fixo
    header_frame = tk.Frame(frame)
    header_frame.grid(row=0, column=0, sticky='ew')

    label_nome = tk.Label(header_frame, text='Cliente')
    label_total = tk.Label(header_frame, text='Total')
    label_restante = tk.Label(header_frame, text='Resta')
    label_data = tk.Label(header_frame, text='Data')

    label_nome.grid(row=0, column=0, sticky='news')
    label_total.grid(row=0, column=1, sticky='news',padx=40)
    label_restante.grid(row=0, column=2, sticky='news',padx=20)
    label_data.grid(row=0, column=3, sticky='news',padx=20)

    # Cria um canvas e uma scrollbar
    canvas = tk.Canvas(frame,width=500,height=500)
    scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    listar_pedidos(scrollable_frame)

    canvas.grid(row=1, column=0, sticky="nsew",columnspan=6)
    scrollbar.grid(row=1, column=1, sticky="ns")

    frame.grid_rowconfigure(1, weight=1)
    frame.grid_columnconfigure(0, weight=1)

    return frame