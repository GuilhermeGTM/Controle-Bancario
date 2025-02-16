from datetime import date
from sqlmodel import Field, Relationship, SQLModel, create_engine
from enum import Enum


class Bancos(Enum):
    NUBANK = 'Nubank'
    SANTANDER = 'Santander'
    SICREDI = 'Sicredi'
    BRADESCO = 'Bradesco'
    BANRISUL = 'Banrisul'


class Status(Enum):
    ATIVO = 'Ativo'
    INATIVO = 'Inativo'


class Tipos(Enum):
    ENTRADA = 'Entrada'
    SAIDA = 'Saida'


class Conta(SQLModel, table=True):
    id: int = Field(primary_key=True)
    banco: Bancos = Field(default=Bancos.NUBANK)
    status: Status = Field(default=Status.ATIVO)
    valor: float


class Historico(SQLModel, table=True):
    id: int = Field(primary_key=True)
    conta_id: int = Field(foreign_key="conta.id")
    conta: Conta = Relationship()
    tipo: Tipos = Field(default=Tipos.ENTRADA)
    valor: float
    data: date


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=False)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    create_db_and_tables()
