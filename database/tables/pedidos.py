from database.postgres import connection
from database.tables.catalogo import lista_de_produtos
from database.tables.compras import inserir_na_lista
lista_de_pedidos=[]

def create_table_pedidos():

    cursor=connection.cursor()

    create_table_query = '''
        CREATE TABLE IF NOT EXISTS pedidos(
            id SERIAL PRIMARY KEY,
            contato VARCHAR(12),
            nome VARCHAR(255) NOT NULL,
            total DECIMAL(10, 2),
            sinal_pago DECIMAL(10, 2), 
            created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
            updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW() 
        );
    '''
    cursor.execute(create_table_query)
    connection.commit()


def create_table_items():
    cursor=connection.cursor()

    create_table_query = '''
        CREATE TABLE IF NOT EXISTS items(
            id SERIAL PRIMARY KEY,
            id_pedido INTEGER NOT NULL,
            id_produto INTEGER NOT NULL,
            quantidade INTEGER NOT NULL,
            preco NUMERIC(10, 2) NOT NULL,
            FOREIGN KEY (id_pedido) REFERENCES pedidos (id) ON DELETE CASCADE,
            FOREIGN KEY (id_produto) REFERENCES catalogo (id) ON DELETE CASCADE
        );
    '''
    cursor.execute(create_table_query)
    connection.commit()


def create_tables_vendas():
    create_table_pedidos()
    create_table_items()

def create_pedido(**pedido):
    global lista_de_pedidos
    global lista_de_produtos
    sinal,nome,contato,produtos,total=pedido.values()
    cursor=connection.cursor()
    create_pedido_query='''
        INSERT INTO pedidos(contato,nome,total,sinal_pago) VALUES(%s,%s,%s,%s) RETURNING id,created_at;
    '''

    create_items_query='''
        INSERT INTO items(id_pedido,id_produto,quantidade,preco) VALUES(%s,%s,%s,%s) RETURNING *
    '''
    cursor.execute(create_pedido_query,(contato,nome,total,sinal))
    connection.commit()

    returning_new_pedido = cursor.fetchone()
    id_pedido=returning_new_pedido[0]
    data_pedido=returning_new_pedido[1]

    pd={
            'id':id_pedido,
            'contato':pedido['contato'],
            'cliente':pedido['nome'],
            'valor_total':pedido['total'],
            'valor_sinal':pedido['sinal'],
            'data_do_pedido':data_pedido,
            'produtos':[]
        }

    for item in produtos:
        for produto in lista_de_produtos:
            if produto['nome']==item['nome']:
                prod_id=produto['id']
                cursor.execute(create_items_query,(id_pedido,prod_id,item['quantidade'],item['preço']))
                connection.commit()
                new_item=cursor.fetchone()
                inserir_na_lista(new_item[2],new_item[3])
                pd['produtos'].append(new_item)
            
    lista_de_pedidos.insert(0,pd)

def receber_sinal(id,valor):
    global lista_de_pedidos
    cursor=connection.cursor()
    editar_sinal_query='''
        UPDATE pedidos
        SET sinal_pago = sinal_pago + %s
        WHERE id=%s
        returning *;
    ''' 

    cursor.execute(editar_sinal_query,(valor,id))
    connection.commit()

def select_all_pedidos():
    global lista_de_pedidos
    cursor=connection.cursor()
    select_all_query='''
        SELECT * FROM pedidos;
    '''

    select_items_query='''
        SELECT * FROM items;
    '''
    cursor.execute(select_all_query)
    pedidos=cursor.fetchall()

    cursor.execute(select_items_query)
    items=cursor.fetchall()
    for pedido in pedidos:
        pd={
            'id':pedido[0],
            'contato':pedido[1],
            'cliente':pedido[2],
            'valor_total':pedido[3],
            'valor_sinal':pedido[4],
            'data_do_pedido':pedido[5],
            'produtos':[]
        }
        for item in items:
            if pedido[0]==item[1]:
                pd['produtos'].append(item) 
        lista_de_pedidos.insert(0,pd)
