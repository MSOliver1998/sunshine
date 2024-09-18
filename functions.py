def find_index(list,key,value):
    id=-1
    for index,val in enumerate(list):
        if(val[key]==value):
            id=index
            break
    return id


def find_by_name(list,nome):
    for item in list:
        if item['nome']==nome:
            return item
    return ''

def criar_pedido(root,lista,sinal):
    contato=sinal['contato']
    print(contato)
    sin=sinal['sinal']
    import os

    pasta='pedidos'
    total=0.00
    caminho_arquivo = os.path.join(pasta, f'Sunshine-{contato}.txt')
    with open(caminho_arquivo, 'a') as arquivo:
        for item in lista:
            total+= (item['quantidade']*item['preço'])

        for item in lista:
            print(lista)
            arquivo.write(f'{item['quantidade']} - {item['nome']} - {item['preço']:.2f} - {(item['preço']*item['quantidade']):.2f}')
            arquivo.write('\n')
        
        arquivo.write(f'| Total R$:{total:.2f} | Sinal R$: {sin:.2f} | resta: {total-sin:.2f} | \n')
    
    root.destroy()

