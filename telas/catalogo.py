import tkinter as tk
from colors import catalogo 
from telas.framesCatalogo.adicionar_produto import frame_adicionar_produto 
from telas.framesCatalogo.remover_produto import frame_remover_produto
from telas.framesCatalogo.editar_produtos import frame_editar_produto

def frame_catalogo(root):

    buttons_frames=tk.Frame(root,background=catalogo)
    
    button_add=tk.Button(buttons_frames,text='Novo',command=lambda:f1.tkraise())
    button_edt=tk.Button(buttons_frames,text='Editar',command=lambda:f2.tkraise())
    button_del=tk.Button(buttons_frames,text='Deletar',command=lambda:f3.tkraise())

    frame_option=tk.Frame(root,background='green',width=300,height=300)

    f1= frame_adicionar_produto(buttons_frames)
    f2= frame_editar_produto(buttons_frames)
    f3= frame_remover_produto(buttons_frames)
 
    for frame in (f1,f2,f3):
        frame.grid(row=1, column=0,columnspan=4, sticky='news')

    f1.tkraise()

    frame_option.grid(row=1,column=0,columnspan=6)

    button_add.grid(row=0,column=0)
    button_edt.grid(row=0,column=1)
    button_del.grid(row=0,column=3)

    return buttons_frames