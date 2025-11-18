<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class LDAPController extends Controller
{
    public function index()
    {
        return view('ldap.index', [
            'title' => 'LDAP'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'LDAP created']);
    }
}
