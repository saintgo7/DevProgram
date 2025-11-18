<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class SprintController extends Controller
{
    public function index()
    {
        return view('sprint.index', [
            'title' => 'Sprint'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'Sprint created']);
    }
}
