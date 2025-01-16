function ListGroup() {
  const items = ["Suiza", "Noruega", "Suecia", "Dinamarca"];
  const Message = items.length === 0 ? <p>Not item found</p> : null
  return (
    <div>
        <h1>List</h1>
        {Message}
        <ul className="list-group">
        {items.map(item => <li key={item} >{item}</li>)}
        </ul>
    </div>
  );
}

export default ListGroup;
