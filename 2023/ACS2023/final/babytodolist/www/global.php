<?php
error_reporting(E_ALL ^ E_NOTICE ^ E_WARNING);
ini_set('display_errors', '1');
session_start();

$conn = mysqli_connect("babytodo_db", "ctf", "ctf", "CTF");
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

function badwordfiltering($string){
	$string = preg_replace("/flag/i", "f-l-a-g", $string);
	return $string;
}

function decrypt($string){
	$r = substr(base64_decode($string), 1);
	return base64_decode($r);
}

if( is_array($_GET) )
{
	foreach($_GET as $k => $v){
		if(!is_array($v)){
		
			$_GET[$k]	= badwordfiltering($v);
			${$k}		= badwordfiltering($v);
		}
	}

	@reset($_GET);
}

if( is_array($_POST) )
{
	foreach($_POST as $k => $v){
		if(!is_array($v)){
		
			$_POST[$k]	= badwordfiltering($v);
			${$k}		= badwordfiltering($v);
		}
	}

	@reset($_POST);
}
if(isset($_COOKIE['preview_theme'])){
	$preview_theme = badwordfiltering(htmlspecialchars(decrypt($_COOKIE['preview_theme'])));
    $themes_fetch = mysqli_query($conn, "SELECT * FROM themes WHERE tname = '$preview_theme'");
    $theme = @mysqli_fetch_array($themes_fetch);
    if($theme){
        $preview = true;
    }
}
?>