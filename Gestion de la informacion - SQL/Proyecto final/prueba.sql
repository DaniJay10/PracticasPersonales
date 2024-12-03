CREATE TABLE prueba (
    ID INT PRIMARY KEY,
    Nombre VARCHAR(50),
    Edad INT
);

INSERT INTO prueba (ID, Nombre, Edad) VALUES (1, 'Juan', 25);

UPDATE prueba SET Edad = 26 WHERE ID = 1;


SELECT * FROM prueba;

DELETE FROM prueba WHERE ID = 1;

DROP TABLE prueba;
