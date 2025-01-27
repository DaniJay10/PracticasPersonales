import Card from "./components/Card";
import CardBody from "./components/CardBody";
import List from "./components/List";

function App() {
  const list: string[] = ["messi"];
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
  return (
    <>
      <Card>
        <CardBody title="Esto es el título" text="Este es el texto" />
        {cont}
        {cont2}
      </Card>
    </>
  );
}
export default App;
