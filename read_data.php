<?php
    $d = dir("/var/www/html/MTBV/data");
    while (false !== ($entry = $d->read())) {
        echo $entry."\n";
    }
    $d->close();
?>
