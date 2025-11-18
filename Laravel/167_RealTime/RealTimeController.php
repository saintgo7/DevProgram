<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class RealTimeController extends Controller
{
    public function index()
    {
        return view('realtime.index', [
            'title' => 'RealTime'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'RealTime created']);
    }
}
