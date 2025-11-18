<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class GeographyController extends Controller
{
    public function index()
    {
        return view('geography.index', [
            'title' => 'Geography'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'Geography created']);
    }
}
