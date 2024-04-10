<?php

namespace App\Data;

class ModelProduto
{
    private $filePath = 'data/arquivo.json';

    public function getAll()
    {
        $data = file_get_contents($this->filePath);
        return json_decode($data, true);
    }

    public function insertProduto($produto)
    {
        $data = $this->getAll();
        $data[] = $produto;
        file_put_contents($this->filePath, json_encode($data));
    }

    public function deleteProduto($id)
    {
        $data = $this->getAll();
        $data = array_filter($data, function ($item) use ($id) {
            return $item['id'] !== $id;
        });
        file_put_contents($this->filePath, json_encode($data));
    }
}
