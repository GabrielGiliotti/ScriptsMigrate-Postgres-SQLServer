import pyodbc


def connection_SQL(driver, server, database, userid, senha, str_query, fetch):
    if database == "":
        database = " "

    connection = "Driver={};SERVER={};DATABASE={};UID={};PWD={};".format(driver, server, database, userid, senha)

    conn = pyodbc.connect(connection)

    cursor = conn.cursor()
    cursor.execute(str_query)

    if fetch:  # fetch eh um bool indicando se a chamada da consulta eh um select ou um insert
        db_q = cursor.fetchall()  # Se for um SELECT, deve entrar fazer fetchall(), caso contrario deve pular esse passo
        conn.commit()
        return db_q

    conn.commit()
