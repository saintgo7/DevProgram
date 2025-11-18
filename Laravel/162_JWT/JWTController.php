<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class JWTController extends Controller
{
    public function index()
    {
        return view('jwt.index', [
            'title' => 'JWT'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'JWT created']);
    }
}
