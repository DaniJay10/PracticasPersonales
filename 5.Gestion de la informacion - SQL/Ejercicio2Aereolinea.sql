CREATE TABLE Aereopuerto
(
       IATA INT NOT NULL,
       Nombre VARCHAR(10),
       Direccion VARCHAR(15),
       #Terminales INT,
       PRIMARY KEY (IATA)
);

CREATE TABLE Terminal
(
       IDterminal INT NOT NULL,
       Nombre VARCHAR(10),
       Politicas VARCHAR(50),
       RutasActivas VARCHAR(20),
       PRIMARY KEY (IDterminal)
);


CREATE TABLE Terminal_Aereopuerto
(
       IDterminal INT NOT NULL,
       IATAaereopuerto INT NOT NULL,
       PRIMARY KEY (IDterminal,IATAaereopuerto),
       FOREIGN KEY(IDterminal) REFERENCES Terminal(IDterminal),
       FOREIGN KEY(IATAareopuerto) REFERENCES Aereopuerto(IATA)
);

CREATE TABLE TorreControl
(
       IDtorre INT NOT NULL,
       IATAaereopuerto INT NOT NULL,
       PRIMARY KEY (IDtorre,IATAaereopuerto),
       FOREIGN KEY(IATAareopuerto) REFERENCES Aereopuerto(IATA)
);

CREATE TABLE Pista
(
       IDpista INT NOT NULL,
       Longitud INT,
       #Luces INT,
       PRIMARY KEY (IDpista)
);


CREATE TABLE TorreControl_Pista
(
       IDtorre INT NOT NULL,
       IDpista INT NOT NULL,
       IATAaereopuerto INT,
       PRIMARY KEY (IDtorre,IDpista,IATAaereopuerto),
       FOREIGN KEY(IDtorre) REFERENCES TorreControl(IDtorre),
       FOREIGN KEY(IATAaereopuerto) REFERENCES TorreControl(IATAaereopuerto),
       FOREIGN KEY(IDpista) REFERENCES Pista(IDpista)
);

CREATE TABLE Avion
(
       IDavion INT NOT NULL,
       Modelo VARCHAR(10),
       NumeroSerie INT,
       AltitudMaxima INT,
       VelocidadMaxima INT,
       PRIMARY KEY (IDavion)
);

CREATE TABLE AvionTradicional
(
       IDavion INT NOT NULL,
       #Asientos INT,
       TipoServicio VARCHAR(10),
       PRIMARY KEY (IDavion),
       FOREIGN KEY(IDavion) REFERENCES Avion(IDavion)
);

CREATE TABLE Avioneta
(
       IDavion INT NOT NULL,
       TipoUso VARCHAR(15),
       PRIMARY KEY (IDavion),
       FOREIGN KEY(IDavion) REFERENCES Avion(IDavion)
);

CREATE TABLE AvionPractica
(
       IDavion INT NOT NULL,
       Instructor VARCHAR(15),
       PRIMARY KEY (IDavion),
       FOREIGN KEY(IDavion) REFERENCES Avion(IDavion)
);

CREATE TABLE Helicoptero
(
       IDavion INT NOT NULL,
       PesoMaximo INT,
       PRIMARY KEY (IDavion),
       FOREIGN KEY(IDavion) REFERENCES Avion(IDavion)
);

CREATE TABLE Aereopuerto_Avion
(
       IATAaereopuerto INT NOT NULL,
       IDavion INT NOT NULL,
       PRIMARY KEY (IATAaereopuerto, IDavion),
       FOREIGN KEY(IATAaereopuerto) REFERENCES Aereopuerto(IATA),
       FOREIGN KEY(IDavion) REFERENCES Avion(IDavion)
);

CREATE TABLE Avion_Pista
(
       IDavion INT NOT NULL,
       IDpista INT NOT NULL,
       PRIMARY KEY (IDavion, IDpista),
       FOREIGN KEY(IDavion) REFERENCES Avion(IDavion),
       FOREIGN KEY(IDpista) REFERENCES Pista(IDpista)
);


CREATE TABLE Persona
(
       Cedula INT NOT NULL,
       Nombre VARCHAR(15),
       FechaNac DATE,
       Edad INT,
       Direccion VARCHAR(10),
       Genero CHAR(1),
       PRIMARY KEY(Cedula),
       CHECK(Genero in("F","M"))
);

CREATE TABLE Telefono
(
       Numero INT NOT NULL,
       CedulaPersona INT NOT NULL,
       PRIMARY KEY(Numero),
       FOREIGN KEY(CedulaPersona) REFERENCES Persona(Cedula)
);

CREATE TABLE Empleado
(
       Cedula INT NOT NULL,
       IATAaereopuerto INT NOT NULL,
       Salario INT NOT NULL,
       PRIMARY KEY(Cedula),
       FOREIGN KEY(Cedula) REFERENCES Persona(Cedula),
       FOREIGN KEY(IATAaereopuerto) REFERENCES Aereopuerto(IATA)
);

CREATE TABLE Piloto
(
       Cedula INT NOT NULL,
       IDavion INT NOT NULL,
       AñosExperiencia INT,
       TipoAvion VARCHAR(10),
       PRIMARY KEY(Cedula),
       FOREIGN KEY(Cedula) REFERENCES Empleado(Cedula)
)
,
        FOREIGN KEY
((IDavion) REFERENCES Avion
(IDavion));

CREATE TABLE Maletero
(
       Cedula INT NOT NULL,
       EquipoSeguridad VARCHAR(10),
       CondificionFisica VARCHAR(5),
       PRIMARY KEY(Cedula),
       FOREIGN KEY(Cedula) REFERENCES Empleado(Cedula),
       CHECK(EquipoSeguridad in("Recibido","NoRecibido")),
       CHECK(CondicionFisica in("Buena","Mala"))
);

CREATE TABLE Recepcionista
(
       Cedula INT NOT NULL,
       Cabina INT,
       Horario TIME,
       PRIMARY KEY(Cedula),
       FOREIGN KEY(Cedula) REFERENCES Empleado(Cedula)
);

CREATE TABLE Pasajero
(
       Cedula INT NOT NULL,
       CedulaRecepcionista INT NOT NULL,
       PRIMARY KEY(Cedula),
       FOREIGN KEY(Cedula) REFERENCES Persona (Cedula)
)
,
        FOREIGN KEY
(CedulaRecepcionista) REFERENCES Recepcionista
(Cedula));


CREATE TABLE CarroCargaEquipaje
(
       IDcarro INT NOT NULL,
       CedulaMaletero INT NOT NULL,
       PRIMARY KEY(IDcarro),
       FOREIGN KEY(CedulaMaletero) REFERENCES Maletero (Cedula)
);


CREATE TABLE Equipaje(
        IDequipaje CHAR(5) NOT NULL,
        CedulaPasajero INT NOT NULL,
        IDcarro INT NOT NULL,
        Peso INT,
        Tipo VARCHAR(10),
        PRIMARY
(IDequipaje),
        FOREIGN KEY
(CedulaPasajero) REFERENCES Pasajero
(Cedula),
        FOREIGN KEY
(IDcarro) REFERENCES CarroCargaEquipaje
(IDcarro));