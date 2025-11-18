<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class SAMLController extends Controller
{
    public function index()
    {
        return view('saml.index', [
            'title' => 'SAML'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'SAML created']);
    }
}
