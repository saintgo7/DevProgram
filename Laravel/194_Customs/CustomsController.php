<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class CustomsController extends Controller
{
    public function index()
    {
        return view('customs.index', [
            'title' => 'Customs'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'Customs created']);
    }
}
