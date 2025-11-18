<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class FieldController extends Controller
{
    public function index()
    {
        return view('field.index', [
            'title' => 'Field'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'Field created']);
    }
}
