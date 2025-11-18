<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class ControllerController extends Controller
{
    public function index()
    {
        return view('controller.index', [
            'title' => 'Controller'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'Controller created']);
    }
}
