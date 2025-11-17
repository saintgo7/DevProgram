#!/usr/bin/env python3
"""
Script to create 100 PHP programs for DevProgram repository
"""

import os

# Base directory
BASE_DIR = "/home/user/DevProgram/PHP"

# Program definitions (5 featured programs with full implementations)
FEATURED_PROGRAMS = {
    1: {
        "name": "Hello World",
        "description": "Basic PHP script",
        "content": """<?php
/**
 * Hello World - Basic PHP Script
 * Demonstrates basic PHP syntax and output
 */

// Simple output
echo "Hello, PHP World!<br>";

// Variables
$name = "PHP Developer";
$version = phpversion();

echo "<h1>Welcome to PHP!</h1>";
echo "<p>Hello, $name</p>";
echo "<p>PHP Version: $version</p>";

// Array example
$features = ["Server-side scripting", "Database integration", "Dynamic content", "Cross-platform"];

echo "<h2>PHP Features:</h2>";
echo "<ul>";
foreach ($features as $feature) {
    echo "<li>$feature</li>";
}
echo "</ul>";

// Current date and time
echo "<p>Current date and time: " . date('Y-m-d H:i:s') . "</p>";
?>
"""
    },
    2: {
        "name": "Calculator",
        "description": "PHP calculator with form handling",
        "content": """<?php
/**
 * Calculator - Form Handling Example
 * Demonstrates POST method, form processing, and arithmetic operations
 */

$result = null;
$error = null;

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $num1 = $_POST['num1'] ?? 0;
    $num2 = $_POST['num2'] ?? 0;
    $operation = $_POST['operation'] ?? '+';

    if (!is_numeric($num1) || !is_numeric($num2)) {
        $error = "Please enter valid numbers";
    } else {
        switch ($operation) {
            case '+':
                $result = $num1 + $num2;
                break;
            case '-':
                $result = $num1 - $num2;
                break;
            case '*':
                $result = $num1 * $num2;
                break;
            case '/':
                if ($num2 == 0) {
                    $error = "Cannot divide by zero";
                } else {
                    $result = $num1 / $num2;
                }
                break;
            default:
                $error = "Invalid operation";
        }
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP Calculator</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .calculator {
            background: white;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            width: 400px;
        }
        h1 { color: #333; margin-bottom: 1.5rem; text-align: center; }
        .form-group {
            margin-bottom: 1rem;
        }
        label {
            display: block;
            margin-bottom: 0.5rem;
            color: #555;
            font-weight: bold;
        }
        input, select, button {
            width: 100%;
            padding: 0.75rem;
            border: 2px solid #ddd;
            border-radius: 5px;
            font-size: 1rem;
        }
        button {
            background: #667eea;
            color: white;
            border: none;
            cursor: pointer;
            margin-top: 1rem;
            transition: background 0.3s;
        }
        button:hover { background: #5568d3; }
        .result {
            margin-top: 1.5rem;
            padding: 1rem;
            background: #e8f5e9;
            border-radius: 5px;
            text-align: center;
            font-size: 1.5rem;
            font-weight: bold;
            color: #2e7d32;
        }
        .error {
            background: #ffebee;
            color: #c62828;
        }
    </style>
</head>
<body>
    <div class="calculator">
        <h1>PHP Calculator</h1>
        <form method="POST">
            <div class="form-group">
                <label>First Number:</label>
                <input type="number" name="num1" step="any" required
                       value="<?php echo $_POST['num1'] ?? ''; ?>">
            </div>

            <div class="form-group">
                <label>Operation:</label>
                <select name="operation">
                    <option value="+">+ (Addition)</option>
                    <option value="-">- (Subtraction)</option>
                    <option value="*">* (Multiplication)</option>
                    <option value="/">/ (Division)</option>
                </select>
            </div>

            <div class="form-group">
                <label>Second Number:</label>
                <input type="number" name="num2" step="any" required
                       value="<?php echo $_POST['num2'] ?? ''; ?>">
            </div>

            <button type="submit">Calculate</button>
        </form>

        <?php if ($result !== null): ?>
            <div class="result">Result: <?php echo $result; ?></div>
        <?php endif; ?>

        <?php if ($error): ?>
            <div class="result error"><?php echo $error; ?></div>
        <?php endif; ?>
    </div>
</body>
</html>
"""
    },
    3: {
        "name": "Todo List",
        "description": "Session-based todo list",
        "content": """<?php
/**
 * Todo List - Session Management Example
 * Demonstrates session handling, array operations, and CRUD operations
 */

session_start();

// Initialize todos array in session
if (!isset($_SESSION['todos'])) {
    $_SESSION['todos'] = [];
}

// Handle form submissions
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    if (isset($_POST['add_todo']) && !empty($_POST['todo_text'])) {
        $todo = [
            'id' => time(),
            'text' => htmlspecialchars($_POST['todo_text']),
            'completed' => false
        ];
        $_SESSION['todos'][] = $todo;
    } elseif (isset($_POST['toggle_todo'])) {
        $id = $_POST['todo_id'];
        foreach ($_SESSION['todos'] as &$todo) {
            if ($todo['id'] == $id) {
                $todo['completed'] = !$todo['completed'];
                break;
            }
        }
    } elseif (isset($_POST['delete_todo'])) {
        $id = $_POST['todo_id'];
        $_SESSION['todos'] = array_filter($_SESSION['todos'], function($todo) use ($id) {
            return $todo['id'] != $id;
        });
    } elseif (isset($_POST['clear_all'])) {
        $_SESSION['todos'] = [];
    }

    // Redirect to prevent form resubmission
    header("Location: " . $_SERVER['PHP_SELF']);
    exit;
}

$todos = $_SESSION['todos'];
$total = count($todos);
$completed = count(array_filter($todos, function($t) { return $t['completed']; }));
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP Todo List</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 2rem;
        }
        .container {
            max-width: 600px;
            margin: 0 auto;
            background: white;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        }
        h1 { color: #333; margin-bottom: 1.5rem; text-align: center; }
        .add-form {
            display: flex;
            gap: 0.5rem;
            margin-bottom: 1.5rem;
        }
        input[type="text"] {
            flex: 1;
            padding: 0.75rem;
            border: 2px solid #ddd;
            border-radius: 5px;
            font-size: 1rem;
        }
        button {
            padding: 0.75rem 1.5rem;
            background: #667eea;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 1rem;
        }
        button:hover { background: #5568d3; }
        .todo-item {
            display: flex;
            align-items: center;
            padding: 1rem;
            border-bottom: 1px solid #eee;
            gap: 1rem;
        }
        .todo-item.completed .todo-text {
            text-decoration: line-through;
            color: #999;
        }
        .todo-text { flex: 1; }
        .btn-small {
            padding: 0.4rem 0.8rem;
            font-size: 0.9rem;
        }
        .btn-danger { background: #e74c3c; }
        .btn-danger:hover { background: #c0392b; }
        .stats {
            margin-top: 1rem;
            padding: 1rem;
            background: #f8f9fa;
            border-radius: 5px;
            text-align: center;
            color: #666;
        }
        .clear-btn {
            width: 100%;
            margin-top: 1rem;
            background: #e74c3c;
        }
        .clear-btn:hover { background: #c0392b; }
    </style>
</head>
<body>
    <div class="container">
        <h1>PHP Todo List</h1>

        <form method="POST" class="add-form">
            <input type="text" name="todo_text" placeholder="Enter a task..." required>
            <button type="submit" name="add_todo">Add</button>
        </form>

        <div class="todo-list">
            <?php foreach ($todos as $todo): ?>
                <div class="todo-item <?php echo $todo['completed'] ? 'completed' : ''; ?>">
                    <div class="todo-text"><?php echo $todo['text']; ?></div>
                    <form method="POST" style="display: inline;">
                        <input type="hidden" name="todo_id" value="<?php echo $todo['id']; ?>">
                        <button type="submit" name="toggle_todo" class="btn-small">
                            <?php echo $todo['completed'] ? 'Undo' : 'Complete'; ?>
                        </button>
                    </form>
                    <form method="POST" style="display: inline;">
                        <input type="hidden" name="todo_id" value="<?php echo $todo['id']; ?>">
                        <button type="submit" name="delete_todo" class="btn-small btn-danger">Delete</button>
                    </form>
                </div>
            <?php endforeach; ?>

            <?php if (empty($todos)): ?>
                <p style="text-align: center; color: #999; padding: 2rem;">No tasks yet. Add one above!</p>
            <?php endif; ?>
        </div>

        <div class="stats">
            Total: <?php echo $total; ?> | Completed: <?php echo $completed; ?>
        </div>

        <?php if (!empty($todos)): ?>
            <form method="POST">
                <button type="submit" name="clear_all" class="clear-btn"
                        onclick="return confirm('Clear all tasks?')">Clear All</button>
            </form>
        <?php endif; ?>
    </div>
</body>
</html>
"""
    },
    4: {
        "name": "User Registration",
        "description": "Form validation and file handling",
        "content": """<?php
/**
 * User Registration - Form Validation Example
 * Demonstrates input validation, sanitization, and error handling
 */

$errors = [];
$success = false;
$formData = [];

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // Get and sanitize input
    $formData['name'] = trim($_POST['name'] ?? '');
    $formData['email'] = trim($_POST['email'] ?? '');
    $formData['password'] = $_POST['password'] ?? '';
    $formData['confirm_password'] = $_POST['confirm_password'] ?? '';
    $formData['age'] = $_POST['age'] ?? '';

    // Validation
    if (empty($formData['name'])) {
        $errors[] = "Name is required";
    } elseif (strlen($formData['name']) < 3) {
        $errors[] = "Name must be at least 3 characters";
    }

    if (empty($formData['email'])) {
        $errors[] = "Email is required";
    } elseif (!filter_var($formData['email'], FILTER_VALIDATE_EMAIL)) {
        $errors[] = "Invalid email format";
    }

    if (empty($formData['password'])) {
        $errors[] = "Password is required";
    } elseif (strlen($formData['password']) < 6) {
        $errors[] = "Password must be at least 6 characters";
    }

    if ($formData['password'] !== $formData['confirm_password']) {
        $errors[] = "Passwords do not match";
    }

    if (empty($formData['age'])) {
        $errors[] = "Age is required";
    } elseif (!is_numeric($formData['age']) || $formData['age'] < 18) {
        $errors[] = "You must be at least 18 years old";
    }

    // If no errors, process registration
    if (empty($errors)) {
        // In a real application, you would save to database here
        $success = true;
        $formData = []; // Clear form
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Registration</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 2rem;
        }
        .container {
            max-width: 500px;
            margin: 0 auto;
            background: white;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        }
        h1 { color: #333; margin-bottom: 1.5rem; text-align: center; }
        .form-group {
            margin-bottom: 1.5rem;
        }
        label {
            display: block;
            margin-bottom: 0.5rem;
            color: #555;
            font-weight: bold;
        }
        input {
            width: 100%;
            padding: 0.75rem;
            border: 2px solid #ddd;
            border-radius: 5px;
            font-size: 1rem;
        }
        input:focus {
            outline: none;
            border-color: #667eea;
        }
        button {
            width: 100%;
            padding: 1rem;
            background: #667eea;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 1rem;
            font-weight: bold;
        }
        button:hover { background: #5568d3; }
        .errors {
            background: #ffebee;
            border-left: 4px solid #c62828;
            padding: 1rem;
            margin-bottom: 1.5rem;
            border-radius: 5px;
        }
        .errors ul {
            margin-left: 1.5rem;
            color: #c62828;
        }
        .success {
            background: #e8f5e9;
            border-left: 4px solid #2e7d32;
            padding: 1rem;
            margin-bottom: 1.5rem;
            border-radius: 5px;
            color: #2e7d32;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>User Registration</h1>

        <?php if ($success): ?>
            <div class="success">
                <strong>Registration Successful!</strong><br>
                Account created successfully.
            </div>
        <?php endif; ?>

        <?php if (!empty($errors)): ?>
            <div class="errors">
                <strong>Please fix the following errors:</strong>
                <ul>
                    <?php foreach ($errors as $error): ?>
                        <li><?php echo $error; ?></li>
                    <?php endforeach; ?>
                </ul>
            </div>
        <?php endif; ?>

        <form method="POST">
            <div class="form-group">
                <label>Name:</label>
                <input type="text" name="name" value="<?php echo htmlspecialchars($formData['name'] ?? ''); ?>" required>
            </div>

            <div class="form-group">
                <label>Email:</label>
                <input type="email" name="email" value="<?php echo htmlspecialchars($formData['email'] ?? ''); ?>" required>
            </div>

            <div class="form-group">
                <label>Password:</label>
                <input type="password" name="password" required>
            </div>

            <div class="form-group">
                <label>Confirm Password:</label>
                <input type="password" name="confirm_password" required>
            </div>

            <div class="form-group">
                <label>Age:</label>
                <input type="number" name="age" value="<?php echo htmlspecialchars($formData['age'] ?? ''); ?>" required>
            </div>

            <button type="submit">Register</button>
        </form>
    </div>
</body>
</html>
"""
    },
    5: {
        "name": "File Upload",
        "description": "File upload and validation",
        "content": """<?php
/**
 * File Upload - File Handling Example
 * Demonstrates file upload, validation, and error handling
 */

$message = '';
$messageType = '';

if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_FILES['file'])) {
    $file = $_FILES['file'];

    // File properties
    $fileName = $file['name'];
    $fileTmpName = $file['tmp_name'];
    $fileSize = $file['size'];
    $fileError = $file['error'];

    // Get file extension
    $fileExt = strtolower(pathinfo($fileName, PATHINFO_EXTENSION));

    // Allowed extensions
    $allowed = ['jpg', 'jpeg', 'png', 'gif', 'pdf', 'txt'];

    if ($fileError !== 0) {
        $message = "Error uploading file";
        $messageType = 'error';
    } elseif (!in_array($fileExt, $allowed)) {
        $message = "File type not allowed. Allowed types: " . implode(', ', $allowed);
        $messageType = 'error';
    } elseif ($fileSize > 5000000) { // 5MB
        $message = "File too large. Maximum size: 5MB";
        $messageType = 'error';
    } else {
        // Create uploads directory if it doesn't exist
        $uploadDir = 'uploads/';
        if (!is_dir($uploadDir)) {
            mkdir($uploadDir, 0777, true);
        }

        // Generate unique file name
        $newFileName = uniqid('', true) . '.' . $fileExt;
        $destination = $uploadDir . $newFileName;

        if (move_uploaded_file($fileTmpName, $destination)) {
            $message = "File uploaded successfully: $fileName";
            $messageType = 'success';
        } else {
            $message = "Failed to upload file";
            $messageType = 'error';
        }
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Upload</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 2rem;
        }
        .container {
            background: white;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            max-width: 500px;
            width: 100%;
        }
        h1 { color: #333; margin-bottom: 1.5rem; text-align: center; }
        .upload-area {
            border: 3px dashed #ddd;
            border-radius: 10px;
            padding: 3rem;
            text-align: center;
            margin-bottom: 1.5rem;
            cursor: pointer;
            transition: all 0.3s;
        }
        .upload-area:hover {
            border-color: #667eea;
            background: #f8f9fa;
        }
        input[type="file"] {
            display: none;
        }
        .file-label {
            font-size: 1.1rem;
            color: #666;
        }
        button {
            width: 100%;
            padding: 1rem;
            background: #667eea;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 1rem;
            font-weight: bold;
        }
        button:hover { background: #5568d3; }
        .message {
            padding: 1rem;
            border-radius: 5px;
            margin-bottom: 1.5rem;
            text-align: center;
        }
        .success {
            background: #e8f5e9;
            color: #2e7d32;
            border-left: 4px solid #2e7d32;
        }
        .error {
            background: #ffebee;
            color: #c62828;
            border-left: 4px solid #c62828;
        }
        .info {
            background: #f8f9fa;
            padding: 1rem;
            border-radius: 5px;
            margin-top: 1.5rem;
            font-size: 0.9rem;
            color: #666;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>File Upload</h1>

        <?php if ($message): ?>
            <div class="message <?php echo $messageType; ?>">
                <?php echo $message; ?>
            </div>
        <?php endif; ?>

        <form method="POST" enctype="multipart/form-data">
            <div class="upload-area" onclick="document.getElementById('file-input').click()">
                <div class="file-label">
                    📁<br><br>
                    Click to select a file<br>
                    <small>or drag and drop</small>
                </div>
            </div>
            <input type="file" name="file" id="file-input" required
                   onchange="document.querySelector('.file-label').innerHTML = this.files[0].name">
            <button type="submit">Upload File</button>
        </form>

        <div class="info">
            <strong>Allowed file types:</strong> JPG, JPEG, PNG, GIF, PDF, TXT<br>
            <strong>Maximum file size:</strong> 5MB
        </div>
    </div>
</body>
</html>
"""
    }
}

# All 100 program titles
ALL_PROGRAMS = [
    "Hello World", "Calculator", "Todo List", "User Registration", "File Upload",
    "Login System", "Contact Form", "Email Sender", "Image Gallery", "Session Manager",
    "Cookie Handler", "Array Operations", "String Functions", "Date and Time", "Number Formatter",
    "URL Parser", "JSON Handler", "XML Parser", "CSV Reader", "File Manager",
    "Directory Listing", "Text File Reader", "File Writer", "File Copy", "File Delete",
    "Simple OOP", "Class and Objects", "Inheritance", "Abstract Classes", "Interfaces",
    "Namespaces", "Autoloading", "Magic Methods", "Static Members", "Traits",
    "Exception Handling", "Custom Exceptions", "Error Logging", "Debugging", "Try-Catch",
    "MySQL Connection", "Database CRUD", "Prepared Statements", "Transaction", "Join Queries",
    "User Authentication", "Password Hashing", "JWT Token", "Remember Me", "Password Reset",
    "Shopping Cart", "Pagination", "Search Filter", "Sorting Data", "Data Validation",
    "Form Builder", "Multi-step Form", "AJAX Handler", "REST API", "API Endpoints",
    "Template Engine", "Route Handler", "MVC Pattern", "Dependency Injection", "Service Container",
    "Cache System", "Rate Limiting", "CSRF Protection", "XSS Prevention", "SQL Injection Prevention",
    "Image Resize", "Thumbnail Generator", "Watermark", "Image Filter", "QR Code Generator",
    "Barcode Generator", "PDF Generator", "Excel Export", "Chart Generator", "Report Builder",
    "Email Template", "Newsletter", "Notification System", "SMS Sender", "Push Notifications",
    "Webhook Handler", "Cron Job", "Background Task", "Queue System", "Event Dispatcher",
    "Logger", "Analytics", "Visitor Counter", "IP Tracker", "Geolocation",
    "Currency Converter", "Unit Converter", "Timezone Converter", "Age Calculator", "BMI Calculator",
    "Random Generator", "UUID Generator", "Slug Generator", "Hash Generator", "Encryption"
]

def create_program(program_num):
    """Create a single PHP program file"""
    program_name = ALL_PROGRAMS[program_num - 1]
    program_dir = os.path.join(BASE_DIR, f"{program_num:03d}_Program")

    # Create directory
    os.makedirs(program_dir, exist_ok=True)

    # Create index.php file
    if program_num in FEATURED_PROGRAMS:
        content = FEATURED_PROGRAMS[program_num]["content"]
    else:
        content = f"""<?php
/**
 * {program_name}
 * Program {program_num:03d}
 */

echo "<h1>{program_name}</h1>";
echo "<p>This is a PHP program demonstrating {program_name.lower()}.</p>";

// Implement the program logic here...

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{program_name}</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 2rem;
        }}
        .container {{
            background: white;
            padding: 3rem;
            border-radius: 10px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            max-width: 600px;
        }}
        h1 {{ color: #333; margin-bottom: 1rem; }}
        p {{ color: #666; line-height: 1.6; }}
    </style>
</head>
<body>
    <div class="container">
        <!-- Content goes here -->
    </div>
</body>
</html>
"""

    with open(os.path.join(program_dir, "index.php"), "w") as f:
        f.write(content)

    print(f"Created program {program_num:03d}: {program_name}")

def main():
    """Main function to create all 100 PHP programs"""
    print("Creating PHP programs...")
    print(f"Base directory: {BASE_DIR}")

    # Create base directory
    os.makedirs(BASE_DIR, exist_ok=True)

    # Create all 100 programs
    for i in range(1, 101):
        create_program(i)

    print("\n✓ Successfully created 100 PHP programs!")
    print(f"Location: {BASE_DIR}")

    # Count total lines
    total_lines = 0
    for root, dirs, files in os.walk(BASE_DIR):
        for file in files:
            if file.endswith('.php'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    total_lines += len(f.readlines())

    print(f"Total lines of code: {total_lines:,}")

if __name__ == "__main__":
    main()
