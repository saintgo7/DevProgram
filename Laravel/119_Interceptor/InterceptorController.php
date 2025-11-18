<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class InterceptorController extends Controller
{
    public function index()
    {
        return view('interceptor.index', [
            'title' => 'Interceptor'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'Interceptor created']);
    }
}
