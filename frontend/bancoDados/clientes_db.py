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
        self.createTableClients()
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

    def allClientsIdName(self):
        sql_command = "SELECT id_clientes, nome_completo FROM clientes;"
        self.cursor.execute(sql_command)
        result = self.cursor.fetchall()
        return result

    def allClientsName(self):
        sql_command = "SELECT nome_completo FROM clientes;"
        self.cursor.execute(sql_command)
        result = self.cursor.fetchall()
        result = [name[0] for name in result]
        return result




    def createTableClients(self):
        sql_command = '''
        CREATE TABLE IF NOT EXISTS project_rt.clientes (
          id_clientes INT NOT NULL AUTO_INCREMENT,
          nome_completo VARCHAR(45) NULL,
          matricula VARCHAR(80) NULL,
          senha VARCHAR(45) NULL,
          permissao INT NULL,
          PRIMARY KEY (id_clientes)
          );
        '''
        self.cursor.execute(sql_command)
        self.inicializarClientes()

    def inicializarClientes(self):
        try:
            print('try')
            sql_command = "SELECT * FROM projeto_rt.clientes;"
            self.cursor.execute(sql_command)
            result = self.cursor.fetchall()
            if (result == []):
                print('vazio')
                sql_command = "INSERT INTO projeto_rt.clientes  VALUES (NULL,%s,%s,%s,%s)"
                val = [("Guilherme Matheus de Aguiar Lima"      , "21950880", "s98", "2"),
                       ("José Marcos Cabrera Neto"              , "21953043", "s23", "1"),
                       ("Luiza Paula Moreira Leão"              , "21950883", "s43", "1"),
                       ("Mattheus Smith Costa Fernandes"        , "21954379", "s87", "1"),
                       ("Thiago Rodrigo Monteiro Salgado"       , "21954456", "s45", "2"),
                       ("Odalisio Leite da Silva Neto"          , "21950520", "s55", "2"),
                       ("Vinícius Patrício Medeiros da Silva"   , "21951799", "s95", "1")]
                for val_aux in val:
                    print('inserindo cada')
                    self.cursor.execute(sql_command, val_aux)
                    self.db.connection.commit()

            return True
        except:
            return False
