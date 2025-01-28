import Ejercicio1 from "./components/Ejercicio1";
import { useState } from "react";
import Card from "./components/Card";

const App = () => {
  //Ejercicio1
  const [Estado, setEstado] = useState(false);
  const handleClick = () => {
    setEstado(!Estado);
  };
  //Ejercicio2
  let textN = "";
  return (
    <>
      <Card Estado={Estado}>textN</Card>
      <Ejercicio1 onClick={handleClick} Estado={Estado}>
        MostrarTexto
      </Ejercicio1>
    </>
  );
};

export default App;
