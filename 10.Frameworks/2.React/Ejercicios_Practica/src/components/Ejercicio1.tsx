import { ReactNode } from "react";

type Props = {
  children: ReactNode;
  onClick: () => void;
  Estado: boolean;
};

const Ejercicio1 = ({ children, onClick, Estado }: Props) => {
  return (
    <>
      <button
        onClick={onClick}
        type="button"
        className={`btn btn-${Estado === true ? "dark" : "light"}`}
      >
        {Estado ? "OcultarTexto" : children}
      </button>
    </>
  );
};

export default Ejercicio1;
