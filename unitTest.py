import unittest
from Postgres_conection_gabriel import connection_postgres
from SQLServer_conection_gabriel import connection_SQL


# Devemos testar funções e possiveis respostas que podemos receber de uma função
# 1-) Criar uma classe que testa e herda de unittest.TestCase, como no exemplo abaixo
# 2-) Cada função é considerada um test, mas dentro de cada função/test você pode testar mais de um caso/item.


class TestConections(unittest.TestCase):
    def testPostgreConectionOne(self):
        try:
            connection_postgres("", "database", "usuario", "senha", 10, 1000, "")
            teste = 1
        except:
            teste = 0
        self.assertTrue(bool(teste), msg="Teste 1 (Postgre) veio true (1), mas esperava falso (0).")

    def testPostgreConectionTwo(self):
        try:
            connection_postgres("host", "", "usuario", "senha", 10, 1000, "")
            teste = 1
        except:
            teste = 0
        self.assertFalse(bool(teste), msg="Teste 2 (Postgre) veio true (1), mas esperava falso (0).")

    def testPostgreConectionThree(self):
        try:
            connection_postgres("host", "database", "", "senha", 10, 1000, "")
            teste = 1
        except:
            teste = 0
        self.assertFalse(bool(teste), msg="Teste 3 (Postgre) veio true (1), mas esperava falso (0).")

    def testPostgreConectionFour(self):
        try:
            connection_postgres("host", "database", "usuario", "", 10, 1000, "")
            teste = 1
        except:
            teste = 0
        self.assertFalse(bool(teste), msg="Teste 4 (Postgre) veio true (1), mas esperava falso (0).")

    def testPostgreConectionFive(self):
        try:
            connection_postgres("host", "database", "usuario", "senha", "", 1000, "")
            teste = 1
        except:
            teste = 0
        self.assertFalse(bool(teste), msg="Teste 5 (Postgre) veio true (1), mas esperava falso (0).")

    def testPostgreConectionSix(self):
        try:
            connection_postgres("host", "database", "usuario", "senha", 10, "", "")
            teste = 1
        except:
            teste = 0
        self.assertFalse(bool(teste), msg="Teste 6 (Postgre) veio true (1), mas esperava falso (0).")

    def testPostgreConectionSeven(self):
        self.assertTrue(connection_postgres("host", "database", "usuario", "senha", 10, 10, ""))
        self.assertTrue(connection_postgres("host", "database", "usuario", "senha", 10, 100, ""))
        self.assertTrue(connection_postgres("host", "database", "usuario", "senha", 10, 1000, ""))
        self.assertTrue(connection_postgres("host", "database", "usuario", "senha", 10, 10000, ""))

        self.assertTrue(connection_postgres("host", "database", "usuario", "senha", 14, 10, ""))
        self.assertTrue(connection_postgres("host", "database", "usuario", "senha", 14, 100, ""))
        self.assertTrue(connection_postgres("host", "database", "usuario", "senha", 14, 1000, ""))
        self.assertTrue(connection_postgres("host", "database", "usuario", "senha", 14, 10000, ""))

        self.assertTrue(connection_postgres("host", "database", "usuario", "senha", 16, 10, ""))
        self.assertTrue(connection_postgres("host", "database", "usuario", "senha", 16, 100, ""))
        self.assertTrue(connection_postgres("host", "database", "usuario", "senha", 16, 1000, ""))
        self.assertTrue(connection_postgres("host", "database", "usuario", "senha", 16, 10000, ""))

        self.assertTrue(connection_postgres("host", "database", "usuario", "senha", 17, 10, ""))
        self.assertTrue(connection_postgres("host", "database", "usuario", "senha", 17, 100, ""))
        self.assertTrue(connection_postgres("host", "database", "usuario", "senha", 17, 1000, ""))
        self.assertTrue(connection_postgres("host", "database", "usuario", "senha", 17, 10000, ""))

        self.assertTrue(connection_postgres("host", "database", "usuario", "senha", 19, 10, ""))
        self.assertTrue(connection_postgres("host", "database", "usuario", "senha", 19, 100, ""))
        self.assertTrue(connection_postgres("host", "database", "usuario", "senha", 19, 1000, ""))
        self.assertTrue(connection_postgres("host", "database", "usuario", "senha", 19, 10000, ""))

    def testPostgreConectionEight(self):
        try:
            connection_postgres("host", "database", "usuario", "senha", 10, 1000, "AND gdfssg > 1000")
            teste = 1
        except:
            teste = 0
        self.assertFalse(bool(teste), msg="Teste 8 (Postgre) veio true (1), mas esperava falso (0).")

    def testSQLServerConectionOne(self):
        query_sql = "SELECT id FROM Teste2 WHERE machine_id = 10 ORDER BY id DESC OFFSET 0 ROWS FETCH NEXT 1 ROWS ONLY"
        try:
            connection_SQL("", "server", "database", "usuario", "senha", query_sql, True)
            teste = 1
        except:
            teste = 0
        self.assertFalse(bool(teste), msg="Teste 1 (SQL Server) veio true (1), mas esperava falso (0).")

    def testSQLServerConectionTwo(self):
        query_sql = "SELECT id FROM Teste2 WHERE machine_id = 10 ORDER BY id DESC OFFSET 0 ROWS FETCH NEXT 1 ROWS ONLY"
        try:
            connection_SQL("driver", "", "database", "usuario", "senha", query_sql, True)
            teste = 1
        except:
            teste = 0
        self.assertFalse(bool(teste), msg="Teste 2 (SQL Server) veio true (1), mas esperava falso (0).")

    def testSQLServerConectionThree(self):
        query_sql = "SELECT id FROM Teste2 WHERE machine_id = 10 ORDER BY id DESC OFFSET 0 ROWS FETCH NEXT 1 ROWS ONLY"
        try:
            connection_SQL("driver", "server", "", "usuario", "senha", query_sql, True)
        except:
            teste = 0
            self.assertFalse(bool(teste), msg="Teste 3 (SQL Server) veio true (1), mas esperava falso (0).")

    def testSQLServerConectionFour(self):
        query_sql = "SELECT id FROM Teste2 WHERE machine_id = 10 ORDER BY id DESC OFFSET 0 ROWS FETCH NEXT 1 ROWS ONLY"
        try:
            connection_SQL("driver", "server", "database", "", "senha", query_sql, True)
            teste = 1
        except:
            teste = 0
        self.assertFalse(bool(teste), msg="Teste 4 (SQL Server) veio true (1), mas esperava falso (0).")

    def testSQLServerConectionFive(self):
        query_sql = "SELECT id FROM Teste2 WHERE machine_id = 10 ORDER BY id DESC OFFSET 0 ROWS FETCH NEXT 1 ROWS ONLY"
        try:
            connection_SQL("driver", "server", "database", "usuario", "", query_sql, True)
            teste = 1
        except:
            teste = 0
        self.assertFalse(bool(teste), msg="Teste 5 (SQL Server) veio true (1), mas esperava falso (0).")

    def testSQLServerConectionSix(self):
        try:
            connection_SQL("driver", "server", "database", "usuario", "senha", "", True)
            teste = 1
        except:
            teste = 0
        self.assertFalse(bool(teste), msg="Teste 6 (SQL Server) veio true (1), mas esperava falso (0).")

    def testSQLServerConectionSeven(self):
        query_sql = "INSERT INTO Teste2 VALUES ()"
        try:
            connection_SQL("", "server", "database", "usuario", "senha", query_sql, False)
            teste = 1
        except:
            teste = 0
        self.assertFalse(bool(teste), msg="Teste 7 (SQL Server) veio true (1), mas esperava falso (0).")

    def testSQLServerConectionEight(self):
        query_sql = "INSERT INTO Teste2 VALUES ()"
        try:
            connection_SQL("driver", "", "database", "usuario", "senha", query_sql, False)
            teste = 1
        except:
            teste = 0
        self.assertFalse(bool(teste), msg="Teste 7 (SQL Server) veio true (1), mas esperava falso (0).")

    def testSQLServerConectionNine(self):
        query_sql = "INSERT INTO Teste2 VALUES ()"
        try:
            connection_SQL("driver", "server", "", "usuario", "senha", query_sql, False)
            teste = 1
        except:
            teste = 0
        self.assertFalse(bool(teste), msg="Teste 7 (SQL Server) veio true (1), mas esperava falso (0).")

    def testSQLServerConectionTen(self):
        query_sql = "INSERT INTO Teste2 VALUES ()"
        try:
            connection_SQL("driver", "server", "database", "", "senha", query_sql, False)
            teste = 1
        except:
            teste = 0
        self.assertFalse(bool(teste), msg="Teste 7 (SQL Server) veio true (1), mas esperava falso (0).")

    def testSQLServerConectionEleven(self):
        query_sql = "INSERT INTO Teste2 VALUES ()"
        try:
            connection_SQL("driver", "server", "database", "usuario", "", query_sql, False)
            teste = 1
        except ConnectionError:
            teste = 0
        self.assertFalse(bool(teste), msg="Teste 7 (SQL Server) veio true (1), mas esperava falso (0).")


if __name__ == '__main__':
    unittest.main()
