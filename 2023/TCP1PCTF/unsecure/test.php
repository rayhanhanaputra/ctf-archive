<?php
    $the_array = array("PHP","Object");
    $serialized = serialize($the_array);
    print $serialized;
    print base64_encode($serialized);

?>