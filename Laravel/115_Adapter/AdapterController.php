<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class AdapterController extends Controller
{
    public function index()
    {
        return view('adapter.index', [
            'title' => 'Adapter'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'Adapter created']);
    }
}
