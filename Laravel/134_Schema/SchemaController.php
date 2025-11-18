<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class SchemaController extends Controller
{
    public function index()
    {
        return view('schema.index', [
            'title' => 'Schema'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'Schema created']);
    }
}
