from database.tables.pedidos import *

def criar_pedido(root,**pedido):
    create_pedido(**pedido)
    contato=pedido['contato']
    sinal_pago=pedido['sinal']
    import os

    pasta='pedidos'
    total=0.00
    caminho_arquivo = os.path.join(pasta, f'Sunshine-{contato}.txt')
    with open(caminho_arquivo, 'a') as arquivo:
        for item in pedido['produtos']:
            total+= (item['quantidade']*item['preço'])

        for item in pedido['produtos']:
            arquivo.write(f'{item['quantidade']} - {item['nome']} - {item['preço']:.2f} - {(item['preço']*item['quantidade']):.2f}')
            arquivo.write('\n')
    
        arquivo.write(f'| Total R$:{total:.2f} | Sinal R$: {sinal_pago:.2f} | resta: {total-sinal_pago:.2f} | \n')
    
    root.destroy()

