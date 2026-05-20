from sqlalchemy import create_engine, Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils.types import ChoiceType

# Cria a conexão (engine) do database SQLite
db = create_engine("sqlite:///database/granforno.db")
# Cria a base do database
Base = declarative_base()

# Usuário
class Usuario(Base):
    __tablename__ = 'usuarios' # Nome da tabela no database

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String, nullable=False)
    email = Column("email", String, unique=True, nullable=False)
    senha = Column("senha", String, nullable=False)
    ativo = Column("ativo", Boolean, default=True)
    admin = Column("admin", Boolean, default=False)

    # id = Column("[nome da coluna]", [tipo de dado da coluna], [chave primária], [autoincremento])
    # nome = Column("[nome da coluna]", [tipo de dado da coluna], [não nulo])
    # email = Column("[nome da coluna]", [tipo de dado da coluna], [único], [não nulo])
    # senha = Column("[nome da coluna]", [tipo de dado da coluna], [não nulo])
    # ativo = Column("[nome da coluna]", [tipo de dado da coluna], [valor padrão])
    # admin = Column("[nome da coluna]", [tipo de dado da coluna], [valor padrão])

    def __init__(self, nome, email, senha, ativo=True, admin=False): # Função que define os parâmetros de criação de um usuário
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin

# Sabores
class Sabores(Base):
    __table_name__ = 'sabores'

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome_sabor = Column("nome_sabor", String, nullable=False)
    descricao_sabor = Column("descricao_sabor", String)
    alerta_alergenicos = Column("alerta_alergenicos", String, default="SEM ALERGÊNCOS")

    def __init__(self, nome_sabor, descricao_sabor, alerta_alergenicos="SEM ALERGÊNICOS"):
        self.nome_sabor = nome_sabor
        self.descricao_sabor = descricao_sabor
        self.alerta_alergenicos = alerta_alergenicos

# ItensPedido
class ItensPedido(Base):
    __table_name__ = 'itenspedido'

    TAMANHO_ITENS = (
        ("INDIVIDUAL", "INDIVIDUAL"),
        ("PEQUENO", "PEQUENO"),
        ("MÉDIO", "MÉDIO"),
        ("GRANDE", "GRANDE"),
        ("ANORMAL", "ANORMAL")
    )

    BORDA_ITENS = (
        ("VAZIO", "VAZIO")
        ("CATUPIRY", "CATUPIRY"),
        ("CHEDDAR", "CHEDDAR"),
        ("CHOCOLATE", "CHOCOLATE"),
        ("CREME DE NINHO", "CREME DE NINHO")
    )

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    quantidade = Column("quantidade", Integer, nullable=False, default=0)
    sabor = Column("sabor", ForeignKey("sabores.id"), nullable=False)
    tamanho = Column("tamanho", ChoiceType(choices=TAMANHO_ITENS), nullable=False)
    tipo_borda = Column("tipo_borda", ChoiceType(choices=BORDA_ITENS), default="VAZIO")
    preco_unitario = Column("preco_unitario", Float, nullable=False)
    id_pedido = Column("id_pedido", ForeignKey("pedidos.id"), nullable=False)

    def __init__(self, quantidade, sabor, tamanho, preco_unitario, id_pedido, tipo_borda="VAZIO"):
        self.quantidade = quantidade
        self.sabor = sabor
        self.tamanho = tamanho
        self.preco_unitario = preco_unitario
        self.id_pedido = id_pedido
        self.tipo_borda = tipo_borda

# Pedido
class Pedido(Base):
    __table_name__ = 'pedidos'

    # Escolha de somente três informações para o campo "status"
    STATUS_PEDIDOS = (
        ("PENDENTE", "PENDENTE"),
        ("FINALIZADO", "FINALIZADO"),
        ("CANCELADO", "CANCELADO")
    )

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    status = Column("status", ChoiceType(choices=STATUS_PEDIDOS), nullable=False, default="PENDENTE")
    id_usuario = Column("id_usuario", ForeignKey("usuarios.id"), nullable=False)
    preco = Column("preco", Float, nullable=False)
    itens = Column("itens", ForeignKey("itenspedido.id"))

    def __init__(self, usuario, status="PENDENTE", preco=0):
        self.usuario = usuario
        self.status = status
        self.preco = preco

# TODO: Criar metadados do database (criar efetivamente o database)

# TODO: Atualizar documentação interna sobre toda a criação do database (SQLAlchemy, criação de modelo, criação de metadados, migrations, etc)