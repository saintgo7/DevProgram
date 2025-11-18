<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class SeederController extends Controller
{
    public function index()
    {
        return view('seeder.index', [
            'title' => 'Seeder'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'Seeder created']);
    }
}
