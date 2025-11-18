<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class ExtensionController extends Controller
{
    public function index()
    {
        return view('extension.index', [
            'title' => 'Extension'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'Extension created']);
    }
}
