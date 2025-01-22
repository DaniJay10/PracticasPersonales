type Props = {
  data: string[];
};

function List({ data }: Props) {
  const handleClick = (e: string) => {
    console.log(e);
  };
  return (
    <>
      <ul className="list-group">
        {data.map((elemento) => (
          <li
            onClick={() => handleClick(elemento)}
            key={elemento}
            className="list-group-item"
          >
            {elemento}
          </li>
        ))}
      </ul>
    </>
  );
}

export default List;
