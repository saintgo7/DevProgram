<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class DutyController extends Controller
{
    public function index()
    {
        return view('duty.index', [
            'title' => 'Duty'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'Duty created']);
    }
}
