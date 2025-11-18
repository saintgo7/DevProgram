<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class StyleController extends Controller
{
    public function index()
    {
        return view('style.index', [
            'title' => 'Style'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'Style created']);
    }
}
