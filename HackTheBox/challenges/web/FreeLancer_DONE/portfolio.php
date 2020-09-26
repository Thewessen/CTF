<?php
// Include config file
require_once "administrat/include/config.php";
?>
<?php
 
$id = isset($_GET['id']) ? $_GET['id'] : '';
 
$query = "SELECT * FROM portfolio WHERE id = $id";
if ($result = mysqli_query($link, $query)) {

    /* fetch associative array */
    while ($row = mysqli_fetch_row($result)) {
        printf ("%s - %s\n", $row[1], $row[2]);
    }

    /* free result set */
    mysqli_free_result($result);
}

/* close connection */
mysqli_close($link);
?>
