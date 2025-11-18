<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class FollowController extends Controller
{
    public function index()
    {
        return view('follow.index', [
            'title' => 'Follow'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'Follow created']);
    }
}
