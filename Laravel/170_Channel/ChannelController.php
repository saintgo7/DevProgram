<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class ChannelController extends Controller
{
    public function index()
    {
        return view('channel.index', [
            'title' => 'Channel'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'Channel created']);
    }
}
