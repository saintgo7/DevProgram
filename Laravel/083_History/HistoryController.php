<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class HistoryController extends Controller
{
    public function index()
    {
        return view('history.index', [
            'title' => 'History'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'History created']);
    }
}
