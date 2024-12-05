<?php
$numMes = intval($_POST["mes"]);
$mes = "";
$dias = 0;
if($numMes == 1){
    $mes = "Enero";
    }elseif($numMes == 2){
    $mes = "Febrero";
    }elseif($numMes == 3){
    $mes = "Marzo";
    }elseif($numMes == 4){
    $mes = "Abril";
    }elseif($numMes == 5){
    $mes = "Mayo";
    }elseif($numMes == 6){
    $mes = "Junio";
    }elseif($numMes == 7){
    $mes="Julio";
    }elseif($numMes == 8){
    $mes="Agosto";
    }elseif($numMes == 9){
    $mes="Septiembre";
    }elseif($numMes == 10){
    $mes="Octubre";
    }elseif($numMes ==11){
    $mes="Noviembre";
    }elseif($numMes == 12){
    $mes="Diciembre";
    }
    if($numMes == 2){
        $dias = 28;
    }
    if($numMes == 1 || $numMes == 3 || $numMes == 5 || $numMes == 7 || $numMes == 8 || $numMes == 10 || $numMes == 12){ 
        $dias = 31;
    }else {
        $dias = 30;
    }
    echo "Nombre del mes: " . $mes . "<br>";
    echo "Dias del mes: " . $dias;
?>