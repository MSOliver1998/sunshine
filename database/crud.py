from database.produtos import produtos

def checar_valor_database(produto,quantidade):
    for prod in produtos:
        if prod['nome']==produto:
            keys=prod.keys()
            valor_final=prod['preço']
            for k in keys:
                if k=='desconto':
                    for k,v in prod['desconto'].items():
                        if int(k) <=  int(quantidade):
                            valor_final=v
    return valor_final