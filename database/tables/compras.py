from database.postgres import connection
from datetime import datetime
listas_de_compras=[]

def create_table_compras():
    cursor= connection.cursor()

    create_table_query='''
        CREATE TABLE IF NOT EXISTS compras(
            id SERIAL PRIMARY KEY,
            valor DECIMAL(10,2),
            created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
        );
    '''

    cursor.execute(create_table_query)
    connection.commit()


def create_table_produtos_compra():

    cursor=connection.cursor()

    create_table_query='''
        CREATE TABLE IF NOT EXISTS produtos_compra(
            id SERIAL PRIMARY KEY,
            id_produto INTEGER NOT NULL,
            id_lista INTEGER,
            quantidade INTEGER,
            CONSTRAINT fk_produto FOREIGN KEY (id_produto)
            REFERENCES catalogo (id),
            CONSTRAINT fk_lista_de_compras FOREIGN KEY(id_lista)
            REFERENCES compras (id)
        );
    '''

    cursor.execute(create_table_query)
    connection.commit()

def create_tables_compras():
    create_table_compras()
    create_table_produtos_compra()

def nova_lista_de_compras():
    global listas_de_compras
    cursor=connection.cursor()

    query_checar_lista='''
        SELECT id from produtos_compra WHERE id_lista IS NULL
    '''

    create_lista_query='''
        INSERT INTO compras(valor) VALUES(0.00) RETURNING *;
    '''
    
    query_adicionar_produto='''
        UPDATE produtos_compra
        SET id_lista = %s
        WHERE id_lista IS NULL
        RETURNING id_produto,quantidade
    '''

    query_nomear_items = '''
        SELECT pc.quantidade, c.nome
        FROM produtos_compra pc
        JOIN catalogo c ON pc.id_produto = c.id
        WHERE pc.id_lista=%s
        ORDER BY pc.id_lista;
    '''

    cursor.execute(query_checar_lista)
    ids=cursor.fetchall()

    if len(ids)>0:
        cursor.execute(create_lista_query)
        lista=cursor.fetchone()
        cursor.execute(query_adicionar_produto,(lista[0],))
        cursor.execute(query_nomear_items,(lista[0],))
        produtos=cursor.fetchall()
        connection.commit() 
        listas_de_compras.insert(0,format_lista(lista,produtos))


def inserir_na_lista(id,quantidade):

    cursor= connection.cursor()

    query_buscar_produto='''
        SELECT id from produtos_compra WHERE id_produto=%s AND id_lista IS NULL
    '''

    query_adicionar='''
        UPDATE produtos_compra
        SET quantidade = quantidade + %s
        WHERE id = %s;
    '''

    query_criar='''
        INSERT INTO produtos_compra(id_produto,quantidade) VALUES(%s,%s)
    '''

    cursor.execute(query_buscar_produto,(id,))
    produto_encontrado=cursor.fetchone()

    if produto_encontrado:
        cursor.execute(query_adicionar,(quantidade,produto_encontrado[0]))
    else:
        cursor.execute(query_criar,(id,quantidade))

    connection.commit()


def all_listas():

    cursor=connection.cursor()

    query_listas='''
        SELECT * FROM compras;
    '''

    query = '''
        SELECT pc.quantidade, c.nome
        FROM produtos_compra pc
        JOIN catalogo c ON pc.id_produto = c.id
        WHERE pc.id_lista=%s
        ORDER BY pc.id_lista;
    '''

    cursor.execute(query_listas)
    listas=cursor.fetchall()

    for lista in listas:
        cursor.execute(query,(lista[0],))
        items_lista=cursor.fetchall()
        new_lista=format_lista(lista,items_lista)
        listas_de_compras.insert(0,new_lista)


def format_lista(lista,produtos):

    _lista={
        'id':lista[0],
        'total':lista[1],
        'data':f'{lista[2].strftime("%d/%m/%Y")}',
        'items':[]
    }

    for item in produtos:
        _lista['items'].append(item)

    return _lista