<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class EndpointController extends Controller
{
    public function index()
    {
        return view('endpoint.index', [
            'title' => 'Endpoint'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'Endpoint created']);
    }
}
