<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class SchedulerController extends Controller
{
    public function index()
    {
        return view('scheduler.index', [
            'title' => 'Scheduler'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'Scheduler created']);
    }
}
