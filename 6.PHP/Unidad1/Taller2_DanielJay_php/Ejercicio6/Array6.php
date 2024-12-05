<?php
echo '<form action="Posicion.php" method="POST">';
$longitud = intval($_POST["long"]);
for($i=1;$i<=$longitud;$i++){
    echo '<input type="text" name="elemento[]" id="numero' . $i . '" placeholder="Ingrese un número"/><br>';
}
echo '<p>Ingrese el número a buscar</p>';
echo '<input type="text" name="NumeroABuscar" id="NumeroABuscar" placeholder="Ingrese un número"/><br>';
echo '<input type="submit" name="EncontrarNumero" value="EncontrarNumero"/>';
echo "</form>";
echo "<br><a href='Ejercicio6.html'>Regresar</a>";
?>
