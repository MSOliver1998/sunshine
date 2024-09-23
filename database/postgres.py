import psycopg2
import os
from dotenv import load_dotenv

try:
    load_dotenv()

    db_password = os.getenv("DB_PASSWORD")
    # Estabelecendo a conexão
    connection = psycopg2.connect(
        host="localhost",
        database="sunshine",
        user="postgres",
        password=db_password,
        port=5432
    )

    cursor = connection.cursor()

except (Exception, psycopg2.DatabaseError) as error:
    print(f"Erro ao conectar ao PostgreSQL: {error}")
finally:
    if connection:
        print('conectado  ao DB!')
        cursor.close()
