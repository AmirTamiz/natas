<?php


$defaultdata = array("showpassword"=>"yes", "bgcolor"=>"#ffffff");
$text=json_encode($defaultdata);

 
function xor_encrypt($in) {
    $key = "qw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jq";
    $text = $in;
    $outText = null;

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }
	
	return base64_encode($outText);
	
}
$cookies=xor_encrypt($text);
echo "Set this Cookie:<br> data=".$cookies;


?>