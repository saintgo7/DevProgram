<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class UserController extends Controller
{
    public function index()
    {
        return view('user.index', [
            'title' => 'User'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'User created']);
    }
}
