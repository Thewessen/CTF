<?php
  
  $array = array("data" => "¿", "number" => "¿");

  $myarray = print_r($array,true);

  echo htmlentities("$myarray");

?>
