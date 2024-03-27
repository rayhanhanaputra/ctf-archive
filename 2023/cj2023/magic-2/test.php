<?php
$input="namafile.php";
$fileExtension = strtolower(pathinfo($input, PATHINFO_EXTENSION));
echo $fileExtension;
?>
