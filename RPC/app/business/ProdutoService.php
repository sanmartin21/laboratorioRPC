<?php

namespace App\Business;

use App\Data\ModelProduto;

class ProdutoService
{
    private $modelProduto;

    public function __construct()
    {
        $this->modelProduto = new ModelProduto();
    }

    public function listar()
    {
        return $this->modelProduto->getAll();
    }

    public function inserir($produto)
    {
        $this->modelProduto->insertProduto($produto);
    }

    public function excluir($id)
    {
        $this->modelProduto->deleteProduto($id);
    }
}
