'''
CREATE TABLE project_rt.clientes (
  id_clientes INT NOT NULL AUTO_INCREMENT,
  nome_completo VARCHAR(45) NULL,
  matricula VARCHAR(80) NULL,
  senha VARCHAR(45) NULL,
  permissao INT NULL,
  PRIMARY KEY (id_clientes));
'''
class Clientes_DB:

    def __init__(self, db):
        self.db = db
        self.cursor = db.connection.cursor()
    def insertClient(self, cliente):
        sql_command = "INSERT INTO clientes VALUES (NULL, %s,%s,%s,%s)"
        val = (cliente.nome_completo, cliente.matricula, cliente.senha, cliente.permissao)
        self.cursor.execute(sql_command, val)
        self.db.connection.commit()
    def getID_nameCLient(self, name_client):
        sql_command = "SELECT *FROM clientes WHERE nome_completo = '{name}'".format(name=name_client)
        self.cursor.execute(sql_command)
        result = self.cursor.fetchall()
        return result[0][0]
    def getPermission_nameClient(self, name_client):
        sql_command = "SELECT *FROM clientes WHERE nome_completo = '{name}'".format(name=name_client)
        self.cursor.execute(sql_command)
        result = self.cursor.fetchall()
        return result[0][4]
