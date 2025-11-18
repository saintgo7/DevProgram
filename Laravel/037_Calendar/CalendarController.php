<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class CalendarController extends Controller
{
    public function index()
    {
        return view('calendar.index', [
            'title' => 'Calendar'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'Calendar created']);
    }
}
