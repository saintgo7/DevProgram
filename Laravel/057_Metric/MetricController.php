<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class MetricController extends Controller
{
    public function index()
    {
        return view('metric.index', [
            'title' => 'Metric'
        ]);
    }

    public function store(Request $request)
    {
        // Store logic
        return response()->json(['message' => 'Metric created']);
    }
}
