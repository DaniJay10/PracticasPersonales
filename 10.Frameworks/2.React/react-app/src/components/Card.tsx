import { ReactNode } from "react";
interface Props {
  children: ReactNode;
}
function Card(props: Props) {
  const { children } = props;
  return (
    <div className="card" style={{ width: "350px" }}>
      <div className="card-body">{children}</div>
    </div>
  );
}

export default Card;
