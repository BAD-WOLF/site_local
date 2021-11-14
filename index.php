<?php

	if(isset($_POST["text1"])){
		$num = $_POST["text1"];
		if($num % 2 == 0){
			echo $num,"\né um numero par";
		}else{
			echo $num,"\né um numero ipar";
		}
	
	}
?>
