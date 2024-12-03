CREATE TABLE proyecto (
	codProyecto INT NOT NULL,
	Nombre VARCHAR(20),
        Descripcion VARCHAR(50),
        Cliente VARCHAR(10),
        Presupuesto INT NOT NULL,
        numHoras INT,
        fechaInicio DATE,
        PRIMARY KEY (codProyecto));


CREATE TABLE fase (
	numFase INT NOT NULL,
	Nombre VARCHAR(20),
        Estado VARCHAR(10),
        fechaInicio DATE,
        fechaFIN DATE,
        Proyecto INT NOT NULL,
        PRIMARY KEY(numFase)
        FOREIGN KEY(Proyecto) REFERENCES proyecto (codProyecto));

CREATE TABLE Recurso (
	Codigo INT NOT NULL,
        Nombre VARCHAR(15),
        Descripcion VARCHAR(30),
        tipo VARCHAR(10),
        PRIMARY KEY (Codigo));

CREATE TABLE Recurso_fase (
	numFase INT NOT NULL,
	proyecto INT NOT NULL,
        codigoRecurso INT NOT NULL,
        periodo DATE,
        PRIMARY KEY(numFase, proyecto, codigo),
        FOREIGN KEY(numFase) REFERENCES fase (numFase),
        FOREIGN KEY(proyecto) REFERENCES fase (Proyecto),
        FOREIGN KEY(codigoRecurso) REFERENCES recurso (Codigo));

CREATE TABLE Empleado(
        Cedula INT NOT NULL,
        CodigoEmpleado INT,
        Nombre VARCHAR(20),
        Direccion VARCHAR(15),
        Titulacion VARCHAR(10),
        Años INT,
        tipo VARCHAR(11),
        PRIMARY KEY (Cedula),
        CHECK(tipo in("Analista","Programador")));

CREATE TABLE Programador(
        Cedula INT NOT NULL,
        PRIMARY KEY(Cedula),
        FOREIGN KEY(Cedula) REFERENCES Empleado (Cedula));

CREATE TABLE Proyecto_Empleado(
        CodProyecto INT NOT NULL,
        Cedula INT NOT NULL,
        numHoras INT,
        Costo INT,
        Jefe_proyecto VARCHAR(15),
        PRIMARY KEY(CodProyecto, Cedula),
        FOREIGN KEY(CodProyecto) REFERENCES Proyecto(CodProyecto),
        FOREIGN KEY(Cedula) REFERENCES Empleado(Cedula));

CREATE TABLE Producto(
        Codigo INT NOT NULL,
        Nombre VARCHAR (20),
        Descripcion VARCHAR(30),
        Estado VARCHAR(10),
        Analista VARCHAR(20),
        Fase INT,
        Proyecto INT,
        Tipo Varchar(15),
        CHECK(Tipo in("Inf.tecnica","Prototipos","Software")),
        PRIMARY KEY(Codigo),
        FOREIGN KEY(Analista) REFERENCES Empleado(Cedula),
        FOREIGN KEY(Fase) REFERENCES Fase(numFase),
        FOREIGN KEY(Proyecto) REFERENCES Fase(Proyecto));

CREATE TABLE Software(
        Codigo INT NOT NULL,
        Tipo VARCHAR(10),
        PRIMARY KEY(Codigo),
        FOREIGN KEY(Codigo) REFERENCES Producto(Codigo));

CREATE TABLE Prototipos(
        Codigo INT NOT NULL,
        Version INT,
        Ubicacion VARCHAR(10),
        PRIMARY KEY(Codigo),
        FOREIGN KEY(Codigo) REFERENCES Producto(Codigo));

CREATE TABLE Empleado_Fase_Producto(
        Cedula INT NOT NULL,
        numFase INT NOT NULL,
        Proyecto INT NOT NULL,
        Codigo INT NOT NULL,
        num_horas INT NOT NULL,
        PRIMARY KEY(Cedula, numFase, Codigo, Proyecto),
        FOREIGN KEY(Cedula) REFERENCES Empleado(Cedula),
        FOREIGN KEY(numFase) REFERENCES Fase(numFase),
        FOREIGN KEY(Proyecto) REFERENCES Fase(Proyecto),
        FOREIGN KEY(Codigo) REFERENCES Producto(Codigo));