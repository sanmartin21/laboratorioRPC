from typing import List
from pydantic import BaseModel
import uuid

class ProdutoInput(BaseModel):
    nome: str
    descricao: str
    preco: float
    quantidade: int
    fabricante_id: uuid.UUID
    categoria_id: uuid.UUID

class CategoriaInput(BaseModel):
    nome: str

class FabricanteInput(BaseModel):
    nome: str

class Produto(BaseModel):
    id: uuid.UUID
    nome: str
    descricao: str
    preco: float
    quantidade: int
    fabricante_id: uuid.UUID
    categoria_id: uuid.UUID

class Categoria(BaseModel):
    id: uuid.UUID
    nome: str

class Fabricante(BaseModel):
    id: uuid.UUID
    nome: str
