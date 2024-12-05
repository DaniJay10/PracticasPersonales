<?php
$peso = floatval($_POST["peso"]);
$altura = floatval($_POST["altura"]);
echo "La masa corporal es: " . $masaCorporal = $peso / ($altura ** 2);
?>