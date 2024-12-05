<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aplicación Hospital</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
<?php
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
        $host = "localhost"; 
        $user = "root"; 
        $pass = "spike10"; 
        $db = "Hospital"; 
        $conn = new mysqli($host, $user, $pass, $db);
        if($conn->connect_error){
            die("Conexión fallida: ". $conn->connect_error);
        }
        $Insql = "INSERT INTO Paciente VALUES ($cedula, '$nombre', '$fecha_nacimiento', '$genero')";

        $query = mysqli_query($conn, $Insql);

        if($query){
            echo '<div class="alert alert-success">El paciente se ha registrado en MariaDB</div>';
        }else{
            echo '<div class="alert alert-danger" role="alert">El paciente no se ha podido registrar en MariaDB</div>';
        }
        $conn->close();
    }

   //metodo buscar y ver datos paciente
   function Buscar($cedula){
        $host = "localhost"; 
        $user = "root"; 
        $pass = "spike10"; 
        $db = "Hospital"; 
        $conn = new mysqli($host, $user, $pass, $db);
        if($conn->connect_error){
            die("Conexión fallida: ". $conn->connect_error);
        }
        $ConSQL = "SELECT * FROM Paciente WHERE cedula = '$cedula'";
        $query = mysqli_query($conn, $ConSQL);
        if ($query->num_rows > 0) {
            $paciente = $query->fetch_assoc(); 
            echo "
            <div class='container'>
                <div class='card'>
                    <div class='card-body'>
                        <h3 class='text-center text-success'>Información del Paciente</h3>
                        <table class='table table-striped'>
                            <tr>
                                <td><strong>Cédula:</strong></td>
                                <td>" . $paciente['cedula'] . "</td>
                            </tr>
                            <tr>
                                <td><strong>Nombre:</strong></td>
                                <td>" . $paciente['nombre'] . "</td>
                            </tr>
                            <tr>
                                <td><strong>Fecha de Nacimiento:</strong></td>
                                <td>" . $paciente['fechaNac'] . "</td>
                            </tr>
                            <tr>
                                <td><strong>Género:</strong></td>
                                <td>" . $paciente['genero'] . "</td>
                            </tr>
                        </table>
                    </div>
                </div>
            </div>";
        } else {
            echo '<div class="alert alert-danger" role="alert">No se encontró paciente con cédula ' . $cedula . ' en la base de datos.</div>';
        }
    
        $conn->close();
   }

    //metodo de actualizar datos
    function editar($cedula, $cedulaN, $nombre, $fecha_nacimiento, $genero){
        $host = "localhost"; 
        $user = "root"; 
        $pass = "spike10"; 
        $db = "Hospital"; 
        $conn = new mysqli($host, $user, $pass, $db);
        if($conn->connect_error){
            die("Conexión fallida: ". $conn->connect_error);
        }
        $ConSQL = "SELECT * FROM Paciente WHERE cedula = '$cedula'";
        $query = mysqli_query($conn, $ConSQL);
    if($query->num_rows > 0){
        $datoPaciente = $query->fetch_assoc(); 
        $nombrePaciente = $datoPaciente['nombre'];
        $datosActualizados = [];
        if(!empty($cedulaN)) {
            $datosActualizados[] = "cedula = $cedulaN";
        }
        if(!empty($nombre)) {
            $datosActualizados[] = "nombre = '$nombre'";
        }
        if(!empty($fecha_nacimiento)) {
            $datosActualizados[] = "fechaNac = '$fecha_nacimiento'";
        }
        if(!empty($genero)) {
            $datosActualizados[] = "genero = '$genero'";
        }
        if(!empty($datosActualizados)) {
            $updateSQL = "UPDATE Paciente SET " . implode(", ", $datosActualizados) . " WHERE cedula = '$cedula'";
            if(mysqli_query($conn, $updateSQL)) {
               echo '<div class="alert alert-success">Los datos de ' . $nombrePaciente . ' han sido actualizados correctamente en MariaDB.</div>';
            }else {
                rojo: echo '<div class="alert alert-danger" role="alert">Error al actualizar: ' . $conn->error . '</div>';
            }

        }else {
            echo '<div class="alert alert-warning" role="alert">No se realizaron cambios en los datos.</div>';
        }

    }else{
        echo '<div class="alert alert-danger" role="alert">No se encontró paciente con cédula ' . $cedula . ' en la base de datos.</div>';
    }
        $conn->close();
}



       //metodo de calcular edad
    function calcularEdad($cedula, $anioActual){
        $host = "localhost"; 
        $user = "root"; 
        $pass = "spike10"; 
        $db = "Hospital"; 
        $conn = new mysqli($host, $user, $pass, $db);
        if($conn->connect_error){
            die("Conexión fallida: ". $conn->connect_error);
        }
        $ConSQL = "SELECT * FROM Paciente WHERE cedula = '$cedula'";
        $query = mysqli_query($conn, $ConSQL);
        if($query->num_rows > 0){
            $Insql = "SELECT fechaNac,nombre FROM Paciente WHERE cedula = '$cedula'";
            $query = mysqli_query($conn, $Insql);
            $dato = $query->fetch_assoc();
            $fechaNacimiento = new DateTime($dato['fechaNac']);
            $fechaActual = new DateTime($anioActual);
            $edad = $fechaActual->diff($fechaNacimiento)->y;
            echo '<div class="alert alert-success">La edad de ' . $dato['nombre'] . ' es: ' . $edad . ' años</div>';
        }else{
            echo '<div class="alert alert-danger" role="alert">No se encontró paciente con cédula ' . $cedula . ' en la base de datos.</div>';
        }
        $conn->close();
    }
    


   //metodo eliminar paciente
   function Eliminar($cedula){
        $host = "localhost"; 
        $user = "root"; 
        $pass = "spike10"; 
        $db = "Hospital"; 
        $conn = new mysqli($host, $user, $pass, $db);
        if($conn->connect_error){
            die("Conexión fallida: ". $conn->connect_error);
        }
        $ConSQL = "SELECT * FROM Paciente WHERE cedula = '$cedula'";
        $query = mysqli_query($conn, $ConSQL);
        if($query->num_rows > 0){
        $Insql = "DELETE FROM Paciente WHERE cedula = '$cedula'";
        $query = mysqli_query($conn, $Insql);
        if($query) {
          echo '<div class="alert alert-success">El paciente con cédula ' . $cedula . ' se ha eliminado correctamente en MariaDB.</div>';
        } else {
            echo '<div class="alert alert-danger" role="alert">Error al eliminar el paciente con cédula ' . $cedula . ': ' . $conn->error . '</div>';
        }
        }else{
            echo '<div class="alert alert-danger" role="alert">No se encontró paciente con cédula ' . $cedula . ' en la base de datos.</div>';
        }
        $conn->close();
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
        if($ced != null && $nom != null && $FeNac != null && $gen != null){
            if($gen == "M" || $gen == "F"){
                $Pacientes = new Paciente();
                echo $Pacientes->crear($ced, $nom, $FeNac, $gen);    
            }else{
                echo '<div class="alert alert-warning" role="alert">Dato del GENERO no valido (Ingrese "F" para Femenino y "M" para Masculino).</div>';
                echo '<div class="alert alert-danger" role="alert">El paciente no se ha podido registrar en MariaDB</div>';
        }
        }else{
            echo '<div class="alert alert-danger" role="alert">¡¡¡Error!!! Por favor complete todos los campos</div>';
        }

    }  
    
    elseif($metodo == 2){
        $ced=intval($_POST["ceCon"]);
        //ejecucion
        $Pacientes = new Paciente();
        echo $Pacientes->Buscar($ced);
    } 

    elseif ($metodo == 3){
        //atributos recolectados
        $ced=intval($_POST["cedula"]);
        $cedN=intval($_POST["cedulaNueva"]);
        $nom=$_POST["nombre"];
        $FeNac=$_POST["fechaNac"];
        $gen=$_POST["genero"];
        //ejecucion        
        if($gen == "M" || $gen == "F" || $gen == null){
            $Pacientes = new Paciente();
            echo $Pacientes->editar($ced, $cedN, $nom, $FeNac, $gen);
        }else{
            echo '<div class="alert alert-warning" role="alert">Dato del GENERO no valido (Ingrese "F" para Femenino y "M" para Masculino).</div>';
            echo '<div class="alert alert-danger" role="alert">El paciente no se ha podido registrar en MariaDB</div>';
        }
    }


    elseif($metodo == 4){
        $ced=intval($_POST["cedula"]);
        $feAct=$_POST["fechaActual"];
        //ejecucion
        $Pacientes = new Paciente();
        echo $Pacientes->calcularEdad($ced, $feAct);
    }


    elseif($metodo == 5){
        $ced=intval($_POST["cedulaBorrar"]);
        //ejecucion
        $Pacientes = new Paciente();
        echo $Pacientes->Eliminar($ced);
    } 
    

    else {
        echo '<p>¡¡¡ERROR!!! Hubo algun error en procesos internos</p>';
    }

    echo "<a href='index.html' class='btn btn-success btn-block mt-4'>Regresar</a>";
?>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>

