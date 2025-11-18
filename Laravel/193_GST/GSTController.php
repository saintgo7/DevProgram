<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class GSTController extends Controller
{
    public function index()
    {
        return view('gst.index', [
            'title' => 'GST'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'GST created']);
    }
}
