import mysql.connector

# conexão com o banco de dados
conexao = mysql.connector.connect(
    host =  "localhost",
    user = "root",
    password = "puc1234",
    database = "projeto_integrador"
)

cursor = conexao.cursor()

# inserção de dados - MESARIOS
def inserir_mesarios(cpf, nome, senha):
    sql = "INSERT INTO mesarios (cpf, nome_completo, login, senha) VALUES (%s, %s, %s, %s)"
    valores = (cpf, nome, nome+cpf, senha)
    cursor.execute(sql, valores)
    conexao.commit()
    print("Mesário cadastrado com ID: ", cursor.lastrowid)


# inserção de dados - USUARIOS 
def inserir_mesarios(cpf, nome, senha, numero_voto, ja_votou):
    sql = "INSERT INTO usuarios (cpf, nome_completo, login, senha, numero_voto, ja_votou) VALUES (%s, %s, %s, %s, %s, %s)"
    valores = (cpf, nome, nome+cpf, senha, numero_voto, ja_votou) #confirmar como salvar a senha com hash
    cursor.execute(sql, valores)
    conexao.commit()
    print("Usuario cadastrado com ID: ", cursor.lastrowid)
    
# inserção de dados - CANDIDATOS
def inserir_candidato(numero, nome, partido):
    sql = "INSERT INTO candidatos (numero, nome_completo, partido) VALUES (%s, %s, %s)"
    valores = (numero, nome, partido)
    cursor.execute(sql, valores)
    conexao.commit()
    print("Candidato cadastrado com ID: ", cursor.lastrowid)
    