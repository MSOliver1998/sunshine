from database.tables.descontos import create_table_descontos
from database.tables.catalogo import create_table_catalogo
from database.tables.pedidos import create_tables_vendas
from database.tables.compras import create_tables_compras


def create_tables():
    create_table_catalogo()
    create_table_descontos()
    create_tables_vendas()
    create_tables_compras()
