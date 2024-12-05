CREATE DATABASE Hospital;
USE Hospital;

CREATE TABLE Paciente (
    cedula INT NOT NULL,
    nombre VARCHAR(100),
    fechaNac DATE,
    genero CHAR(1),
    PRIMARY KEY(cedula),
    CHECK(genero in("F","M")));

INSERT INTO Paciente (cedula, nombre, fechaNac, genero) VALUES
(1005296913, "Daniel Pinzon Jay", "2003-08-16", "M"),
(987654321, "Yeimy Corzo", "2004-10-06", "F"),
(456789123, "Yuliana Garces", "2004-06-18", "M"),
(321654987, "Juan Isabella", "2004-07-23", "F"),
(741852963, "José Torres", "1992-09-10", "M"),
(159753486, "Laura Castro", "1995-11-22", "F"),
(852963741, "Fernando Ruiz", "1983-01-30", "M"),
(963852741, "Luisa Martínez", "1991-04-18", "F"),
(753159846, "Pedro Ramírez", "1982-06-14", "M"),
(854321789, "Sofía Vargas", "1993-08-29", "F"),
(789456123, "Miguel Herrera", "1986-10-07", "M"),
(321789654, "Paula Rojas", "1987-02-17", "F"),
(258147369, "Andrés Medina", "1984-11-03", "M"),
(369258147, "Carolina Fernández", "1996-12-12", "F"),
(147852369, "Esteban Jiménez", "1994-09-23", "M"),
(951753258, "Gabriela Salazar", "1989-05-28", "F"),
(852741963, "Rodrigo Pineda", "1979-07-30", "M"),
(753486159, "Valeria Morales", "1997-08-19", "F"),
(456123789, "Daniela Ortega", "1985-03-15", "F"),
(789321456, "Héctor Castillo", "1980-12-02", "M");
