# main.py
from sqlalchemy import create_engine, text
engine = create_engine("sqlite:///nome_do_arquivo.db", echo=True)
# O bloco "with" garante que a conexão será fechada ao final
with engine.connect() as connection:
    # `text()` informa ao SQLAlchemy que isso é uma instrução SQL
    result = connection.execute(text("SELECT 'Olá, mundo!'"))
    # .scalar() pega o primeiro valor da primeira linha do resultado
    print(result.scalar())
