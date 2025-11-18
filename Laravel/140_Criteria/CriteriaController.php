<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class CriteriaController extends Controller
{
    public function index()
    {
        return view('criteria.index', [
            'title' => 'Criteria'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'Criteria created']);
    }
}
