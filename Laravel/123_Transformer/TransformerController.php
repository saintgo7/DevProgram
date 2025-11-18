<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class TransformerController extends Controller
{
    public function index()
    {
        return view('transformer.index', [
            'title' => 'Transformer'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'Transformer created']);
    }
}
