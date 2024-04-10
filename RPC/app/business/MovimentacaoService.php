<?php

namespace App\Business;

use App\Data\ModelMovimentacao;

class MovimentacaoService
{
    private $modelMovimentacao;

    public function __construct()
    {
        $this->modelMovimentacao = new ModelMovimentacao();
    }

    public function listar()
    {
        return $this->modelMovimentacao->getAll();
    }

    public function inserir($movimentacao)
    {
        $this->modelMovimentacao->insertMovimentacao($movimentacao);
    }

    public function excluir($id)
    {
        $this->modelMovimentacao->deleteMovimentacao($id);
    }
}
