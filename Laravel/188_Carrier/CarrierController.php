<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class CarrierController extends Controller
{
    public function index()
    {
        return view('carrier.index', [
            'title' => 'Carrier'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'Carrier created']);
    }
}
