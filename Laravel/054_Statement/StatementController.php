<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class StatementController extends Controller
{
    public function index()
    {
        return view('statement.index', [
            'title' => 'Statement'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'Statement created']);
    }
}
