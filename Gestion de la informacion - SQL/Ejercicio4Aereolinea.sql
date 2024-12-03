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

CREATE TABLE Vendedor(
        Cedula INT NOT NULL,
        AñosExperiencia INT,
        PRIMARY KEY(Cedula),
        FOREIGN KEY(Cedula) REFERENCES Persona(Cedula));

CREATE TABLE Ingeniero(
        Cedula INT NOT NULL,
        AñosExperiencia INT,
        Especialidad VARCHAR(10),
        PRIMARY KEY(Cedula),
        FOREIGN KEY(Cedula) REFERENCES Persona(Cedula));

CREATE TABLE Arquitecto(
        Cedula INT NOT NULL,
        Comisiones INT,
        PRIMARY KEY(Cedula),
        FOREIGN KEY(Cedula) REFERENCES Persona(Cedula));

CREATE TABLE Proyectos(
        IDproyecto INT NOT NULL,
        IDarquitecto INT,
        Tipo VARCHAR(10),
        PRIMARY KEY(IDproyecto, IDarquitecto),
        FOREIGN KEY(IDarquitecto) REFERENCES Arquitecto(Cedula));

CREATE TABLE Administrativo(
        Cedula INT NOT NULL,
        #Subornidados INT,
        Dependencia VARCHAR(10),
        NivelJerarquico VARCHAR(10),
        PRIMARY KEY(Cedula),
        FOREIGN KEY(Cedula) REFERENCES Persona(Cedula));

CREATE TABLE Proveedor(
        Cedula INT NOT NULL,
        Especialidad VARCHAR(10),
        PRIMARY KEY(Cedula),
        FOREIGN KEY(Cedula) REFERENCES Persona(Cedula));

CREATE TABLE PartesJuguetes(
        IDparteJuguete INT NOT NULL,
        CedulaProveedor INT NOT NULL,
        Tamaño INT,
        Material VARCHAR(10),
        TipoJuguete VARCHAR(10),
        PRIMARY KEY(IDparteJuguete, CedulaProveedor),
        FOREIGN KEY(CedulaProveedor) REFERENCES Proveedor(Cedula));

CREATE TABLE Administrativo_Proveedor(
        CCadministrativo INT NOT NULL,
        CCproovedor INT NOT NULL,
        PRIMARY KEY(CCadministrativo, CCproveedor),
        FOREIGN KEY(CCadministrativo) REFERENCES Administrativo(Cedula)),
        FOREIGN KEY(CCproovedor) REFERENCES Proveedor(Cedula));

CREATE TABLE Cliente(
        Cedula INT NOT NULL,
        FormaPago VARCHAR(10),
        Presupuesto INT,
        Tipo VARCHAR(10),
        CHECK(Tipo in("Infantil","Juvenil"),
        PRIMARY KEY(Cedula),
        FOREIGN KEY(Cedula) REFERENCES Persona(Cedula));

CREATE TABLE Juvenil(
        Cedula INT NOT NULL,
        TarjetaAfiliacion CHAR(10),
        CHECK(TarjetaAfiliacion in("Si","No"),
        PRIMARY KEY(Cedula),
        FOREIGN KEY(Cedula) REFERENCES Cliente(Cedula));

CREATE TABLE Tienda(
        IDtienda INT NOT NULL,
        Direccion VARCHAR(20),
        PRIMARY KEY(Cedula));

CREATE TABLE Vendedor_Tienda(
        CedulaVendedor INT NOT NULL,
        IDtienda INT NOT NULL,
        PRIMARY KEY(CedulaVendedor, IDtienda),
        FOREIGN KEY(CedulaVendedor) REFERENCES Vendedor(Cedula),
        FOREIGN KEY(IDtienda) REFERENCES Tienda(IDtienda));

CREATE TABLE Tienda_Cliente(
        IDtienda INT NOT NULL,
        CedulaCliente INT NOT NULL,
        PRIMARY KEY(IDtienda, CedulaCliente),
        FOREIGN KEY(IDtienda) REFERENCES Tienda(IDtienda),
        FOREIGN KEY(CedulaCliente) REFERENCES Cliente(Cedula));


CREATE TABLE Fabrica(
        IDfabrica INT NOT NULL,
        Ingeniero INT NOT NULL,
        Maquinas INT,
        Direccion VARCHAR(10),
        PRIMARY KEY(Cedula, Ingeniero),
        FOREIGN KEY(Ingeniero) REFERENCES Ingeniero(Cedula));

CREATE TABLE Tienda_Fabrica(
        IDtienda INT NOT NULL,
        IDfabrica INT NOT NULL,
        Ingeniero INT NOT NULL,
        PRIMARY KEY(IDtienda, IDfabrica, Ingeniero),
        FOREIGN KEY(IDtienda) REFERENCES Tienda(IDtienda),
        FOREIGN KEY(IDfabrica) REFERENCES Fabrica(IDfabrica),
        FOREIGN KEY(Ingeniero) REFERENCES Fabrica(Ingeniero));

CREATE TABLE Proveedor_Fabrica(
        Proveedor INT NOT NULL,
        IDfabrica INT NOT NULL,
        Ingeniero INT NOT NULL,
        PRIMARY KEY(Proveedor, IDfabrica, Ingeniero),
        FOREIGN KEY(Proveedor) REFERENCES Proveedor(Cedula),
        FOREIGN KEY(IDfabrica) REFERENCES Fabrica(IDfabrica),
        FOREIGN KEY(Ingeniero) REFERENCES Fabrica(Ingeniero));

CREATE TABLE Juguete(
        IDjuguete INT NOT NULL,
        Arquitecto INT NOT NULL,
        IDfabrica INT NOT NULL,
        Peso INT,
        Precio INT,
        PublicoObjetivo VARCHAR(10),
        PRIMARY KEY(Cedula, Arquitecto, IDfabrica),
        FOREIGN KEY(Arquitecto) REFERENCES Arquitecto(Cedula),
        FOREIGN KEY(IDfabrica) REFERENCES Fabrica(IDfabrica));

CREATE TABLE Mecanico(
        IDjuguete INT NOT NULL,
        DuracionBateria INT
        PRIMARY KEY(IDjuguete),
        FOREIGN KEY(IDjuguete) REFERENCES Juguete(IDjuguete));


CREATE TABLE Didactico(
        IDjuguete INT NOT NULL,
        AreaDidactica VARCHAR(15),
        PRIMARY KEY(IDjuguete),
        FOREIGN KEY(IDjuguete) REFERENCES Juguete(IDjuguete));


CREATE TABLE Digital(
        IDjuguete INT NOT NULL,
        Plataforma VARCHAR(20),
        PRIMARY KEY(IDjuguete),
        FOREIGN KEY(IDjuguete) REFERENCES Juguete(IDjuguete));


CREATE TABLE Juguete_Cliente(
        IDjuguete INT NOT NULL,
        CedulaCliente INT NOT NULL,
        PRIMARY KEY(IDjuguete, CedulaCliente),
        FOREIGN KEY(IDjuguete) REFERENCES Juguete(IDjuguete),
        FOREIGN KEY(CedulaCliente) REFERENCES Cliente(Cedula));