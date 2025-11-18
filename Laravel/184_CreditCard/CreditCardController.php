<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class CreditCardController extends Controller
{
    public function index()
    {
        return view('creditcard.index', [
            'title' => 'CreditCard'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'CreditCard created']);
    }
}
