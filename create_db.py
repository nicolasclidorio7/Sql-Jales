from sqlalchemy import create_engine
from models import Base  # Importamos nossa Base do arquivo models.py

# Criamos o engine para o banco de dados
engine = create_engine("sqlite:///escola.db", echo=True)

# O SQLAlchemy irá conectar, verificar quais tabelas não existem e criá-las
print("Gerando o schema do banco de dados...")
Base.metadata.create_all(engine)
print("Schema gerado com sucesso!")
