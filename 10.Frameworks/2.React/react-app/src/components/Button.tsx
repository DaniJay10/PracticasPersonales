import { ReactNode } from "react";

type Props = {
  children: ReactNode; // Texto del botón
  onClick: () => void; // Función a ejecutar al hacer clic
  isLoading: boolean; // Estado que indica si está cargando
};

const Button = ({ children, onClick, isLoading }: Props) => {
  return (
    <button
      onClick={onClick}
      type="button"
      className={`btn btn-${isLoading ? "secondary" : "primary"}`}
    >
      {isLoading ? "Cargando..." : children}
    </button>
  );
};

export default Button;
