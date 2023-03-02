'''
CREATE TABLE `project_rt`.`registros` (
  `id_registro` INT NOT NULL AUTO_INCREMENT,
  `id_cliente` INT NULL,
  `data` DATETIME NULL,
  `tipo_registro` VARCHAR(15) NULL,
  PRIMARY KEY (`id_registro`));
'''

class Registro_DB:
    def __init__(self, db):
        self.db = db
        self.cursor = db.connection.cursor()

    def insertRegister(self, registro):
        sql_command = "INSERT INTO registros VALUES (NULL, %s,%s,%s)"
        val = (registro.id_client, registro.data, registro.tipo_registro)
        self.cursor.execute(sql_command, val)
        self.db.connection.commit()
    def lastRegister(self, id_cliente):
        sql_command = "SELECT  tipo_registro FROM registros WHERE id_cliente = '{name}' ORDER BY id_registro DESC;".format(name=id_cliente)
        self.cursor.execute(sql_command)
        result = self.cursor.fetchall()
        return result[0][0]

    def dateClient(self, data1, data2, id_client):
        sql_command = "SELECT  *FROM registros WHERE id_cliente = '{name}' AND data>='{data1}' AND data<='{data2}';".format(name=id_client, data1=data1, data2 = data2)
        self.cursor.execute(sql_command)
        result = self.cursor.fetchall()
        return result