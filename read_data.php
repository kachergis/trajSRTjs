<?php
    $d = dir("/var/www/html/Test_Bas/data");
    while (false !== ($entry = $d->read())) {
        echo $entry."\n";
    }
    $d->close();
?>
