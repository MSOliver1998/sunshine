from database.postgres import connection
lista_de_produtos=[]

def create_table_catalogo():
    cursor=connection.cursor()

    create_table_query = '''
        CREATE TABLE IF NOT EXISTS catalogo (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(255) NOT NULL,
            preco FLOAT NOT NULL
        );
    '''
    cursor.execute(create_table_query)
    connection.commit()

def checar_valor_database(produto,quantidade):
    global lista_de_produtos
    produtos=lista_de_produtos
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

def add_prod(prod):

    global lista_de_produtos
    cursor = connection.cursor()

    # Adicionando itens à tabela de produtos
    insert_produtos_query = '''
        INSERT INTO catalogo (nome, preco) VALUES (%s, %s) RETURNING id;
    '''

    insert_desconto_query='''
        INSERT INTO descontos (quantidade,prod_id,preco) VALUES (%s,%s,%s);
    '''

    cursor.execute(insert_produtos_query, (prod['nome'],prod['preço']))

    new_id = cursor.fetchone()[0]
    prod['id']=new_id

    for des in prod['desconto']:
        key=des
        value=prod['desconto'][des]
        cursor.execute(insert_desconto_query, (key,new_id,value))

    # Confirmar as mudanças
    connection.commit()
    cursor.close()
    lista_de_produtos.append(prod)

def select_all():

    global lista_de_produtos

    cursor=connection.cursor()

    cursor.execute('SELECT * FROM catalogo')
    produtos=cursor.fetchall()

    cursor.close()
    cursor=connection.cursor()

    for produto in produtos:
        cursor.execute(f'SELECT * FROM descontos where prod_id={produto[0]}')
        descontos=cursor.fetchall()
        lista_de_descontos={}
        for desconto in descontos:
            lista_de_descontos[desconto[2]]=desconto[3]
        lista_de_produtos.append({
            'id':produto[0],
            'nome':produto[1],
            'preço':produto[2],
            'desconto':lista_de_descontos
        })

    return lista_de_produtos

def edit_prod(id,produto):
    novo_nome=produto['nome']
    novo_preco=produto['preço']
    cursor = connection.cursor()

    update_query = '''UPDATE catalogo SET nome = %s, preco = %s WHERE id = %s'''

    cursor.execute(update_query, (novo_nome, novo_preco, id))
    connection.commit()

    cursor.close()
    connection.close()

def del_prod(prod_nome):
    global lista_de_produtos
    query="SELECT id FROM catalogo WHERE nome = %s"
    cursor=connection.cursor()
    cursor.execute(query,(prod_nome,))
    produtos_encontrados=cursor.fetchall()

    for produto in lista_de_produtos:
        if produto['nome']==prod_nome:
            lista_de_produtos.remove(produto)

    for produto in produtos_encontrados:
        id=produto[0]
        cursor.execute(f"DELETE FROM descontos WHERE prod_id={id}")
        cursor.execute(f'DELETE FROM catalogo WHERE id={id}') 
    connection.commit()