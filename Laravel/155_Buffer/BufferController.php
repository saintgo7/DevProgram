<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BufferController extends Controller
{
    public function index()
    {
        return view('buffer.index', [
            'title' => 'Buffer'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'Buffer created']);
    }
}
