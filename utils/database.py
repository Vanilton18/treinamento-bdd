import psycopg2
from psycopg2 import sql

dbname = "shop-bdd"
user = "postgres"
password = "123456"
host = "localhost"
port = "5432"


def clean_category():
    global connection, cursor
    try:
        connection = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )

        cursor = connection.cursor()
        table_names = ["api_product_category", "api_category"]
        condition_value = "1 = 1"

        for table_name in table_names:
            delete_query = sql.SQL("DELETE FROM {} ;").format(
                sql.Identifier(table_name)
            )
            cursor.execute(delete_query, (condition_value,))

        connection.commit()

        print("DELETE operation successful!")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()
