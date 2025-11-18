<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class SMSController extends Controller
{
    public function index()
    {
        return view('sms.index', [
            'title' => 'SMS'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'SMS created']);
    }
}
