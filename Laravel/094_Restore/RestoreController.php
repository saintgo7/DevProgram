<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class RestoreController extends Controller
{
    public function index()
    {
        return view('restore.index', [
            'title' => 'Restore'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'Restore created']);
    }
}
