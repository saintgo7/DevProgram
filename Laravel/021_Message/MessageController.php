<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class MessageController extends Controller
{
    public function index()
    {
        return view('message.index', [
            'title' => 'Message'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'Message created']);
    }
}
