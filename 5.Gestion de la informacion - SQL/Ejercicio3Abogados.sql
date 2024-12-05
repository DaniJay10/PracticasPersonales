CREATE TABLE TribunalApelaciones(
        NIT INT NOT NULL,
        PRIMARY KEY(NIT);


CREATE TABLE Persona(
        Cedula INT NOT NULL,
        Nombre VARCHAR(15),
        FechaNac DATE,
        Edad INT,
        Direccion VARCHAR(10),
        Genero CHAR(1),
        PRIMARY KEY(Cedula),
        CHECK(Genero in("F","M")));

CREATE TABLE Telefono(
        Numero INT NOT NULL,
        CedulaPersona INT NOT NULL,
        PRIMARY KEY(Numero),
        FOREIGN KEY(CedulaPersona) REFERENCES Persona(Cedula));

CREATE TABLE Abogado(
        Cedula INT NOT NULL,
        IDveredicto INT NOT NULL,
        Honarios INT,
        CasosGanados INT,
        AñosExperiencia INT,
        Maestria VARCHAR(10),
        PRIMARY KEY(Cedula, IDveredicto),
        FOREIGN KEY(IDveredicto) REFERENCES Veredicto(IDveredicto)),
        FOREIGN KEY(Cedula) REFERENCES Persona(Cedula));


CREATE TABLE Fiscal(
        Cedula INT NOT NULL,
        TestimonioAcusatorio VARCHAR(50),
        PRIMARY KEY(Cedula),
        FOREIGN KEY(Cedula) REFERENCES Abogado(Cedula));

CREATE TABLE Defensor(
        Cedula INT NOT NULL,
        TribunalApelaciones INT,
        TestimonioDefensa VARCHAR(50),
        PRIMARY KEY(Cedula, TribunalApelaciones),
        FOREIGN KEY(Cedula) REFERENCES Abogado(Cedula),
        FOREIGN KEY(TribunalApelaciones) REFERENCES TribunalApelaciones(NIT));

CREATE TABLE Acusado(
        Cedula INT NOT NULL,
        TestimonioPropio VARCHAR(50),
        AbogadoDefensor VARCHAR(15),
        PRIMARY KEY(Cedula, AbogadoDefensor),
        FOREIGN KEY(AbogadoDefensor) REFERENCES Defensor(Cedula));

CREATE TABLE Acusador(
        Cedula INT NOT NULL,
        MotivoDemanda VARCHAR(25),
        AbogadoFiscal VARCHAR(15),
        PRIMARY KEY(Cedula, AbogadoFiscal),
        FOREIGN KEY(AbogadoFiscal) REFERENCES Fiscal(Cedula));


CREATE TABLE Testigo(
        Cedula INT NOT NULL,
        RelacionVictima VARCHAR(10),
        RelacionVictimario VARCHAR(10),
        PRIMARY KEY(Cedula),
        FOREIGN KEY(Cedula) REFERENCES Persona(Cedula));

CREATE TABLE Testimonio(
        #Testimonio INT NOT NULL,
        CedulaTestigo INT NOT NULL,
        TipoTestimonio VARCHAR(10),
        PRIMARY KEY(#Testimonio, CedulaTestigo),
        FOREIGN KEY(CedulaTestigo) REFERENCES Testigo(Cedula));

CREATE TABLE Juez(
        Cedula INT NOT NULL,
        AñosExperiencia INT,
        Especializacion VARCHAR(10),
        PRIMARY KEY(Cedula),
        FOREIGN KEY(Cedula) REFERENCES Persona(Cedula));

CREATE TABLE Veredicto(
        IDveredicto INT NOT NULL,
        CedulaJuez INT NOT NULL,
        Evidencia VARCHAR(50),
        Conclusion VARCHAR(30),
        Tipo VARCHAR(10),
        PRIMARY KEY(Cedula, CedulaJuez),
        FOREIGN KEY(CedulaJuez) REFERENCES Juez(Cedula),
        CHECK Tipo(in("Inocente","Culpable")));

CREATE TABLE Inocente(
        IDveredicto INT NOT NULL,
        Absolucion VARCHAR(30),
        Indemnizacion INT,
        PRIMARY KEY(IDveredicto),
        FOREIGN KEY(IDveredicto) REFERENCES Veredicto(IDveredicto));

CREATE TABLE Condena(
        IDcondena INT NOT NULL,
        IDveredictoCulpable INT NOT NULL,
        FechaInicio DATE,
        FechaFin DATE,
        PRIMARY KEY(IDcondena, IDveredictoCulpable),
        FOREIGN KEY(IDveredictoCulpable) REFERENCES Veredicto(IDveredicto));

CREATE TABLE Economica(
        IDcondena INT NOT NULL,
        ValorAPagar INT,
        PRIMARY KEY(IDcondena),
        FOREIGN KEY(IDcondena) REFERENCES Condena(IDcondena));

CREATE TABLE Intramural(
        IDcondena INT NOT NULL,
        CentroReclusion VARCHAR(10),
        PRIMARY KEY(IDcondena),
        FOREIGN KEY(IDcondena) REFERENCES Condena(IDcondena));

CREATE TABLE Domiciliaria(
        IDcondena INT NOT NULL,
        TipoMonitoreo VARCHAR(10),
        Supervisor VARCHAR(10),
        PRIMARY KEY(IDcondena),
        FOREIGN KEY(IDcondena) REFERENCES Condena(IDcondena));

CREATE TABLE TrabajoComunitario(
        IDcondena INT NOT NULL,
        CantidadHoras INT
        PRIMARY KEY(IDcondena),
        FOREIGN KEY(IDcondena) REFERENCES Condena(IDcondena));

CREATE TABLE LibertadCondicional(
        IDcondena INT NOT NULL,
        Supervision VARCHAR(10),
        Condiciones VARCHAR(20),
        PRIMARY KEY(IDcondena),
        FOREIGN KEY(IDcondena) REFERENCES Condena(IDcondena));
