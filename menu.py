import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

#Criando banco de dados
MEU_BANCO = create_engine("sqlite:///meubanco.db")

#Criando conexão com banco de dados
Session = sessionmaker(bind=MEU_BANCO)
session = Session()


#criando tabela

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"

    #Definindo campos da tabela
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)

    #Definindo atributos da classe
    def __init__(self, nome: str, email: str, senha: str):
        self.nome = nome
        self.email = email
        self.senha = senha

#craindo tabela no banco de dados
Base.metadata.create_all(bind=MEU_BANCO)

#Salvar no banco de0 dados.
os.system("cls || clear")

print("Solicitando dados para o usuario")
usuario = Usuario("Marta", "marta@gmail.com", "123")
session.add(usuario)
session.commit()

usuario = Usuario(nome="Maria", email="maria@gmail.com", senha="456")
session.add(usuario)
session.commit()

# Listando todos os ususario do banco de dados.
print("\nExibindo todos os usuarios do bando de dados.")
lista_usuario = session.query(Usuario).all()

for usuario in lista_usuario:
    print(f"{usuario.id} - {usuario.nome} - {usuario.senha}")

# Fechando conexão
session.close()