<?php

require 'vendor/autoload.php';

use JsonRpc\Client;

$client = new Client('http://localhost/server.php');

// Exemplo de chamada RPC para listar produtos
$response = $client->call('produto.listar');

// Exemplo de chamada RPC para inserir um produto
$response = $client->call('produto.inserir', ['nome' => 'Produto Teste', 'preco' => 100.00]);

// Exemplo de chamada RPC para excluir um produto
$response = $client->call('produto.excluir', ['id' => 1]);

// Exemplo de chamada RPC para listar movimentações
$response = $client->call('movimentacao.listar');

// Exemplo de chamada RPC para inserir uma movimentação
$response = $client->call('movimentacao.inserir', ['descricao' => 'Movimentação Teste', 'valor' => 50.00]);

// Exemplo de chamada RPC para excluir uma movimentação
$response = $client->call('movimentacao.excluir', ['id' => 1]);
