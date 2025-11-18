<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class PayPalController extends Controller
{
    public function index()
    {
        return view('paypal.index', [
            'title' => 'PayPal'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'PayPal created']);
    }
}
