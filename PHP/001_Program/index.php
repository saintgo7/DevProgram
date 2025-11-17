<?php
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
