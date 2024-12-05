<?php
//creacion de archivo 
$file="Base_datos_paciente.txt";
$fp=fopen($file, "a");

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
        global $fp;
        $datos= $cedula . "," . $nombre . "," . $fecha_nacimiento . "," . $genero . "\n";
        fwrite($fp, $datos);
        fclose($fp);
        echo '<p>Datos registrados correctamente</p>';
    }
    

    //metodo de actualizar datos
    function editar($cedula, $cedulaN, $nombre, $fecha_nacimiento, $genero){
        $file="Base_datos_paciente.txt";
        $lineas=file($file);  //funcion file() agarra las lineas de un archivo y guarda cada una como si fuera un array
        $lineasArchivoActualizadas = [];
        $cedulaEncontrada = false;
        for ($i=0;$i<count($lineas);$i++) {
            $linea = trim($lineas[$i]); 
            if (empty($linea)) continue;
            list($c, $n, $f, $g) = explode(",", $linea);//cada elemento de la linea le otorgo una variable.
            if ($c == $cedula) {
                //proceso para actualizar o guardar la variable existentes
                if (!empty($cedulaN)) {
                    $cedula = $cedulaN;  
                } else {
                    $cedula = $c; 
                }
                if (!empty($nombre)) {
                    $nombre = $nombre;  
                } else {
                    $nombre = $n; 
                }
                if (!empty($fecha_nacimiento)) {
                    $fecha_nacimiento = $fecha_nacimiento;  
                } else {
                    $fecha_nacimiento = $f; 
                }
                if (!empty($genero)) {
                    $genero = $genero;  
                } else {
                    $genero = $g; 
                }
                $actualizacionLinea = $cedula . "," . $nombre . "," . $fecha_nacimiento . "," . $genero . "\n";
                $lineasArchivoActualizadas[] = $actualizacionLinea;
                $cedulaEncontrada = true;
            }else{
                $lineasArchivoActualizadas[] = $linea . "\n";;
            }
        }
        //editacion de filas
        if($cedulaEncontrada == true){
        $fp = fopen($file, "w");
        for ($i = 0; $i < count($lineasArchivoActualizadas); $i++) {//con este for usaremos w para sobreescribir el documento con las nuevas filas
        fwrite($fp, $lineasArchivoActualizadas[$i]);
        }
        fclose($fp);
        echo '<p>Datos actualizados correctamente</p>';
    }else {
        echo '<p>El paciente no existe</p>';
    }
}


    //metodo de calcular edad
    function calcularEdad($cedula, $anioActual){
        $file="Base_datos_paciente.txt";
        $lineas=file($file);
        $fechaNacimiento = null;
        for ($i=0;$i<count($lineas);$i++) {
        $linea = $lineas[$i];
        list($c, $n, $f, $g) = explode(",", $linea);
        if($c == $cedula){
        $fechaNacimiento = new DateTime($f);//variable tipo DATE en PHP 
        break;
        }
    }
        if ($fechaNacimiento === null) {
            echo "Paciente no encontrado";
        }

        $fechaActual = new DateTime($anioActual);
        $edad = $fechaActual->diff($fechaNacimiento)->y;//y es diferencia en años, m mes, d dias, days dias totales
        echo 'La edad de ' . $n . ' es: ' . $edad . ' años<br>';
    }
    
    //metodo eliminar edad
    function Eliminar($cedula){
        $file="Base_datos_paciente.txt";
        $lineas=file($file);  
        $lineasArchivoActualizadas = [];
        for ($i=0;$i<count($lineas);$i++) {
            $linea = trim($lineas[$i]); 
            if (empty($linea)) continue;
            list($c, $n, $f, $g) = explode(",", $linea);
            if ($c != $cedula) {
                $lineasArchivoActualizadas[] = $linea . "\n";;
        }
    }
    //eliminacion de fila
    $fp = fopen($file, "w");
    for ($i = 0; $i < count($lineasArchivoActualizadas); $i++) {
        fwrite($fp, $lineasArchivoActualizadas[$i]);
    }

    fclose($fp);
    echo "Paciente con cédula " . $cedula . " ha sido eliminado.<br>";
    }
}
    
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

    echo "<a href='index.html'>Regresar</a>";
?>