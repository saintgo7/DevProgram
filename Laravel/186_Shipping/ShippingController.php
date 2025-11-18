<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class ShippingController extends Controller
{
    public function index()
    {
        return view('shipping.index', [
            'title' => 'Shipping'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'Shipping created']);
    }
}
