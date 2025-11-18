<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class TimelineController extends Controller
{
    public function index()
    {
        return view('timeline.index', [
            'title' => 'Timeline'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'Timeline created']);
    }
}
