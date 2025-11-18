package com.example.demo.controller;

import org.springframework.web.bind.annotation.*;
import org.springframework.stereotype.Controller;
import java.util.*;

@RestController
@RequestMapping("/api/response")
public class ResponseController {

    @GetMapping
    public List<Map<String, Object>> getAll() {
        // Get all Response
        return new ArrayList<>();
    }

    @GetMapping("/{id}")
    public Map<String, Object> getById(@PathVariable Long id) {
        // Get Response by ID
        return new HashMap<>();
    }

    @PostMapping
    public Map<String, Object> create(@RequestBody Map<String, Object> data) {
        // Create Response
        return data;
    }

    @PutMapping("/{id}")
    public Map<String, Object> update(@PathVariable Long id, @RequestBody Map<String, Object> data) {
        // Update Response
        return data;
    }

    @DeleteMapping("/{id}")
    public void delete(@PathVariable Long id) {
        // Delete Response
    }
}
