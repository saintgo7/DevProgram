<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class QueueController extends Controller
{
    public function index()
    {
        return view('queue.index', [
            'title' => 'Queue'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'Queue created']);
    }
}
