import Card from "./components/Card";
import CardBody from "./components/CardBody";
import List from "./components/List";

function App() {
  const list: string[] = [];
  const handleSelect = (elemento: string) => {
    console.log("imprimiendo", elemento);
  };
  const handleSelect2 = (elemento: string) => {
    console.log("mostrando", elemento);
  };
  return (
    <>
      <Card>
        {list.length !== 0 && "La lista es:"}
        <CardBody title="Esto es el título" text="Este es el texto" />
      </Card>
      <List data={list} onSelect={handleSelect} />
      <List data={list} onSelect={handleSelect2} />
    </>
  );
}
export default App;
