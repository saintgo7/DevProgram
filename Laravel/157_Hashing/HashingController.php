<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class HashingController extends Controller
{
    public function index()
    {
        return view('hashing.index', [
            'title' => 'Hashing'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'Hashing created']);
    }
}
