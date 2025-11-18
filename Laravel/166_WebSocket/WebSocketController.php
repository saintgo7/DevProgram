<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class WebSocketController extends Controller
{
    public function index()
    {
        return view('websocket.index', [
            'title' => 'WebSocket'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'WebSocket created']);
    }
}
