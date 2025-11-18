<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class PaymentMethodController extends Controller
{
    public function index()
    {
        return view('paymentmethod.index', [
            'title' => 'PaymentMethod'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'PaymentMethod created']);
    }
}
