<?php
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
