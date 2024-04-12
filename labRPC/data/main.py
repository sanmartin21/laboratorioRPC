from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uuid
import os
import json
from typing import List

app = FastAPI()

# Define a classe ProdutoInput para entrada de dados ao adicionar um produto
class ProdutoInput(BaseModel):
    nome: str
    descricao: str
    preco: float
    quantidade: int
    fabricante_id: uuid.UUID
    categoria_id: uuid.UUID

# Define a classe Produto para representar um produto
class Produto(BaseModel):
    id: uuid.UUID
    nome: str
    descricao: str
    preco: float
    quantidade: int
    fabricante_id: uuid.UUID
    categoria_id: uuid.UUID

# Gera IDs únicos para fabricante_id e categoria_id
fabricante_id = str(uuid.uuid4())
categoria_id = str(uuid.uuid4())

# Função para salvar um produto em um arquivo JSON
def salvar_produto_json(produto: Produto):
    file_path = 'produtos.json'
    new_data = produto.dict()
    new_data['id'] = str(new_data['id'])
    new_data['fabricante_id'] = str(new_data['fabricante_id'])
    new_data['categoria_id'] = str(new_data['categoria_id'])
    new_data['quantidade'] = produto.quantidade  # Incluir a quantidade
    if not os.path.exists('data'):
        os.makedirs('data')
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
        data.append(new_data)
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    else:
        with open(file_path, 'w') as file:
            json.dump([new_data], file, indent=4)

# Endpoint para adicionar um produto
@app.post("/produtos/", response_model=Produto)
def add_produto(produto: ProdutoInput):
    try:
        new_produto = Produto(
            id=uuid.uuid4(),
            nome=produto.nome,
            descricao=produto.descricao,
            preco=produto.preco,
            quantidade=produto.quantidade,  # A quantidade é inicializada como 0
            fabricante_id=fabricante_id,
            categoria_id=categoria_id
        )
        salvar_produto_json(new_produto)
        return new_produto
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao adicionar produto: {str(e)}")

# Endpoint para listar todos os produtos
@app.get("/produtos/", response_model=List[Produto])
def list_produtos():
    file_path = 'data/produtos.json'
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    else:
        return []

# Nova rota para calcular os somatórios
@app.get("/calcular_somatorios/")
def calcular_somatorios():
    file_path = 'data/produtos.json'
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
        total_valor_produto = sum(p['preco'] * p['quantidade'] for p in data)
        total_quantidade_produto = sum(p['quantidade'] for p in data)
        return {"total_valor_produto": total_valor_produto, "total_quantidade_produto": total_quantidade_produto}
    else:
        return {"total_valor_produto": 0, "total_quantidade_produto": 0}
