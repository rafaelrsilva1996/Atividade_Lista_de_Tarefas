from psycopg2 import connect


class Banco:
    def __init__(self):
        self.conn = connect(
            dbname = "postgres",
            user = "postgres",
            host = "localhost",
            password = "5432"
        )

    def fechar_conexao(self):
        return self.conn.close()
    
    def executar_query(self, query):
        cursor = self.conn.cursor()
        cursor.execute(query)
        return cursor

    def inserir(self, tabela, campos, objeto):
        cursor = self.conn.cursor()
        sql = f"INSERT INTO {tabela} {campos} VALUES {tuple(objeto)} RETURNING id"
        cursor.execute(sql, objeto)
        self.conn.commit()
        id = cursor.fetchone()[0]
        return id
    
    def atualizar(self, tabela, campos, valores, object_id):
        if isinstance(campos, str):
            values_sql = [f"{campos} = '{valores}'"]
        elif len(campos)>1:
            values_sql = []
            for i, item in enumerate(campos):
                values_sql.append( f"{campos[i]} = '{valores[i]}'")

        if len(values_sql)> 1:
            values_sql = ', '.join(values_sql)
        else:
            values_sql = values_sql[0]

        cursor = self.conn.cursor()
        sql = f"UPDATE {tabela} SET {values_sql} WHERE id = {object_id};"
        cursor.execute(sql)
        updated_rows = cursor.rowcount
        self.conn.commit()
        return updated_rows

    def deletar(self, tabela, object_id):
        cursor = self.conn.cursor()
        sql = f"DELETE FROM {tabela} WHERE id = {object_id}"
        cursor.execute(sql)
        self.conn.commit()

    def listar(self, tabela):
        sql = f"SELECT * FROM {tabela} ORDER BY id DESC;"
        result = self.executar_query(sql)
        lst = []

        for i, record in enumerate(result):
            lst.append(record)

        return lst   

if __name__ == '__main__':
    banco = Banco()
    banco.fechar_conexao()
