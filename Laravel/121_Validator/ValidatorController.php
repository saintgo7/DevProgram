<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class ValidatorController extends Controller
{
    public function index()
    {
        return view('validator.index', [
            'title' => 'Validator'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'Validator created']);
    }
}
