#!/usr/bin/env php
<?php
  
  /* $array = array("data" => "¿", "number" => "¿"); */

  /* $myarray = print_r($array,true); */

  /* echo htmlentities("$myarray"); */
  
  $real_query = array( 'query' => 'a' );
  $query = "ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw%3D";

  echo base64_encode(json_encode($real_query));

?>
