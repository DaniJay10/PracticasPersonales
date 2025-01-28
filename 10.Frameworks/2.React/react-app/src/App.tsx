import Card from "./components/Card";
import CardBody from "./components/CardBody";
import List from "./components/List";
import Button from "./components/Button";
import { useState } from "react";
function App() {
  const list: string[] = [];
  const handleSelect = (elemento: string) => {
    console.log("imprimiendo", elemento);
  };
  //metodo 1 de rendereizado condicional
  const cont =
    list.length !== 0 ? (
      <List data={list} onSelect={handleSelect} />
    ) : (
      "Sin elementos para mostrar"
    );
  //metodo 2 de rendereizado condicional
  const cont2 = list.length !== 0 && (
    <List data={list} onSelect={handleSelect} />
  );


  
  const [isLoading, setIsLoading] = useState(false);
  const handleClick = () => {
    setIsLoading(true);
  };
  return (
    <>
      <Card>
        <CardBody title="Esto es el título" text="Este es el texto" />
        {cont}
      </Card>
      <Button onClick={handleClick} isLoading={isLoading}>
        Hola Mundo
      </Button>
    </>
  );
}
export default App;
