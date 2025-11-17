<?php
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
