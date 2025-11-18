<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class DecoratorController extends Controller
{
    public function index()
    {
        return view('decorator.index', [
            'title' => 'Decorator'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'Decorator created']);
    }
}
