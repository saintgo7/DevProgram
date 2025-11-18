<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class FactoryController extends Controller
{
    public function index()
    {
        return view('factory.index', [
            'title' => 'Factory'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'Factory created']);
    }
}
