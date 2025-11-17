<?php
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
