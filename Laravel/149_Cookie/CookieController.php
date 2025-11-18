<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class CookieController extends Controller
{
    public function index()
    {
        return view('cookie.index', [
            'title' => 'Cookie'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'Cookie created']);
    }
}
