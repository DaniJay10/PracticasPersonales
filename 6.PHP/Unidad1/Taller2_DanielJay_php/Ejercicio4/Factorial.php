<?php
$numero = intval($_POST["numero"]);
$factorial = 1;
$factorialVisual = array();
for($i = 1;$i<=$numero;$i++){
    $factorial = $factorial * $i;
    $factorialVisual[]=$i;
}
echo "Terminos del factorial: " . implode("x",$factorialVisual) . "<br>";
echo "Resultado = " . $factorial;
?>