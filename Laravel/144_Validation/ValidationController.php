<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class ValidationController extends Controller
{
    public function index()
    {
        return view('validation.index', [
            'title' => 'Validation'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'Validation created']);
    }
}
