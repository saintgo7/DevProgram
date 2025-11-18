<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BuilderController extends Controller
{
    public function index()
    {
        return view('builder.index', [
            'title' => 'Builder'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'Builder created']);
    }
}
