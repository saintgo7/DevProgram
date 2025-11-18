<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class AssociationController extends Controller
{
    public function index()
    {
        return view('association.index', [
            'title' => 'Association'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'Association created']);
    }
}
