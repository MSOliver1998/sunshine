from database.postgres import connection

def create_table_descontos():

    cursor=connection.cursor()

    create_table_query = '''
        CREATE TABLE IF NOT EXISTS descontos (
            id SERIAL PRIMARY KEY,
            prod_id int,
            quantidade VARCHAR(255) NOT NULL,
            preco FLOAT NOT NULL
        );
    '''
    cursor.execute(create_table_query)
    connection.commit()

