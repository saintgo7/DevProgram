<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class MapperController extends Controller
{
    public function index()
    {
        return view('mapper.index', [
            'title' => 'Mapper'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'Mapper created']);
    }
}
