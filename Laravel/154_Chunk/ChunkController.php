<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class ChunkController extends Controller
{
    public function index()
    {
        return view('chunk.index', [
            'title' => 'Chunk'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'Chunk created']);
    }
}
