<?php

require 'vendor/autoload.php';

use JsonRpc\Server;

$server = new Server;

// Registre suas classes de negócios aqui
$server->register('App\Business\ProdutoService', 'produto');
$server->register('App\Business\MovimentacaoService', 'movimentacao');

// Execute o servidor
$server->handle();
