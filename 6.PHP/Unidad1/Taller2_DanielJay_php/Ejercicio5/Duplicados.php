<?php
$elementos = $_POST["elemento"]; 
$duplicados = array();
for ($i = 0;$i<count($elementos);$i++) {
    for ($j = $i + 1; $j<count($elementos);$j++) {
        if ($elementos[$i] == $elementos[$j]) {
            $duplicados[] = $elementos[$i];
        }
    }
}

    if (!empty($duplicados)) {
        echo "Elementos duplicados: " . implode(", ", $duplicados);
    } else {
        echo "No hay elementos duplicados.";
    }
echo "<br><a href='Ejercicio5.html'>Regresar</a>";
?>