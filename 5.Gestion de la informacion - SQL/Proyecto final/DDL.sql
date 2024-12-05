CREATE TABLE persona (
    cedula INT NOT NULL,
    nombre VARCHAR(100),
    fechaNac DATE,
    edad INT,
    direccion VARCHAR(100),
    genero CHAR(1),
    PRIMARY KEY(cedula),
    CHECK(genero in("F","M")));


CREATE TABLE telefono ( 
    numero INT NOT NULL,
    cedulaPersona INT NOT NULL,
    PRIMARY KEY(numero),
    FOREIGN KEY(cedulaPersona) REFERENCES persona(cedula));


CREATE TABLE empleado (
    cedula INT NOT NULL,
    salario INT,
    añosExperiencia INT,
    PRIMARY KEY(cedula),
    FOREIGN KEY (cedula) REFERENCES persona(cedula));
  

CREATE TABLE puntoVenta (
    IDtienda INT NOT NULL,
    direccion VARCHAR(50),
    PRIMARY KEY(IDtienda));


CREATE TABLE vendedor (
    cedula INT NOT NULL,
    HoraEntrada TIME,
    HoraSalida TIME,
    tienda INT,
    PRIMARY KEY(cedula),
    FOREIGN KEY (cedula) REFERENCES Empleado(cedula),
    FOREIGN KEY(tienda) REFERENCES puntoVenta(IDtienda)); 


CREATE TABLE cliente (
    cedula INT NOT NULL,
    clasificacion VARCHAR(30),
    PRIMARY KEY(cedula),
    FOREIGN KEY (cedula) REFERENCES persona(cedula),
    CHECK(clasificacion in("Minorista", "Mayorista"))); 



CREATE TABLE compra (
    IDfactura INT NOT NULL, 
    productos INT, 
    valor INT,
    cedula_cliente INT NOT NULL, 
    IDtienda INT NOT NULL,
    PRIMARY KEY(IDfactura, cedula_cliente, IDtienda), 
    FOREIGN KEY(cedula_cliente) REFERENCES cliente(Cedula),
    FOREIGN KEY(IDtienda) REFERENCES puntoVenta(IDtienda));


CREATE TABLE transportador ( 
    cedula INT NOT NULL,
    licencia INT, 
    PRIMARY KEY(cedula),
    FOREIGN KEY (cedula) REFERENCES Empleado(cedula));


CREATE TABLE transportador_tienda (
    cedula_transportador INT NOT NULL,
    IDtienda INT NOT NULL, 
    PRIMARY KEY(cedula_transportador, IDtienda),
    FOREIGN KEY(cedula_transportador) REFERENCES transportador(cedula),
    FOREIGN KEY(IDtienda) REFERENCES puntoVenta(IDtienda));


CREATE TABLE CamionCarga (
    matricula INT NOT NULL, 
    marca VARCHAR(20),
    modelo VARCHAR(20),
    PRIMARY KEY(matricula)); 


CREATE TABLE transportador_camion (
    cedula_transportador INT NOT NULL, 
    matricula INT NOT NULL, 
    PRIMARY KEY(cedula_transportador, matricula), 
    FOREIGN KEY(cedula_transportador) REFERENCES transportador (cedula),
    FOREIGN KEY(matricula) REFERENCES CamionCarga (matricula));


CREATE TABLE finca (
    IDfinca INT NOT NULL, 
    nombre VARCHAR(25), 
    direccion VARCHAR(100), 
    PRIMARY KEY(IDfinca)); 


CREATE TABLE alimento (
    IDalimento INT NOT NULL,
    fechaProduccion VARCHAR(20),
    fechaVencimiento VARCHAR(20), 
    certificacion VARCHAR(30) CHECK (certificacion IN ('Orgánico', 'OMG')),
    PRIMARY KEY (IDalimento));

CREATE TABLE carne (
    IDalimento INT NOT NULL, 
    peso INT, 
    corte VARCHAR(20),
    raza VARCHAR(20),
    valorXlibra INT,
    tipo VARCHAR(20) CHECK (tipo IN ('Res', 'Cerdo', 'Pescado', 'Gallina')),
    PRIMARY KEY(IDalimento), 
    FOREIGN KEY(IDalimento) REFERENCES alimento(IDalimento)); 


CREATE TABLE cartonHuevo (
    IDalimento INT NOT NULL,
    clasificacion VARCHAR(28) CHECK (clasificacion IN ('B', 'A', 'AA', 'AAA')),
    unidades INT, 
    tipoHuevo VARCHAR(15) CHECK (tipoHuevo IN ('Tradicional', 'Criollo')),
    ValorCarton INT,
    PRIMARY KEY(IDalimento), 
    FOREIGN KEY(IDalimento) REFERENCES alimento(IDalimento)
);



CREATE TABLE cultivo (
    IDalimento INT NOT NULL, 
    nombre VARCHAR(20),
    valorXlibra INT,
    tipo VARCHAR(28), 
    PRIMARY KEY(IDalimento), 
    FOREIGN KEY(IDalimento) REFERENCES alimento(IDalimento));


CREATE TABLE finca_alimento (
    IDfinca INT NOT NULL,
    IDalimento INT NOT NULL, 
    PRIMARY KEY(IDfinca, IDalimento), 
    FOREIGN KEY(IDfinca) REFERENCES finca(IDfinca),
    FOREIGN KEY (IDalimento) REFERENCES alimento(IDalimento)); 


CREATE TABLE loteProduccion (
    IDlote INT NOT NULL, 
    estado VARCHAR(20),
    camionCarga INT NOT NULL,
    puntoVenta INT NOT NULL,
    PRIMARY KEY(IDlote), 
    FOREIGN KEY(camionCarga) REFERENCES camionCarga(matricula),
    FOREIGN KEY(puntoVenta) REFERENCES puntoVenta(IDtienda)); 


CREATE TABLE lote_alimento (
    IDlote INT NOT NULL,
    IDalimento INT NOT NULL, 
    PRIMARY KEY(IDlote, IDalimento),
    FOREIGN KEY(IDlote) REFERENCES loteProduccion(IDlote),
    FOREIGN KEY(IDalimento) REFERENCES alimento(IDalimento));


CREATE TABLE establo (
    IDestablo INT NOT NULL, 
    tipo VARCHAR(25),
    tamaño INT, 
    IDfinca INT NOT NULL, 
    PRIMARY KEY(IDestablo),
    FOREIGN KEY(IDfinca) REFERENCES finca(IDfinca));


CREATE TABLE animal (
    IDanimal INT NOT NULL, 
    peso INT,
    raza VARCHAR(20),
    sexo VARCHAR(5),
    estadoSalud VARCHAR(25),
    edad INT, 
    etapaDesarrollo VARCHAR(28),
    establo INT,
    tipo VARCHAR (28) CHECK (tipo IN ('Vaca', 'Cerdo', 'Pescado', 'Gallina')), 
    CHECK(sexo in("F","M")),
    PRIMARY KEY(IDanimal), 
    FOREIGN KEY(establo) REFERENCES establo(IDestablo));



CREATE TABLE trabajadorFinca( 
    cedula INT NOT NULL, 
    Labor VARCHAR(28), 
    mayordomo INT, 
    finca INT, 
    PRIMARY KEY(cedula), 
    FOREIGN KEY (cedula) REFERENCES Empleado(Cedula),
    FOREIGN KEY (mayordomo) REFERENCES trabajadorFinca(cedula),
    FOREIGN KEY (finca) REFERENCES finca(IDfinca));

--vista1
CREATE VIEW Finca_Mayordomo_Trabajadores AS
SELECT 
    f.nombre AS Finca, p.nombre AS Mayordomo,
    (
        SELECT GROUP_CONCAT(p.nombre)
        FROM trabajadorFinca tf2
        JOIN Persona p ON tf2.Cedula = p.Cedula
        WHERE tf2.finca = tf.finca AND tf2.mayordomo IS NOT NULL
    ) AS Trabajadores
FROM trabajadorFinca tf
JOIN Persona p ON tf.Cedula = p.Cedula
JOIN finca f ON tf.finca = f.IDfinca
WHERE tf.mayordomo IS NULL
ORDER BY f.IDfinca;

--vista2
CREATE VIEW ProductoPorTienda AS
SELECT lp.puntoVenta AS Tienda, pv.direccion AS DireccionTienda,
    CASE
        WHEN a.IDalimento IN (SELECT IDalimento FROM carne) THEN c.tipo
        WHEN a.IDalimento IN (SELECT IDalimento FROM cartonHuevo) THEN "Carton Huevo"
        WHEN a.IDalimento IN (SELECT IDalimento FROM cultivo cu) THEN cu.tipo
        ELSE "Desconocido"
    END AS TipoProducto,
    a.fechaProduccion AS FechaProduccion, a.fechaVencimiento AS FechaVencimiento
FROM loteProduccion lp
JOIN puntoVenta pv ON lp.puntoVenta = pv.IDtienda
JOIN lote_alimento la ON lp.IDlote = la.IDlote
JOIN alimento a ON la.IDalimento = a.IDalimento
LEFT JOIN carne c ON a.IDalimento = c.IDalimento
LEFT JOIN cultivo cu ON a.IDalimento = cu.IDalimento;
--triggers
--persona
DELIMITER //
CREATE TRIGGER Insertar_Persona
AFTER INSERT ON proyecto.Persona
FOR EACH ROW
BEGIN
INSERT INTO AuditoriaProyecto.auditoriaPersona (fecha, IDobjeto, Tabla, Usuario, Operacion)
VALUES (NOW(), NEW.cedula,"Persona", USER(), "INSERT");
END;
//

DELIMITER // 
CREATE TRIGGER Actualizar_Persona
AFTER UPDATE ON proyecto.Persona
FOR EACH ROW
BEGIN
INSERT INTO AuditoriaProyecto.auditoriaPersona (fecha, IDobjeto, Tabla, Usuario, Operacion)
VALUES (NOW(), NEW.cedula, "Persona", USER(), "UPDATE");
END;
//

DELIMITER //
CREATE TRIGGER Borrar_Persona
AFTER DELETE ON proyecto.Persona
FOR EACH ROW
BEGIN
INSERT INTO AuditoriaProyecto.auditoriaPersona (fecha, IDobjeto, Tabla, Usuario, Operacion)
VALUES (NOW(), OLD.cedula, "Persona", USER(), "DELETE");
END;
//

--empleado
DELIMITER //
CREATE TRIGGER Insertar_Empleado 
AFTER INSERT ON proyecto.Empleado 
FOR EACH ROW
BEGIN
INSERT INTO AuditoriaProyecto.auditoriaEmpleado  (fecha, IDobjeto, Tabla, Usuario, Operacion)
VALUES (NOW(), NEW.cedula,"Empleado", USER(), "INSERT");
END;
//
DELIMITER // 
CREATE TRIGGER Actualizar_Empleado 
AFTER UPDATE ON proyecto.Empleado 
FOR EACH ROW
BEGIN
INSERT INTO AuditoriaProyecto.auditoriaEmpleado  (fecha, IDobjeto, Tabla, Usuario, Operacion)
VALUES (NOW(), NEW.cedula, "Empleado", USER(), "UPDATE");
END;
//
DELIMITER //
CREATE TRIGGER Borrar_Empleado
AFTER DELETE ON proyecto.Empleado 
FOR EACH ROW
BEGIN
INSERT INTO AuditoriaProyecto.auditoriaEmpleado  (fecha, IDobjeto, Tabla, Usuario, Operacion)
VALUES (NOW(), OLD.cedula, "Empleado", USER(), "DELETE");
END;
//


--Cliente 
DELIMITER //
CREATE TRIGGER Insertar_Cliente 
AFTER INSERT ON proyecto.Cliente  
FOR EACH ROW
BEGIN
INSERT INTO AuditoriaProyecto.auditoriaCliente (fecha, IDobjeto, Tabla, Usuario, Operacion)
VALUES (NOW(), NEW.cedula,"Cliente", USER(), "INSERT");
END;
//

DELIMITER // 
CREATE TRIGGER Actualizar_Cliente 
AFTER UPDATE ON proyecto.Cliente  
FOR EACH ROW
BEGIN
INSERT INTO AuditoriaProyecto.auditoriaCliente   (fecha, IDobjeto, Tabla, Usuario, Operacion)
VALUES (NOW(), NEW.cedula, "Cliente", USER(), "UPDATE");
END;
//


DELIMITER //
CREATE TRIGGER Borrar_Cliente 
AFTER DELETE ON proyecto.Cliente 
FOR EACH ROW
BEGIN
INSERT INTO AuditoriaProyecto.auditoriaCliente   (fecha, IDobjeto, Tabla, Usuario, Operacion)
VALUES (NOW(), OLD.cedula, "Cliente", USER(), "DELETE");
END;
//


--Compra
DELIMITER //
CREATE TRIGGER Insertar_Compra
AFTER INSERT ON proyecto.Compra  
FOR EACH ROW
BEGIN
INSERT INTO AuditoriaProyecto.auditoriaCompra (fecha, IDobjeto, Tabla, Usuario, Operacion)
VALUES (NOW(), NEW.IDfactura,"Compra", USER(), "INSERT");
END;
//
DELIMITER // 
CREATE TRIGGER Actualizar_Compra
AFTER UPDATE ON proyecto.Compra
FOR EACH ROW
BEGIN
INSERT INTO AuditoriaProyecto.auditoriaCompra (fecha, IDobjeto, Tabla, Usuario, Operacion)
VALUES (NOW(), NEW.IDfactura, "Compra", USER(), "UPDATE");
END;
//
DELIMITER //
CREATE TRIGGER Borrar_Compra
AFTER DELETE ON proyecto.Compra
FOR EACH ROW
BEGIN
INSERT INTO AuditoriaProyecto.auditoriaCompra (fecha, IDobjeto, Tabla, Usuario, Operacion)
VALUES (NOW(), OLD.IDfactura, "Compra", USER(), "DELETE");
END;
//


--PuntoVenta
DELIMITER //
CREATE TRIGGER Insertar_PuntoVenta
AFTER INSERT ON proyecto.PuntoVenta
FOR EACH ROW
BEGIN
INSERT INTO AuditoriaProyecto.auditoriaPuntoVenta   (fecha, IDobjeto, Tabla, Usuario, Operacion)
VALUES (NOW(), NEW.IDtienda,"PuntoVenta", USER(), "INSERT");
END;
//
DELIMITER // 
CREATE TRIGGER Actualizar_PuntoVenta
AFTER UPDATE ON proyecto.PuntoVenta
FOR EACH ROW
BEGIN
INSERT INTO AuditoriaProyecto.auditoriaPuntoVenta  (fecha, IDobjeto, Tabla, Usuario, Operacion)
VALUES (NOW(), NEW.IDtienda, "PuntoVenta", USER(), "UPDATE");
END;
//
DELIMITER //
CREATE TRIGGER Borrar_PuntoVenta
AFTER DELETE ON proyecto.PuntoVenta
FOR EACH ROW
BEGIN
INSERT INTO AuditoriaProyecto.auditoriaPuntoVenta  (fecha, IDobjeto, Tabla, Usuario, Operacion)
VALUES (NOW(), OLD.IDtienda, "PuntoVenta", USER(), "DELETE");
END;
//


--TrabajadorFinca
DELIMITER //
CREATE TRIGGER Insertar_TrabajadorFinca
AFTER INSERT ON proyecto.TrabajadorFinca
FOR EACH ROW
BEGIN
INSERT INTO AuditoriaProyecto.auditoriaEmpleado   (fecha, IDobjeto, Tabla, Usuario, Operacion)
VALUES (NOW(), NEW.cedula,"TrabajadorFinca", USER(), "INSERT");
END;
//
DELIMITER // 
CREATE TRIGGER Actualizar_TrabajadorFinca
AFTER UPDATE ON proyecto.TrabajadorFinca
FOR EACH ROW
BEGIN
INSERT INTO AuditoriaProyecto.auditoriaEmpleado (fecha, IDobjeto, Tabla, Usuario, Operacion)
VALUES (NOW(), NEW.cedula, "TrabajadorFinca", USER(), "UPDATE");
END;
//
DELIMITER //
CREATE TRIGGER Borrar_TrabajadorFinca
AFTER DELETE ON proyecto.TrabajadorFinca
FOR EACH ROW
BEGIN
INSERT INTO AuditoriaProyecto.auditoriaEmpleado  (fecha, IDobjeto, Tabla, Usuario, Operacion)
VALUES (NOW(), OLD.cedula, "TrabajadorFinca", USER(), "DELETE");
END;
//

--Vendedor
DELIMITER //
CREATE TRIGGER Insertar_Vendedor
AFTER INSERT ON proyecto.Vendedor
FOR EACH ROW
BEGIN
INSERT INTO AuditoriaProyecto.auditoriaEmpleado (fecha, IDobjeto, Tabla, Usuario, Operacion)
VALUES (NOW(), NEW.cedula, "Vendedor", USER(), "INSERT");
END;
//
DELIMITER // 
CREATE TRIGGER Actualizar_Vendedor
AFTER UPDATE ON proyecto.Vendedor
FOR EACH ROW
BEGIN
INSERT INTO AuditoriaProyecto.auditoriaEmpleado (fecha, IDobjeto, Tabla, Usuario, Operacion)
VALUES (NOW(), NEW.cedula, "Vendedor", USER(), "UPDATE");
END;
//
DELIMITER //
CREATE TRIGGER Borrar_Vendedor
AFTER DELETE ON proyecto.Vendedor
FOR EACH ROW
BEGIN
INSERT INTO AuditoriaProyecto.auditoriaEmpleado (fecha, IDobjeto, Tabla, Usuario, Operacion)
VALUES (NOW(), OLD.cedula, "Vendedor", USER(), "DELETE");
END;
//

--Transportador 
DELIMITER //
CREATE TRIGGER Insertar_Transportador 
AFTER INSERT ON proyecto.Transportador 
FOR EACH ROW
BEGIN
INSERT INTO AuditoriaProyecto.auditoriaEmpleado (fecha, IDobjeto, Tabla, Usuario, Operacion)
VALUES (NOW(), NEW.cedula,"Transportador", USER(), "INSERT");
END;
//
DELIMITER // 
CREATE TRIGGER Actualizar_Transportador 
AFTER UPDATE ON proyecto.Transportador 
FOR EACH ROW
BEGIN
INSERT INTO AuditoriaProyecto.auditoriaEmpleado (fecha, IDobjeto, Tabla, Usuario, Operacion)
VALUES (NOW(), NEW.cedula, "Transportador", USER(), "UPDATE");
END;
//
DELIMITER //
CREATE TRIGGER Borrar_Transportador 
AFTER DELETE ON proyecto.Transportador 
FOR EACH ROW
BEGIN
INSERT INTO AuditoriaProyecto.auditoriaEmpleado  (fecha, IDobjeto, Tabla, Usuario, Operacion)
VALUES (NOW(), OLD.cedula, "Transportador", USER(), "DELETE");
END;
//

--Finca
DELIMITER //
CREATE TRIGGER Insertar_Finca
AFTER INSERT ON proyecto.Finca
FOR EACH ROW
BEGIN
INSERT INTO AuditoriaProyecto.auditoriaFinca (fecha, IDobjeto, Tabla, Usuario, Operacion)
VALUES (NOW(), NEW.IDfinca, "Finca", USER(), "INSERT");
END;
//
DELIMITER // 
CREATE TRIGGER Actualizar_Finca
AFTER UPDATE ON proyecto.Finca
FOR EACH ROW
BEGIN
INSERT INTO AuditoriaProyecto.auditoriaFinca(fecha, IDobjeto, Tabla, Usuario, Operacion)
VALUES (NOW(), NEW.IDfinca, "Finca", USER(), "UPDATE");
END;
//
DELIMITER //
CREATE TRIGGER Borrar_Finca
AFTER DELETE ON proyecto.Finca
FOR EACH ROW
BEGIN
INSERT INTO AuditoriaProyecto.auditoriaFinca (fecha, IDobjeto, Tabla, Usuario, Operacion)
VALUES (NOW(), OLD.IDfinca, "Finca", USER(), "DELETE");
END;
//

--establo 
DELIMITER //
CREATE TRIGGER Insertar_Establo
AFTER INSERT ON proyecto.Establo
FOR EACH ROW
BEGIN
INSERT INTO AuditoriaProyecto.auditoriaEstablo (fecha, IDobjeto, Tabla, Usuario, Operacion)
VALUES (NOW(), NEW.IDestablo,"Establo", USER(), "INSERT");
END;
//
DELIMITER // 
CREATE TRIGGER Actualizar_Establo
AFTER UPDATE ON proyecto.Establo
FOR EACH ROW
BEGIN
INSERT INTO AuditoriaProyecto.auditoriaEstablo(fecha, IDobjeto, Tabla, Usuario, Operacion)
VALUES (NOW(), NEW.IDestablo, "Establo", USER(), "UPDATE");
END;
//
DELIMITER //
CREATE TRIGGER Borrar_Establo
AFTER DELETE ON proyecto.Establo
FOR EACH ROW
BEGIN
INSERT INTO AuditoriaProyecto.auditoriaEstablo (fecha, IDobjeto, Tabla, Usuario, Operacion)
VALUES (NOW(), OLD.IDestablo, "Establo", USER(), "DELETE");
END;
//

--animal 
DELIMITER //
CREATE TRIGGER Insertar_Animal
AFTER INSERT ON proyecto.Animal
FOR EACH ROW
BEGIN
INSERT INTO AuditoriaProyecto.auditoriaAnimal (fecha, IDobjeto, Tabla, Usuario, Operacion)
VALUES (NOW(), NEW.IDanimal,"Animal", USER(), "INSERT");
END;
//
DELIMITER // 
CREATE TRIGGER Actualizar_Animal
AFTER UPDATE ON proyecto.Animal
FOR EACH ROW
BEGIN
INSERT INTO AuditoriaProyecto.auditoriaAnimal(fecha, IDobjeto, Tabla, Usuario, Operacion)
VALUES (NOW(), NEW.IDanimal, "Animal", USER(), "UPDATE");
END;
//
DELIMITER //
CREATE TRIGGER Borrar_Animal
AFTER DELETE ON proyecto.Animal
FOR EACH ROW
BEGIN
INSERT INTO AuditoriaProyecto.auditoriaAnimal (fecha, IDobjeto, Tabla, Usuario, Operacion)
VALUES (NOW(), OLD.IDanimal, "Animal", USER(), "DELETE");
END;
//

--loteProduccion 
DELIMITER //
CREATE TRIGGER Insertar_LoteProduccion 
AFTER INSERT ON proyecto.LoteProduccion 
FOR EACH ROW
BEGIN
INSERT INTO AuditoriaProyecto.auditoriaLoteProduccion (fecha, IDobjeto, Tabla, Usuario, Operacion)
VALUES (NOW(), NEW.IDlote,"LoteProduccion ", USER(), "INSERT");
END;
//
DELIMITER // 
CREATE TRIGGER Actualizar_LoteProduccion 
AFTER UPDATE ON proyecto.LoteProduccion 
FOR EACH ROW
BEGIN
INSERT INTO AuditoriaProyecto.auditoriaLoteProduccion(fecha, IDobjeto, Tabla, Usuario, Operacion)
VALUES (NOW(), NEW.IDlote, "LoteProduccion ", USER(), "UPDATE");
END;
//
DELIMITER //
CREATE TRIGGER Borrar_LoteProduccion 
AFTER DELETE ON proyecto.LoteProduccion 
FOR EACH ROW
BEGIN
INSERT INTO AuditoriaProyecto.auditoriaLoteProduccion (fecha, IDobjeto, Tabla, Usuario, Operacion)
VALUES (NOW(), OLD.IDlote, "LoteProduccion ", USER(), "DELETE");
END;
//

--CamionCarga
DELIMITER //
CREATE TRIGGER Insertar_CamionCarga
AFTER INSERT ON proyecto.CamionCarga
FOR EACH ROW
BEGIN
INSERT INTO AuditoriaProyecto.auditoriaCamionCarga (fecha, IDobjeto, Tabla, Usuario, Operacion)
VALUES (NOW(), NEW.matricula,"CamionCarga", USER(), "INSERT");
END;
//
DELIMITER // 
CREATE TRIGGER Actualizar_CamionCarga
AFTER UPDATE ON proyecto.CamionCarga
FOR EACH ROW
BEGIN
INSERT INTO AuditoriaProyecto.auditoriaCamionCarga(fecha, IDobjeto, Tabla, Usuario, Operacion)
VALUES (NOW(), NEW.matricula, "CamionCarga", USER(), "UPDATE");
END;
//

DELIMITER //
CREATE TRIGGER Borrar_CamionCarga
AFTER DELETE ON proyecto.CamionCarga
FOR EACH ROW
BEGIN
INSERT INTO AuditoriaProyecto.auditoriaCamionCarga (fecha, IDobjeto, Tabla, Usuario, Operacion)
VALUES (NOW(), OLD.matricula, "CamionCarga", USER(), "DELETE");
END;
//


--alimento 
DELIMITER //
CREATE TRIGGER Insertar_Alimento 
AFTER INSERT ON proyecto.Alimento
FOR EACH ROW
BEGIN
INSERT INTO AuditoriaProyecto.auditoriaAlimento (fecha, IDobjeto, Tabla, Usuario, Operacion)
VALUES (NOW(), NEW.IDalimento,"Alimento", USER(), "INSERT");
END;
//
DELIMITER // 
CREATE TRIGGER Actualizar_Alimento
AFTER UPDATE ON proyecto.Alimento
FOR EACH ROW
BEGIN
INSERT INTO AuditoriaProyecto.auditoriaAlimento(fecha, IDobjeto, Tabla, Usuario, Operacion)
VALUES (NOW(), NEW.IDalimento, "Alimento", USER(), "UPDATE");
END;
//
DELIMITER //
CREATE TRIGGER Borrar_Alimento
AFTER DELETE ON proyecto.Alimento
FOR EACH ROW
BEGIN
INSERT INTO AuditoriaProyecto.auditoriaAlimento (fecha, IDobjeto, Tabla, Usuario, Operacion)
VALUES (NOW(), OLD.IDalimento, "Alimento", USER(), "DELETE");
END;
//

--Alimento/Carne
DELIMITER //
CREATE TRIGGER Insertar_Carne
AFTER INSERT ON proyecto.Carne
FOR EACH ROW
BEGIN
INSERT INTO AuditoriaProyecto.auditoriaAlimento (fecha, IDobjeto, Tabla, Usuario, Operacion)
VALUES (NOW(), NEW.IDalimento,"Carne", USER(), "INSERT");
END;
//
DELIMITER // 
CREATE TRIGGER Actualizar_Carne
AFTER UPDATE ON proyecto.Carne
FOR EACH ROW
BEGIN
INSERT INTO AuditoriaProyecto.auditoriaAlimento(fecha, IDobjeto, Tabla, Usuario, Operacion)
VALUES (NOW(), NEW.IDalimento, "Carne", USER(), "UPDATE");
END;
//
DELIMITER //
CREATE TRIGGER Borrar_Carne
AFTER DELETE ON proyecto.Carne
FOR EACH ROW
BEGIN
INSERT INTO AuditoriaProyecto.auditoriaAlimento (fecha, IDobjeto, Tabla, Usuario, Operacion)
VALUES (NOW(), OLD.IDalimento, "Carne", USER(), "DELETE");
END;
//

--Alimento/CartonHuevo
DELIMITER //
CREATE TRIGGER Insertar_CartonHuevo
AFTER INSERT ON proyecto.CartonHuevo
FOR EACH ROW
BEGIN
INSERT INTO AuditoriaProyecto.auditoriaAlimento (fecha, IDobjeto, Tabla, Usuario, Operacion)
VALUES (NOW(), NEW.IDalimento,"CartonHuevo", USER(), "INSERT");
END;
//
DELIMITER // 
CREATE TRIGGER Actualizar_CartonHuevo
AFTER UPDATE ON proyecto.CartonHuevo
FOR EACH ROW
BEGIN
INSERT INTO AuditoriaProyecto.auditoriaAlimento(fecha, IDobjeto, Tabla, Usuario, Operacion)
VALUES (NOW(), NEW.IDalimento, "CartonHuevo", USER(), "UPDATE");
END;
//
DELIMITER //
CREATE TRIGGER Borrar_CartonHuevo
AFTER DELETE ON proyecto.CartonHuevo
FOR EACH ROW
BEGIN
INSERT INTO AuditoriaProyecto.auditoriaAlimento (fecha, IDobjeto, Tabla, Usuario, Operacion)
VALUES (NOW(), OLD.IDalimento, "CartonHuevo", USER(), "DELETE");
END;
//

--Alimento/Cultivo
DELIMITER //
CREATE TRIGGER Insertar_Cultivo
AFTER INSERT ON proyecto.Cultivo
FOR EACH ROW
BEGIN
INSERT INTO AuditoriaProyecto.auditoriaAlimento (fecha, IDobjeto, Tabla, Usuario, Operacion)
VALUES (NOW(), NEW.IDalimento,"Cultivo", USER(), "INSERT");
END;
//
DELIMITER // 
CREATE TRIGGER Actualizar_Cultivo
AFTER UPDATE ON proyecto.Cultivo
FOR EACH ROW
BEGIN
INSERT INTO AuditoriaProyecto.auditoriaAlimento(fecha, IDobjeto, Tabla, Usuario, Operacion)
VALUES (NOW(), NEW.IDalimento, "Cultivo", USER(), "UPDATE");
END;
//
DELIMITER //
CREATE TRIGGER Borrar_Cultivo
AFTER DELETE ON proyecto.Cultivo
FOR EACH ROW
BEGIN
INSERT INTO AuditoriaProyecto.auditoriaAlimento (fecha, IDobjeto, Tabla, Usuario, Operacion)
VALUES (NOW(), OLD.IDalimento, "Cultivo", USER(), "DELETE");
END;
//