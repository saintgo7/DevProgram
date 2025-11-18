<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BroadcastController extends Controller
{
    public function index()
    {
        return view('broadcast.index', [
            'title' => 'Broadcast'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'Broadcast created']);
    }
}
