<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class ManufacturerController extends Controller
{
    public function index()
    {
        return view('manufacturer.index', [
            'title' => 'Manufacturer'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'Manufacturer created']);
    }
}
