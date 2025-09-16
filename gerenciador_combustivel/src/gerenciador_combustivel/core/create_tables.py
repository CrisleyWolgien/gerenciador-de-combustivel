# src/create_tables.py

from sqlmodel import SQLModel
from gerenciador_combustivel.core.db import engine

# Importa todos os modelos para que o SQLModel conheça as tabelas
from gerenciador_combustivel.models.user import Users
from gerenciador_combustivel.models.supply import Supply
from gerenciador_combustivel.models.vehicle import Vehicle

def create_db_and_tables():
    print("Iniciando a criação das tabelas no banco de dados...")

    # Cria todas as tabelas conhecidas pela metadata
    SQLModel.metadata.create_all(engine)

    print("Tabelas criadas com sucesso!")

if __name__ == "__main__":
    create_db_and_tables()
