<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class SigningController extends Controller
{
    public function index()
    {
        return view('signing.index', [
            'title' => 'Signing'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'Signing created']);
    }
}
