<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class VATController extends Controller
{
    public function index()
    {
        return view('vat.index', [
            'title' => 'VAT'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'VAT created']);
    }
}
