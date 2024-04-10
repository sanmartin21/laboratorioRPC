<?php

namespace App\Client;

class ViewPage
{
    public function render($content)
    {
        return '<html><body>' . $content . '</body></html>';
    }
}
