import { ReactNode } from "react";

type Props = {
  children: ReactNode;
  Estado: boolean;
};

const Card = ({ children, Estado }: Props) => {
  let text =
    "Some quick example text to build on the card title and make up the bulk of the card's content.";
  return (
    <>
      <div className="card">
        <div className="card-body">
          <h5 className="card-title">Card title</h5>
          <p className="card-text">{Estado ? text : ""}</p>
        </div>
      </div>
    </>
  );
};

export default Card;
