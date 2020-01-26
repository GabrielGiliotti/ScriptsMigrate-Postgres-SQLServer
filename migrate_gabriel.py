from Postgres_conection_gabriel import connection_postgres
from SQLServer_conection_gabriel import connection_SQL
from logreport import logger

lista_maquinas_consulta = [10]  # Lista de ids de maquinas que devemos migrar os dados
lista_response = []  # lista que recebera os dados de cada maquina

# Itera sobre a lista de ids de maquinas para realizar a consulta no banco de dados
for id_maquina in lista_maquinas_consulta:
    # Para cada maquina, vamos retornar o ultimo valor de id inserido no banco para continuarmos a inserção a partir
    # desse id, e não quebrarmos o codigo em uma segunda execucao
    query_sql = "SELECT id FROM Tabela WHERE machine_id = {0} ORDER BY id DESC OFFSET 0 ROWS FETCH NEXT 1 ROWS ONLY".format(id_maquina)

    # Parametros da funcao connection_SQL:
    # Driver de acessor
    # Server que será acessado
    # Database
    # Userid
    # Senha
    # str_query: Query que sera executada no banco
    # fetch: bool que indica se a query eh um SELECT (True) ou INSERT (False)

    last_id = connection_SQL("Driver", "Server", "Database", "UserID", "Senha", query_sql, True)
    if len(last_id) != 0:  # Se last_id que eh uma lista for diferente de vazia, passamos o where com o valor retornado
        where = 'AND hf.id > {0}'.format(last_id[0][0])  # Parte da clausula Where que deve ser inserida na conecção com postgres
    else:
        where = ''  # passamos vazio pois nao existe um primeiro id inserido no SQL Server

    # Parametros da funcao connection_postgres:
    # Host
    # Database
    # Usuario
    # Senha
    # id_maquina: id da maquina que desejamos retornar os valores (Inserir os ids em lista_maquinas_consulta)
    # limit_value: Valor limitante de quantos registros desejamos retornar do banco
    # where: Caso uma primeira consulta ja executada, envia uma restrição para puxar ids maiores que o ultimo ja migrado

    # maq recebe os dados puxados do database postgres
    maq = connection_postgres("Host", "Database", "User", "Senha", id_maquina, 1000, where)
    # e apenda os dados para cada id de maquina
    lista_response.append(maq)

count_for_query = 1  # ID que conta cada linha de dado puxada. A cada 1000 registros, devemos realizar a insercao
for rows in lista_response:  # para cada maquina, ou seja, para todos os dados de cada maquina retornado
    q_insert = "INSERT INTO Teste2 VALUES "
    for row in rows:  # Para uma unica maquina, itera sobre as dicts

        q_insert += "({},{},'{}',CONVERT(datetime,'{}',127),{},'{}',{},'{}',{},{},{},'{}',{}),".format(
            row["id"],
            row["maquina_id"],
            row["maquina_nome"],
            row["inicio"].strftime("%Y-%m-%dT%H:%M:%SZ"),
            row["op_id"],
            row["op_name"],
            row["tempo_status"],
            row["motivo_status_texto"],
            row["status_valor"],
            row["produzidas_valor"],
            row["quantidade_perdas"],
            row["motivo_perda_texto"],
            row["motivo_perda_valor"])

        # Se o numero de dados para insercao chegar a 1000, entao faz a inserção e re-seta a string para + 1000 dados
        if count_for_query % 1000 == 0:
            query_sql = q_insert[:len(q_insert) - 1] + ';'
            try:
                connection_SQL("Driver", "Server", "Database", "UserID", "Senha", query_sql, True)
                q_insert = "INSERT INTO Teste2 VALUES "
            except:
                logger.error("Erro nos dados da chamada da funcao de conexao com SQL Server")
        count_for_query += 1

    # se nao, so acessa o banco e insere os dados que faltam
    if q_insert != "INSERT INTO Teste2 VALUES ":
        query_sql = q_insert[:len(q_insert) - 1] + ';'
        connection_SQL("Driver", "Server", "Database", "UserID", "Senha", query_sql, True)
