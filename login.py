import psycopg
print(psycopg)
class Usuario:
    def __init__ (self, login, senha):
        self.login = login
        self.senha = senha

#verifica  se o usuario recebido existe na basse
def existe(usuario):
    #abrir conexao com o postgreeSQL
    #obter uma abstração do tipo "cursor"
    #executar um comando sql
    #verificar resultado
    #devolver true ou false
    with psycopg.connect(
        host="localhost",
        port=5432,
        dbname="20241_fatec_ipi_pbdi_login_python",
        user="postgres",
        password="123456"        
    ) as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(
                'SELECT * FROM tb_usuario WHERE login=%s AND senha=%s',
                (usuario.login, usuario.senha)
            )
            result = cursor.fetchone()
            #return True if result != None else False #se result for igual a none, devolvo False, senão true
            return result != None

def teste():
    print(existe(Usuario('admin', 'admin')))

teste()