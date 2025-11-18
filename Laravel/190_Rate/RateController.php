<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class RateController extends Controller
{
    public function index()
    {
        return view('rate.index', [
            'title' => 'Rate'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'Rate created']);
    }
}
