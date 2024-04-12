# Classe client.py

import json
import httpx
import asyncio

# Função para cadastrar um produto
async def post_produto(nome):
    url = "http://localhost:8000/postProduto/"
    data = {"nome": nome}
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=data)
        print(response.json())
        return response.json()

# Função para cadastrar uma categoria
async def post_categoria(nome):
    url = "http://localhost:8000/postCategoria/"
    data = {"nome": nome}
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=data)
        print(response.json())
        return response.json()

# Função para cadastrar um fabricante
async def post_fabricante(nome):
    url = "http://localhost:8000/postFabricante/"
    data = {"nome": nome}
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=data)
        print(response.json())
        return response.json()

# Exemplo de uso
async def cadastrar_produtos():
    produto = await post_produto("Produto A")
    categoria = await post_categoria("Categoria X")
    fabricante = await post_fabricante("Fabricante 1")

asyncio.run(cadastrar_produtos())
