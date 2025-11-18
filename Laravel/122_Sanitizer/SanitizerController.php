<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class SanitizerController extends Controller
{
    public function index()
    {
        return view('sanitizer.index', [
            'title' => 'Sanitizer'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'Sanitizer created']);
    }
}
