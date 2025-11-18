<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class APIController extends Controller
{
    public function index()
    {
        return view('api.index', [
            'title' => 'API'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'API created']);
    }
}
