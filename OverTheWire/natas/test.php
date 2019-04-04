<?php
  $cookie = "YTo3OntpOjA7YTo0OntzOjI6IngxIjtzOjI6IjIwIjtzOjI6InkxIjtzOjI6IjIwIjtzOjI6IngyIjtzOjI6IjQwIjtzOjI6InkyIjtzOjI6IjQwIjt9aToxO2E6NDp7czoyOiJ4MSI7czoyOiIyMCI7czoyOiJ5MSI7czoyOiIyMCI7czoyOiJ4MiI7czoyOiI0MCI7czoyOiJ5MiI7czoyOiI0MCI7fWk6MjthOjQ6e3M6MjoieDEiO3M6MjoiMjAiO3M6MjoieTEiO3M6MjoiMjAiO3M6MjoieDIiO3M6MjoiNDAiO3M6MjoieTIiO3M6MjoiNDAiO31pOjM7YTo0OntzOjI6IngxIjtzOjI6IjIwIjtzOjI6InkxIjtzOjI6IjIwIjtzOjI6IngyIjtzOjI6IjQwIjtzOjI6InkyIjtzOjI6IjQwIjt9aTo0O2E6NDp7czoyOiJ4MSI7czoyOiIxMCI7czoyOiJ5MSI7czoyOiIxMCI7czoyOiJ4MiI7czoyOiIxMCI7czoyOiJ5MiI7czoyOiIxMCI7fWk6NTthOjQ6e3M6MjoieDEiO3M6MjoiNTAiO3M6MjoieTEiO3M6MjoiNTAiO3M6MjoieDIiO3M6MjoiNTAiO3M6MjoieTIiO3M6MjoiNTAiO31pOjY7YTo0OntzOjI6IngxIjtzOjM6IjE1MCI7czoyOiJ5MSI7czoxOiIwIjtzOjI6IngyIjtzOjE6IjAiO3M6MjoieTIiO3M6MzoiMTUwIjt9fQ%3D%3D";
  $drawing=unserialize(base64_decode($cookie));
  foreach($drawing as $object) {
        echo "Start object\n";
        echo "x1:" . $object["x1"] . "\n";
        echo "y1:" . $object["y1"] . "\n";
        echo "x2:" . $object["x2"] . "\n";
        echo "y2:" . $object["y2"] . "\n"; 
        echo "End object\n";
    }
?>
