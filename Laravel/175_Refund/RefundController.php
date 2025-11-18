<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class RefundController extends Controller
{
    public function index()
    {
        return view('refund.index', [
            'title' => 'Refund'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'Refund created']);
    }
}
