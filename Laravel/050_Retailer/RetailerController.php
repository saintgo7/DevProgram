<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class RetailerController extends Controller
{
    public function index()
    {
        return view('retailer.index', [
            'title' => 'Retailer'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'Retailer created']);
    }
}
