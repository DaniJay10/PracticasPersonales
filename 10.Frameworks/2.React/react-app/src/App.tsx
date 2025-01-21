import Card from "./components/Card";
import CardBody from "./components/CardBody";
import List from "./components/List";

function App() {
  const list = ["Messi", "Iniesta", "Xavi"];
  return (
    <>
      <Card>
        <CardBody title="Este es el titulo" text="este es el texto" />
      </Card>
      <List data={list} />
    </>
  );
}
export default App;
