from database.tables.descontos import create_table_descontos
from database.tables.produtos import create_table_produtos
from database.tables.pedidos import *

def create_tables():
    create_table_produtos()
    create_table_descontos()
    create_table_pedidos()
    create_table_items()
