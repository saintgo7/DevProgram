<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class CouponController extends Controller
{
    public function index()
    {
        return view('coupon.index', [
            'title' => 'Coupon'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'Coupon created']);
    }
}
