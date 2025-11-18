<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class OAuthController extends Controller
{
    public function index()
    {
        return view('oauth.index', [
            'title' => 'OAuth'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'OAuth created']);
    }
}
