<?php
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
