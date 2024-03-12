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
        
def insirir(novo_login,novo_senha):
    if Usuario is None:
        return False
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
            insert = 'INSERT INTO tb_usuario (login,senha) VALUES (%s,%s)'
            values = (novo_login ,novo_senha)
            cursor.execute(insert, values)
        conexao.commit()
            #return True if result != None else False #se result for igual a none, devolvo False, senão true
            

def menu():
    texto = '0-sair\n1-Login\n2-Logoff\n3-sign up'
    #usuario ainda não existe
    usuario = None
    op = int(input(texto))
    while op != 0:
        if op == 1:
            login = input("Digite o login ")
            senha = input("Digite a senha 0")
            usuario = Usuario(login,senha)
            #expressão condicional (if/else)
            print("Usuário OK! " if existe (usuario) else "Usuário NOK")
        elif op == 2:
            usuario = None
            print("Logoff realizado com sucesso")
        elif op == 3:
            novo_login = input("Digite o login: ")
            novo_senha = input("Digite a senha: ")
            insirir(novo_login, novo_senha)
        else:
            print("somente valores entre 0,1 e 2,plis")
        op = int(input(texto))



# def teste():
#     print(existe(Usuario('admin', 'admin')))

# teste()
menu()