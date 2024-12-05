<?php
$numero = intval($_POST["num"]);
$sumatoria = 0;
$elementos = array();
for($i = 1;$i<=$numero;$i++){
    $sumatoria = $sumatoria + (1/$i);
    if ($i == 1){
        $elementos[]="1";
    }else {
        $elementos[]="1/" . $i;
    }
}
echo "sumatoria = " . implode(" + ", $elementos) . "<br>";
echo "total = " . $sumatoria;
?>