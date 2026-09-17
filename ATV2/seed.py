from models import Autor, Livro


def popular_banco(session):
    machado = Autor(nome="Machado de Assis", pais="Brasil")
    clarice = Autor(nome="Clarice Lispector", pais="Brasil")
    tolkien = Autor(nome="J.R.R. Tolkien", pais="Reino Unido")

    livros = [
        Livro(titulo="Dom Casmurro", ano=1899, autor=machado),
        Livro(titulo="Memórias Póstumas de Brás Cubas", ano=1881, autor=machado),
        Livro(titulo="Quincas Borba", ano=1891, autor=machado),
        Livro(titulo="A Hora da Estrela", ano=1977, autor=clarice),
        Livro(titulo="Perto do Coração Selvagem", ano=1943, autor=clarice),
        Livro(titulo="O Hobbit", ano=1937, autor=tolkien),
    ]

    session.add_all([machado, clarice, tolkien])
    session.add_all(livros)
    session.commit()
