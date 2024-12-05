<?php
$elementos = $_POST["elemento"]; 
$posicion = array();
$numero= intval($_POST["NumeroABuscar"]);
for($i=0;$i<count($elementos);$i++){
    if($elementos[$i]==$numero){
    $posicion[]=$i;
    }
}
if(!empty($posicion)){
    echo "Numero " . $numero . " Encontrado en posiciones: " . implode(", ", $posicion);
}else{
    echo "Numero " . $numero . " No encontrado";
}
echo "<br><a href='Ejercicio6.html'>Regresar</a>";
?>
