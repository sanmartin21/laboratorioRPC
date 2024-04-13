import uuid

class Produto:
    def __init__(self, id=None, nome=None, descricao=None, preco=None, quantidade=None, fabricante_id=None, categoria_id=None):
        self.id = id if id else uuid.uuid4()
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.quantidade = quantidade
        self.fabricante_id = fabricante_id
        self.categoria_id = categoria_id

class Categoria:
    def __init__(self, id=None, nome=None):
        self.id = id if id else uuid.uuid4()
        self.nome = nome

class Fabricante:
    def __init__(self, id=None, nome=None):
        self.id = id if id else uuid.uuid4()
        self.nome = nome
