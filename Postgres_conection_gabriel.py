import psycopg2.extras


def connection_postgres(host, database, usuario, senha, id_maquina, limit_value, where):
    
    conn = psycopg2.connect(host=host, database=database, user=usuario, password=senha)
    
    query = """Query no Banco""".format(id_maquina, limit_value, where)
    
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    
    cursor.execute(query)

    db_select = cursor.fetchall()

    conn.commit()

    return db_select
