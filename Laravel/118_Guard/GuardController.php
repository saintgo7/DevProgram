<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class GuardController extends Controller
{
    public function index()
    {
        return view('guard.index', [
            'title' => 'Guard'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'Guard created']);
    }
}
