<?php
echo '<form method="POST" action="Duplicados.php">';
$longitud=intval($_POST["long"]);
for($i = 1; $i<=$longitud;$i++){
    echo '<input type="text" name="elemento[]" id="posicion' . $i . '" placeholder="Ingrese un número"/><br>';
}
echo '<input type="submit" name="EncontrarDuplicados" value="EncontrarDuplicados"/>';
echo '</form>';
echo "<br><a href='Ejercicio5.html'>Regresar</a>";
?>

