<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class FileController extends Controller
{
    public function index()
    {
        return view('file.index', [
            'title' => 'File'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'File created']);
    }
}
