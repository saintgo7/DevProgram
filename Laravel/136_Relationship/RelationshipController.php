<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class RelationshipController extends Controller
{
    public function index()
    {
        return view('relationship.index', [
            'title' => 'Relationship'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'Relationship created']);
    }
}
