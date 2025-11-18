<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BookmarkController extends Controller
{
    public function index()
    {
        return view('bookmark.index', [
            'title' => 'Bookmark'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'Bookmark created']);
    }
}
