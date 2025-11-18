<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class PluginController extends Controller
{
    public function index()
    {
        return view('plugin.index', [
            'title' => 'Plugin'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'Plugin created']);
    }
}
