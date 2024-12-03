<!DOCTYPE html>
<html>
<body>

<h1>Mi primera página en PHP</h1>

<?php
echo "¡Hola, mundo!";
?>

</body>
</html>

<?php
$nombre = "Juan";
$edad = 25;
$precio = 19.99;
$es_valido = true;
?>

<?php
$edad = 20;

if ($edad >= 18) {
    echo "Eres mayor de edad.";
} else {
    echo "Eres menor de edad.";
}
?>


<?php
for ($i = 0; $i < 5; $i++) {
    echo "Número: $i <br>";
}
?>


<?php
$i = 0;

while ($i < 5) {
    echo "Número: $i <br>";
    $i++;
}
?>


<?php
function saludar($nombre) {
    echo "¡Hola, $nombre!";
}

saludar("Juan");
?>



<?php
$frutas = array("Manzana", "Banana", "Naranja");
echo $frutas[0]; // Imprime "Manzana"
?>



<?php
$conn = mysqli_connect("localhost", "usuario", "contraseña", "base_de_datos");

if (!$conn) {
    die("Conexión fallida: " . mysqli_connect_error());
}

echo "Conexión exitosa";
?>
