<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class MilestoneController extends Controller
{
    public function index()
    {
        return view('milestone.index', [
            'title' => 'Milestone'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'Milestone created']);
    }
}
