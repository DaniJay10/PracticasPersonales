<?php
//creacion de archivo TXT
$file="Base_datos_paciente.txt";
$fp=fopen($file, "a");
//Creacion de archivo JSON
$fileJSON = "Paciente.json";
$fpJSON = fopen($fileJSON, "a");
//recoleccion de metodo
$metodo = intval($_POST["metodo"]);

//clase
class Paciente {
    public $cedula;
    public $nombre;
    public $fecha_nacimiento;
    public $genero;
    // Constructor
    function __construct($cedula = null, $nombre = null, $fecha_nacimiento = null, $genero = null) {
        $this->cedula = $cedula;
        $this->nombre = $nombre;
        $this->fecha_nacimiento = $fecha_nacimiento;
        $this->genero = $genero;
    }
    //metodos
    //metodo de registrar datos
    function crear($cedula, $nombre, $fecha_nacimiento, $genero){
        global $fp, $fileJSON, $fpJSON;
        //Insertar datos en TXT
        $datos= $cedula . "," . $nombre . "," . $fecha_nacimiento . "," . $genero . "\n";
        fwrite($fp, $datos);
        fclose($fp);
        echo '<p style="color: green; font-weight: bold; background-color: #e0f7e0; padding: 10px; border-radius: 5px;">Datos registrados correctamente en (.TXT)</p>';
        //Insertar datos en JSON
        $datosJSON = [
        "Cedula" => $cedula,
        "Nombre" => $nombre,
        "Fecha_Nacimiento" => $fecha_nacimiento,
        "Genero" => $genero];
        
        if (file_exists($fileJSON)) {
            $contenido = file_get_contents($fileJSON);
            $jsonArray = json_decode($contenido, true);
            if (!is_array($jsonArray)) {
                $jsonArray = [];
            }} else {
            $jsonArray = [];
            }
 
        $jsonArray[] = $datosJSON;
        //guardamos los datos en $fileJSON
        file_put_contents($fileJSON, json_encode($jsonArray, JSON_PRETTY_PRINT));
        echo '<p style="color: green; font-weight: bold; background-color: #e0f7e0; padding: 10px; border-radius: 5px;">Datos registrados correctamente en (.JSON)</p>';
    }
    

    //metodo de actualizar datos
    function editar($cedula, $cedulaN, $nombre, $fecha_nacimiento, $genero){
        global $file, $fileJSON;
        $lineas=file($file);  //funcion file() agarra las lineas de un archivo y guarda cada una como si fuera un array
        $lineasArchivoActualizadas = [];
        $cedulaEncontrada = false;
        $cedulaEncontradaJSON = false;
        $cedulaOriginal = $cedula;
        for ($i=0;$i<count($lineas);$i++) {
            $linea = trim($lineas[$i]); 
            if (empty($linea)) continue;
            list($c, $n, $f, $g) = explode(",", $linea);//cada elemento de la linea le otorgo una variable.
            if ($c == $cedulaOriginal) {
                //proceso para actualizar o guardar la variable existentes esta vez usando OPERADOR TERNARIO
                $cedula = !empty($cedulaN) ? $cedulaN : $c;
                $nombre = !empty($nombre) ? $nombre : $n;
                $fecha_nacimiento = !empty($fecha_nacimiento) ? $fecha_nacimiento : $f;
                $genero = !empty($genero) ? $genero : $g;
                $actualizacionLinea = $cedula . "," . $nombre . "," . $fecha_nacimiento . "," . $genero . "\n";
                $lineasArchivoActualizadas[] = $actualizacionLinea;
                $cedulaEncontrada = true;
            }else{
                $lineasArchivoActualizadas[] = $linea . "\n";;
            }
        }

    //editacion en el archivo JSON
    if(file_exists($fileJSON)){
        $contenido = file_get_contents($fileJSON);
        $jsonArray = json_decode($contenido, true);
        for($i=0; $i<count($jsonArray);$i++){
            if($jsonArray[$i]['Cedula'] == $cedulaOriginal){
                $jsonArray[$i]['Cedula'] = !empty($cedulaN) ? $cedulaN : $jsonArray[$i]['Cedula']; 
                $jsonArray[$i]['Nombre'] = !empty($nombre) ? $nombre : $jsonArray[$i]['Nombre'];
                $jsonArray[$i]['Fecha_Nacimiento'] = !empty($fecha_nacimiento) ? $fecha_nacimiento : $jsonArray[$i]['Fecha_Nacimiento'];
                $jsonArray[$i]['Genero'] = !empty($genero) ? $genero : $jsonArray[$i]['Genero'];
                $cedulaEncontradaJSON = true;
            }
        }
    }else{
        echo '<p style="color: red; font-weight: bold; background-color: #f7e0e0; padding: 10px; border-radius: 5px;">El archivo JSON no existe</p>';
    }
            //editacion de filas
            if($cedulaEncontrada == true && $cedulaEncontradaJSON == true){
                //insertar cambios en txt
                $fp = fopen($file, "w");
                for ($i = 0; $i < count($lineasArchivoActualizadas); $i++) {
                fwrite($fp, $lineasArchivoActualizadas[$i]);
                }
                fclose($fp);
                echo '<p style="color: green; font-weight: bold; background-color: #e0f7e0; padding: 10px; border-radius: 5px;">Datos actualizados correctamente en (.TXT)</p>';
                //insertar cambios en JSON
                file_put_contents($fileJSON, json_encode($jsonArray, JSON_PRETTY_PRINT));
                echo '<p style="color: green; font-weight: bold; background-color: #e0f7e0; padding: 10px; border-radius: 5px;">Datos actualizados correctamente en (.JSON)</p>';
            }else {
                echo '<p style="color: red; font-weight: bold; background-color: #f7e0e0; padding: 10px; border-radius: 5px;">El paciente no existe</p>';
            } 


}



    //metodo de calcular edad
    function calcularEdad($cedula, $anioActual){
        global $file, $fileJSON;
        $fechaNacimiento = null;
        $fechaNacimientoJSON = null;
        //calculo en BS TXT
        $lineas=file($file);
        for ($i=0;$i<count($lineas);$i++) {
        $linea = $lineas[$i];
        list($c, $n, $f, $g) = explode(",", $linea);
        if($c == $cedula){
        $fechaNacimiento = new DateTime($f);//variable tipo DATE en PHP
        $fechaActual = new DateTime($anioActual);
        $edad = $fechaActual->diff($fechaNacimiento)->y;//y es diferencia en años, m mes, d dias, days dias totales
        echo '<p style="color: green; font-weight: bold; background-color: #e0f7e0; padding: 10px; border-radius: 5px;">La edad de ' . $n . ' es: ' . $edad . ' años (archivo .TXT)</p>';
        break;
        }
    }
     //Calculo en BS JSON
     if(file_exists($fileJSON)){
        $contenido = file_get_contents($fileJSON);
        $jsonArray = json_decode($contenido, true);
        for ($i = 0; $i < count($jsonArray); $i++) {
            if ($jsonArray[$i]['Cedula'] == $cedula) {
                $fechaNacimientoJSON = new DateTime($jsonArray[$i]['Fecha_Nacimiento']);
                $fechaActual = new DateTime($anioActual);
                $edad = $fechaActual->diff($fechaNacimientoJSON)->y;
                echo '<p style="color: green; font-weight: bold; background-color: #e0f7e0; padding: 10px; border-radius: 5px;">La edad de ' . $jsonArray[$i]['Nombre'] . ' es: ' . $edad . ' años (Archivo JSON)</p>';
            }
        }
     }else{
        echo "<p style='color: red; font-weight: bold; background-color: #f7e0e0; padding: 10px; border-radius: 5px;'>Archivo JSON no encontrado.</p><br>";
     }

        if ($fechaNacimiento === null && $fechaNacimientoJSON == null) {
            echo '<p style="color: red; font-weight: bold; background-color: #f7e0e0; padding: 10px; border-radius: 5px;">Paciente no encontrado en .TXT</p>';
            echo '<p style="color: red; font-weight: bold; background-color: #f7e0e0; padding: 10px; border-radius: 5px;">Paciente no encontrado en .JSON</p>';
        }
    }
    


 //metodo eliminar paciente
   function Eliminar($cedula){
    global $file, $fileJSON;
    $lineas=file($file);  
    $lineasArchivoActualizadas = [];
    $cedulaEncontrada = false;
    for ($i=0;$i<count($lineas);$i++) {
        $linea = trim($lineas[$i]); 
        if (empty($linea)) continue;
        list($c, $n, $f, $g) = explode(",", $linea);
        if ($c != $cedula) {
            $lineasArchivoActualizadas[] = $linea . "\n";
    }else{
        $cedulaEncontrada = true;
    }
}
    //eliminacion de fila
    if($cedulaEncontrada == true){
    $fp = fopen($file, "w");
    for ($i = 0; $i < count($lineasArchivoActualizadas); $i++) {
      fwrite($fp, $lineasArchivoActualizadas[$i]);
    }
    fclose($fp);
    echo "<p style='color: green; font-weight: bold; background-color: #e0f7e0; padding: 10px; border-radius: 5px;'>Paciente con cédula " . $cedula . " ha sido eliminado del .TXT</p>";
    }else{
        echo "<p style='color: red; font-weight: bold; background-color: #f7e0e0; padding: 10px; border-radius: 5px;'>Paciente no encontrado en TXT.</p>";
    }

    //Eliminacion en JSON
    if (file_exists($fileJSON)) {
        $contenido = file_get_contents($fileJSON);
        $jsonArray = json_decode($contenido, true); 
        
        if (is_array($jsonArray)) {
            // array_filter filtra el archivo como si fuera un array segun la condicion que le demos
            $jsonArrayFiltrado = array_filter($jsonArray, function($item) use ($cedula) { return $item['Cedula'] != $cedula;});
            if(count($jsonArrayFiltrado) === count($jsonArray)){
                echo "<p style='color: red; font-weight: bold; background-color: #f7e0e0; padding: 10px; border-radius: 5px;'>Paciente no encontrado en archivo JSON.</p>";
            }else{
                file_put_contents($fileJSON, json_encode($jsonArrayFiltrado, JSON_PRETTY_PRINT));
                echo "<p style='color: green; font-weight: bold; background-color: #e0f7e0; padding: 10px; border-radius: 5px;'>Paciente con cédula " . $cedula . " ha sido eliminado del .JSON</p>";
            }
        } else {
            echo "Error al leer el archivo JSON.<br>";
        }
    } else {
        echo "<p style='color: red; font-weight: bold; background-color: #f7e0e0; padding: 10px; border-radius: 5px;'>Archivo JSON no encontrado.</p><br>";
    }
}
   
}//fin clase
    







    //ejecucion de procesos
    

    if($metodo == 1){
        //atributos recolectados
        $ced=intval($_POST["cedula"]);
        $nom=$_POST["nombre"];
        $FeNac=$_POST["fechaNac"];
        $gen=$_POST["genero"];
        //ejecucion
        $Pacientes = new Paciente();
        echo $Pacientes->crear($ced, $nom, $FeNac, $gen);
    }

    elseif ($metodo == 2){
        //atributos recolectados
        $ced=intval($_POST["cedula"]);
        $cedN=intval($_POST["cedulaNueva"]);
        $nom=$_POST["nombre"];
        $FeNac=$_POST["fechaNac"];
        $gen=$_POST["genero"];
        //ejecucion
        $Pacientes = new Paciente();
        echo $Pacientes->editar($ced, $cedN, $nom, $FeNac, $gen);
    }


    elseif($metodo == 3){
        $ced=intval($_POST["cedula"]);
        $feAct=$_POST["fechaActual"];
        //ejecucion
        $Pacientes = new Paciente();
        echo $Pacientes->calcularEdad($ced, $feAct);
    }


    elseif($metodo == 4){
        $ced=intval($_POST["cedulaBorrar"]);
        //ejecucion
        $Pacientes = new Paciente();
        echo $Pacientes->Eliminar($ced);
    } 
    

    else {
        echo '<p>¡¡¡ERROR!!! Hubo algun error en procesos internos</p>';
    }

    echo "<a href='index.html' style='
    display: inline-block;
    padding: 10px 20px;
    background-color: #4CAF50;
    color: white;
    text-align: center;
    text-decoration: none;
    border-radius: 5px;
    font-size: 16px;
    margin-top: 20px;
    font-weight: bold;
    transition: background-color 0.3s ease;'>Regresar</a>";
?>