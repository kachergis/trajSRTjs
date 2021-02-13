<?php
    $d = dir("/var/www/html/MTBV2/data");
    while (false !== ($entry = $d->read())) {
        echo $entry."\n";
    }
    $d->close();
?>
