<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class PaginationController extends Controller
{
    public function index()
    {
        return view('pagination.index', [
            'title' => 'Pagination'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'Pagination created']);
    }
}
