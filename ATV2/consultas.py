from sqlalchemy import func, select
from models import Autor, Livro

def listar_livros(session):
    stmt = select(Livro).join(Livro.autor)
    livros = session.scalars(stmt).all()
    for livro in livros:
        print(f"- {livro.titulo} ({livro.ano}) - {livro.autor.nome}")

def livros_por_autor(session, nome_autor):
    stmt = select(Livro).join(Livro.autor).where(Autor.nome == nome_autor)
    livros = session.scalars(stmt).all()
    if not livros:
        print(f"Nenhum livro encontrado para o autor '{nome_autor}'.")
        return
    for livro in livros:
        print(f"- {livro.titulo} ({livro.ano})")

def buscar_livros(session, trecho):
    stmt = select(Livro).where(Livro.titulo.ilike(f"%{trecho}%"))
    livros = session.scalars(stmt).all()
    if not livros:
        print(f"Nenhum livro encontrado contendo '{trecho}'.")
        return
    for livro in livros:
        print(f"- {livro.titulo} ({livro.ano}) - {livro.autor.nome}")

def listar_autores_com_quantidade(session):
    stmt = (
        select(Autor.nome, func.count(Livro.id))
        .join(Livro, Livro.autor_id == Autor.id)
        .group_by(Autor.id)
    )
    resultados = session.execute(stmt).all()
    for nome, quantidade in resultados:
        print(f"- {nome}: {quantidade} livro(s)")

def detalhes_livro(session, titulo):
    stmt = select(Livro).where(Livro.titulo == titulo)
    livro = session.scalars(stmt).first()
    if not livro:
        print(f"Livro '{titulo}' não encontrado.")
        return
    print(f"Título: {livro.titulo}")
    print(f"Ano: {livro.ano}")
    print(f"Autor: {livro.autor.nome}")
    print(f"País do autor: {livro.autor.pais}")
