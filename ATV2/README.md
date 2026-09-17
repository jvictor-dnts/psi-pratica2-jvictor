## 1. onde ficam os modelos orm?
estão no arquivo models.py, nas classes autor e livro. ambas herdam de base (definida em database.py), o que avisa o sqlalchemy para mapear essas classes para as tabelas autores e livros.

## 2. quem é o lado "um" e quem é o lado "muitos"?
autor é o lado "um" e livro é o "muitos" — um autor escreve vários livros, mas um livro pertence a apenas um autor. no código, dá para ver isso fácil: autor.livros entrega uma lista, enquanto livro.autor traz um único objeto.

## 3. pra que serve o foreignkey em autor_id?
ele garante a integridade no banco, impede que exista um livro apontando para um autor inexistente. além disso, é essa chave estrangeira que permite ao sqlalchemy criar a "ponte" entre os modelos, deixando você navegar direto com livro.autor ou autor.livros.

## 4. o que acontece se esquecer o session.commit()?
os dados não são salvos no disco,tudo  que você adicionou fica apenas em um "rascunho" na memória. se o programa fechar sem o commit(), as alterações se perdem e o banco volta ao estado anterior.