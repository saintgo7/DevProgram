<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class CacheController extends Controller
{
    public function index()
    {
        return view('cache.index', [
            'title' => 'Cache'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'Cache created']);
    }
}
