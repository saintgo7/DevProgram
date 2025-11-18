<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class ZoneController extends Controller
{
    public function index()
    {
        return view('zone.index', [
            'title' => 'Zone'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'Zone created']);
    }
}
