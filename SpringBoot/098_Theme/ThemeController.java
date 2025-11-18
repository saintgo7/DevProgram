package com.example.demo.controller;

import org.springframework.web.bind.annotation.*;
import org.springframework.stereotype.Controller;
import java.util.*;

@RestController
@RequestMapping("/api/theme")
public class ThemeController {

    @GetMapping
    public List<Map<String, Object>> getAll() {
        // Get all Theme
        return new ArrayList<>();
    }

    @GetMapping("/{id}")
    public Map<String, Object> getById(@PathVariable Long id) {
        // Get Theme by ID
        return new HashMap<>();
    }

    @PostMapping
    public Map<String, Object> create(@RequestBody Map<String, Object> data) {
        // Create Theme
        return data;
    }

    @PutMapping("/{id}")
    public Map<String, Object> update(@PathVariable Long id, @RequestBody Map<String, Object> data) {
        // Update Theme
        return data;
    }

    @DeleteMapping("/{id}")
    public void delete(@PathVariable Long id) {
        // Delete Theme
    }
}
