<?php

namespace App\Client;

class ViewListaDeCompras
{
    public function render($produtos)
    {
        $html = '<h1>Lista de Compras</h1>';
        $html .= '<ul>';
        foreach ($produtos as $produto) {
            $html .= '<li>' . $produto['nome'] . ' - ' . $produto['preco'] . '</li>';
        }
        $html .= '</ul>';
        return $html;
    }
}
