<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class SortController extends Controller
{
    public function index()
    {
        return view('sort.index', [
            'title' => 'Sort'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'Sort created']);
    }
}
