<?php
$servername = "localhost";
$username = "mysql";
$password = "mysql";
$database = "wafwaf";

// Create connection
$conn = mysqli_connect($servername, $username, $password, $database);

// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

$result = $conn->query("SELECT note FROM notes WHERE assignee = 'json'");
$rows = $result->fetch_assoc();

foreach ($rows as $row) {
    var_dump($row);
}

$conn->close();
?>
