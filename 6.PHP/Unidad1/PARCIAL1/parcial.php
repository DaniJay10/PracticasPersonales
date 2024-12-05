<?php
$RegistroJSON = "registro.json";
$metodo = intval($_POST["metodo"]);
$Personas = array();
class Usuario {
    public $nombre;
    public $apellido;
    public $edad;
    public $salario;
    public $user;
    public $clave;
    function __construct($nombre = null, $apellido = null, $edad = null, $salario = null, $user = null, $clave =null) {
        $this->nombre = $nombre;
        $this->apellido = $apellido;
        $this->edad = $edad;
        $this->salario = $salario;
        $this->user = $user;
        $this->clave = $clave;
    }
    function registrar($nombre, $apellido, $edad, $salario, $user, $clave){
    global $RegistroJSON;
    $Usuario=[
        "Nombre" => $nombre,
        "Apellido" => $apellido,
        "Edad" => $edad,
        "Salario" => $salario,
        "Usuario" => $user,
        "Clave" => $clave
    ];
    if (file_exists($RegistroJSON)) {
        $contenido = file_get_contents($RegistroJSON);
        $jsonArray = json_decode($contenido, true);
        // Si no existe la clave "Personas", inicializarla como un array vacío
        if (!isset($jsonArray["Personas"])) {
                $jsonArray["Personas"] = [];
            }
        } else {
            // Si el archivo no existe, creamos la estructura inicial con la clave "Personas"
            $jsonArray = ["Personas" => []];
        }
    $jsonArray["Personas"][] = $Usuario;
    file_put_contents($RegistroJSON, json_encode($jsonArray, JSON_PRETTY_PRINT));
    echo '<p style="color: green; font-weight: bold; background-color: #e0f7e0; padding: 10px; border-radius: 5px;">Usuario registrado correctamente</p>';
    }
    function ingresar($user, $clave) {
        global $RegistroJSON;
        $userFound = "n";
    
        if (file_exists($RegistroJSON)) {
            $contenido = file_get_contents($RegistroJSON);
            $jsonArray = json_decode($contenido, true);
            if (isset($jsonArray["Personas"])) {
                $personasArray = $jsonArray["Personas"];
                for ($i = 0; $i < count($personasArray); $i++) {
                    if ($personasArray[$i]['Usuario'] == $user && $personasArray[$i]['Clave'] == $clave) {
                        $userFound = "y";
                        break;
                    } elseif ($personasArray[$i]['Usuario'] == $user && $personasArray[$i]['Clave'] != $clave) {
                        $userFound = "m";
                    }
                }
            }
            if ($userFound == "y") {
                echo '<p style="color: green; font-weight: bold; background-color: #e0f7e0; padding: 10px; border-radius: 5px;">Bienvenido al sistema</p>';
            } elseif ($userFound == "n") {
                echo '<p style="color: red; font-weight: bold; background-color: #f7e0e0; padding: 10px; border-radius: 5px;">Usuario no registrado</p>';
            } elseif ($userFound == "m") {
                echo '<p style="color: red; font-weight: bold; background-color: #f7e0e0; padding: 10px; border-radius: 5px;">Clave incorrecta</p>';
            }
        }
    }    
}



//ejecucion
if($metodo == 1){
    $nom=$_POST["nombre"];
    $ap=$_POST["apellido"];
    $edad=intval($_POST["edad"]);
    $sal=intval($_POST["salario"]);
    $us=$_POST["user"];
    $clave=$_POST["clave"];
    //Creacion usuario y registro
    $Usuarios = new Usuario();
    echo $Usuarios->registrar($nom, $ap, $edad, $sal, $us, $clave);
}elseif($metodo == 2){
    $us=$_POST["user"];
    $clave=$_POST["clave"];
    $Usuarios = new Usuario();
    echo $Usuarios->ingresar($us, $clave);
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