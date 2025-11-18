#!/usr/bin/env python3
"""
Script to create programs for all new web frameworks
"""

import os

# Framework configurations
frameworks = {
    "Laravel": {
        "ext": "php",
        "route_file": "routes/web.php",
        "controller_ext": "php",
        "template": """<?php

namespace App\\Http\\Controllers;

use Illuminate\\Http\\Request;

class {name}Controller extends Controller
{{
    public function index()
    {{
        return view('{name_lower}.index', [
            'title' => '{name}'
        ]);
    }}

    public function store(Request $request)
    {{
        // Store logic
        return response()->json(['message' => '{name} created']);
    }}
}}
""",
        "route": """<?php

use App\\Http\\Controllers\\{name}Controller;
use Illuminate\\Support\\Facades\\Route;

Route::get('/', function () {{
    return view('welcome');
}});

Route::resource('{name_lower}', {name}Controller::class);
"""
    },
    "SpringBoot": {
        "ext": "java",
        "controller_ext": "java",
        "template": """package com.example.demo.controller;

import org.springframework.web.bind.annotation.*;
import org.springframework.stereotype.Controller;
import java.util.*;

@RestController
@RequestMapping("/api/{name_lower}")
public class {name}Controller {{

    @GetMapping
    public List<Map<String, Object>> getAll() {{
        // Get all {name}
        return new ArrayList<>();
    }}

    @GetMapping("/{{id}}")
    public Map<String, Object> getById(@PathVariable Long id) {{
        // Get {name} by ID
        return new HashMap<>();
    }}

    @PostMapping
    public Map<String, Object> create(@RequestBody Map<String, Object> data) {{
        // Create {name}
        return data;
    }}

    @PutMapping("/{{id}}")
    public Map<String, Object> update(@PathVariable Long id, @RequestBody Map<String, Object> data) {{
        // Update {name}
        return data;
    }}

    @DeleteMapping("/{{id}}")
    public void delete(@PathVariable Long id) {{
        // Delete {name}
    }}
}}
"""
    },
    "Rails": {
        "ext": "rb",
        "controller_ext": "rb",
        "template": """class {name}Controller < ApplicationController
  before_action :set_{name_lower}, only: [:show, :edit, :update, :destroy]

  # GET /{name_lower}
  def index
    @{name_lower}s = {name}.all
    render json: @{name_lower}s
  end

  # GET /{name_lower}/1
  def show
    render json: @{name_lower}
  end

  # POST /{name_lower}
  def create
    @{name_lower} = {name}.new({name_lower}_params)

    if @{name_lower}.save
      render json: @{name_lower}, status: :created
    else
      render json: @{name_lower}.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /{name_lower}/1
  def update
    if @{name_lower}.update({name_lower}_params)
      render json: @{name_lower}
    else
      render json: @{name_lower}.errors, status: :unprocessable_entity
    end
  end

  # DELETE /{name_lower}/1
  def destroy
    @{name_lower}.destroy
    head :no_content
  end

  private

  def set_{name_lower}
    @{name_lower} = {name}.find(params[:id])
  end

  def {name_lower}_params
    params.require(:{name_lower}).permit(:name)
  end
end
"""
    },
    "Flask": {
        "ext": "py",
        "controller_ext": "py",
        "template": """from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{name_lower}.db'
db = SQLAlchemy(app)

class {name}(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {{'id': self.id, 'name': self.name}}

@app.route('/api/{name_lower}', methods=['GET'])
def get_all_{name_lower}():
    items = {name}.query.all()
    return jsonify([item.to_dict() for item in items])

@app.route('/api/{name_lower}/<int:id>', methods=['GET'])
def get_{name_lower}(id):
    item = {name}.query.get_or_404(id)
    return jsonify(item.to_dict())

@app.route('/api/{name_lower}', methods=['POST'])
def create_{name_lower}():
    data = request.get_json()
    item = {name}(name=data.get('name'))
    db.session.add(item)
    db.session.commit()
    return jsonify(item.to_dict()), 201

@app.route('/api/{name_lower}/<int:id>', methods=['PUT'])
def update_{name_lower}(id):
    item = {name}.query.get_or_404(id)
    data = request.get_json()
    item.name = data.get('name', item.name)
    db.session.commit()
    return jsonify(item.to_dict())

@app.route('/api/{name_lower}/<int:id>', methods=['DELETE'])
def delete_{name_lower}(id):
    item = {name}.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
"""
    },
    "Gin": {
        "ext": "go",
        "controller_ext": "go",
        "template": """package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type {name} struct {{
    ID   uint   `json:"id"`
    Name string `json:"name"`
}}

var {name_lower}s = []{{name}}{{}}

func getAll{name}s(c *gin.Context) {{
    c.JSON(http.StatusOK, {name_lower}s)
}}

func get{name}ByID(c *gin.Context) {{
    id := c.Param("id")
    // Find {name} by ID
    c.JSON(http.StatusOK, gin.H{{"id": id, "name": "{name}"}})
}}

func create{name}(c *gin.Context) {{
    var new{name} {name}
    if err := c.BindJSON(&new{name}); err != nil {{
        c.JSON(http.StatusBadRequest, gin.H{{"error": err.Error()}})
        return
    }}
    {name_lower}s = append({name_lower}s, new{name})
    c.JSON(http.StatusCreated, new{name})
}}

func update{name}(c *gin.Context) {{
    id := c.Param("id")
    var updated{name} {name}
    if err := c.BindJSON(&updated{name}); err != nil {{
        c.JSON(http.StatusBadRequest, gin.H{{"error": err.Error()}})
        return
    }}
    c.JSON(http.StatusOK, updated{name})
}}

func delete{name}(c *gin.Context) {{
    id := c.Param("id")
    // Delete {name}
    c.JSON(http.StatusNoContent, nil)
}}

func main() {{
    r := gin.Default()

    api := r.Group("/api")
    {{
        api.GET("/{name_lower}", getAll{name}s)
        api.GET("/{name_lower}/:id", get{name}ByID)
        api.POST("/{name_lower}", create{name})
        api.PUT("/{name_lower}/:id", update{name})
        api.DELETE("/{name_lower}/:id", delete{name})
    }}

    r.Run(":8080")
}}
"""
    },
    "Rocket": {
        "ext": "rs",
        "controller_ext": "rs",
        "template": """#[macro_use] extern crate rocket;

use rocket::serde::{{json::Json, Deserialize, Serialize}};
use rocket::State;
use std::sync::Mutex;

#[derive(Serialize, Deserialize, Clone)]
#[serde(crate = "rocket::serde")]
struct {name} {{
    id: u64,
    name: String,
}}

type {name}List = Mutex<Vec<{name}>>;

#[get("/{name_lower}")]
fn get_all(list: &State<{name}List>) -> Json<Vec<{name}>> {{
    let items = list.lock().unwrap();
    Json(items.clone())
}}

#[get("/{name_lower}/<id>")]
fn get_by_id(id: u64, list: &State<{name}List>) -> Option<Json<{name}>> {{
    let items = list.lock().unwrap();
    items.iter()
        .find(|item| item.id == id)
        .map(|item| Json(item.clone()))
}}

#[post("/{name_lower}", data = "<item>")]
fn create(item: Json<{name}>, list: &State<{name}List>) -> Json<{name}> {{
    let mut items = list.lock().unwrap();
    items.push(item.clone());
    item
}}

#[put("/{name_lower}/<id>", data = "<item>")]
fn update(id: u64, item: Json<{name}>, list: &State<{name}List>) -> Option<Json<{name}>> {{
    let mut items = list.lock().unwrap();
    items.iter_mut()
        .find(|i| i.id == id)
        .map(|i| {{
            *i = item.clone();
            Json(i.clone())
        }})
}}

#[delete("/{name_lower}/<id>")]
fn delete(id: u64, list: &State<{name}List>) -> Option<()> {{
    let mut items = list.lock().unwrap();
    let pos = items.iter().position(|i| i.id == id)?;
    items.remove(pos);
    Some(())
}}

#[launch]
fn rocket() -> _ {{
    rocket::build()
        .manage({name}List::new(Vec::new()))
        .mount("/api", routes![get_all, get_by_id, create, update, delete])
}}
"""
    }
}

# Common program names
program_names = [
    "User", "Product", "Order", "Customer", "Invoice",
    "Payment", "Category", "Tag", "Comment", "Review",
    "Article", "Blog", "Post", "Page", "Media",
    "Album", "Photo", "Video", "Audio", "File",
    "Message", "Notification", "Email", "SMS", "Alert",
    "Task", "Project", "Milestone", "Sprint", "Issue",
    "Team", "Member", "Role", "Permission", "Group",
    "Event", "Calendar", "Schedule", "Appointment", "Booking",
    "Inventory", "Stock", "Warehouse", "Shipment", "Delivery",
    "Supplier", "Vendor", "Manufacturer", "Distributor", "Retailer",
    "Transaction", "Account", "Balance", "Statement", "Report",
    "Analytics", "Metric", "Dashboard", "Chart", "Graph",
    "Survey", "Question", "Answer", "Vote", "Poll",
    "Contact", "Address", "Phone", "Location", "Geography",
    "Settings", "Configuration", "Preference", "Option", "Feature",
    "Session", "Token", "Authentication", "Authorization", "Security",
    "Log", "Audit", "History", "Activity", "Timeline",
    "Search", "Filter", "Sort", "Pagination", "Export",
    "Import", "Sync", "Backup", "Restore", "Archive",
    "Template", "Layout", "Theme", "Style", "Asset",
    "Widget", "Component", "Module", "Plugin", "Extension",
    "API", "Endpoint", "Route", "Controller", "Model",
    "Service", "Repository", "Factory", "Builder", "Adapter",
    "Middleware", "Filter", "Guard", "Interceptor", "Decorator",
    "Validator", "Sanitizer", "Transformer", "Mapper", "Converter",
    "Cache", "Queue", "Job", "Worker", "Scheduler",
    "Database", "Migration", "Seeder", "Schema", "Table",
    "Relationship", "Association", "Join", "Query", "Criteria",
    "Form", "Input", "Field", "Validation", "Error",
    "Response", "Request", "Header", "Cookie", "Session",
    "Upload", "Download", "Stream", "Chunk", "Buffer",
    "Encryption", "Hashing", "Signing", "Verification", "Certificate",
    "OAuth", "JWT", "SAML", "LDAP", "SSO",
    "WebSocket", "RealTime", "Pusher", "Broadcast", "Channel",
    "Subscription", "Plan", "Billing", "Charge", "Refund",
    "Coupon", "Discount", "Promotion", "Offer", "Deal",
    "Cart", "Checkout", "PaymentMethod", "CreditCard", "PayPal",
    "Shipping", "Tracking", "Carrier", "Zone", "Rate",
    "Tax", "VAT", "GST", "Customs", "Duty",
    "Wishlist", "Favorite", "Bookmark", "Like", "Follow",
    "Feed", "Stream", "Timeline", "Wall", "Activity",
    "Friend", "Connection", "Network", "Follower", "Following",
    "Chat", "Conversation", "Thread", "Reply", "Mention",
    "Hashtag", "Trend", "Topic", "Subject", "Keyword",
    "Rating", "Score", "Point", "Badge", "Achievement",
    "Level", "Rank", "Leaderboard", "Competition", "Prize",
    "Reward", "Gift", "Voucher", "Credit", "Loyalty",
    "Referral", "Affiliate", "Commission", "Payout", "Withdrawal",
    "Budget", "Expense", "Income", "Revenue", "Profit",
    "Forecast", "Prediction", "Estimate", "Projection", "Target",
    "Goal", "Objective", "KPI", "Metric", "Indicator",
    "Department", "Division", "Branch", "Office", "Store",
    "Employee", "Staff", "Contractor", "Freelancer", "Intern",
    "Salary", "Wage", "Bonus", "Benefit", "Deduction",
    "Leave", "Absence", "Holiday", "Vacation", "TimeOff",
    "Attendance", "Timesheet", "Shift", "Roster", "Duty",
    "Training", "Course", "Lesson", "Module", "Certificate",
]

# Create programs for each framework
for framework_name, config in frameworks.items():
    print(f"Creating {framework_name} programs...")
    framework_dir = f"/home/user/DevProgram/{framework_name}"
    os.makedirs(framework_dir, exist_ok=True)

    for i, prog_name in enumerate(program_names[:200], 1):
        folder_name = f"{i:03d}_{prog_name}"
        folder_path = os.path.join(framework_dir, folder_name)
        os.makedirs(folder_path, exist_ok=True)

        # Create controller/main file
        filename = f"{prog_name}Controller.{config['ext']}" if framework_name != "Gin" and framework_name != "Rocket" else f"main.{config['ext']}"
        file_path = os.path.join(folder_path, filename)

        code = config["template"].format(
            name=prog_name,
            name_lower=prog_name.lower()
        )

        with open(file_path, 'w') as f:
            f.write(code)

        # Create README
        readme_path = os.path.join(folder_path, "README.md")
        framework_cmd = {
            "Laravel": "php artisan serve",
            "SpringBoot": "mvn spring-boot:run",
            "Rails": "rails server",
            "Flask": "python app.py",
            "Gin": "go run main.go",
            "Rocket": "cargo run"
        }

        with open(readme_path, 'w') as f:
            f.write(f"""# {prog_name} API

## Description
{prog_name} RESTful API implementation in {framework_name}.

## Endpoints
- GET    /api/{prog_name.lower()} - Get all {prog_name}s
- GET    /api/{prog_name.lower()}/{{id}} - Get {prog_name} by ID
- POST   /api/{prog_name.lower()} - Create new {prog_name}
- PUT    /api/{prog_name.lower()}/{{id}} - Update {prog_name}
- DELETE /api/{prog_name.lower()}/{{id}} - Delete {prog_name}

## Usage
```bash
{framework_cmd.get(framework_name, 'run server')}
```

## Features
- RESTful API design
- CRUD operations
- {framework_name} best practices
- JSON responses
""")

    print(f"✅ Created 200 {framework_name} programs in {framework_dir}")

print("\n✅ All frameworks completed!")
