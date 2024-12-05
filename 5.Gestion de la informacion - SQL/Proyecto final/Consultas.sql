--CONSULTAS
--Numero de ventas realizadas por punto de venta
SELECT pv.IDtienda, COUNT(c.IDfactura) AS NumeroDeVentas
FROM puntoVenta pv
LEFT JOIN compra c ON pv.IDtienda = c.IDtienda
GROUP BY pv.IDtienda;
--Obtener las etapas de desarollo de los animales en la finca maria
SELECT a.IDanimal, a.tipo, a.EtapaDesarrollo, e.IDestablo as Establo
FROM Animal a
JOIN establo e ON a.Establo = e.IDestablo
JOIN finca f ON e.IDfinca = f.IDfinca
WHERE f.Nombre = "Maria";
--Promedio de salarios por labor en la finca Napoleon
SELECT tf.Labor, COUNT(*) AS TotalTrabajadores,
       (SELECT AVG(salario)
        FROM empleado e
        WHERE e.cedula = tf.cedula
       ) AS SalarioPromedio
FROM trabajadorFinca tf
WHERE tf.finca = 41
GROUP BY tf.Labor;
--Horas trabajadas al dia por cada empleado
SELECT p.nombre AS NombreVendedor,
       v.cedula AS CedulaVendedor,
       SUM(TIMESTAMPDIFF(HOUR, v.HoraEntrada, v.HoraSalida)) AS TotalHorasTrabajadas
FROM vendedor v
JOIN persona p ON v.cedula = p.cedula
GROUP BY v.cedula, p.nombre;
--se requiere saber todos los datos de las personas que trabajan en la finca Antonio
SELECT *
FROM persona
WHERE cedula IN (
    SELECT cedula
    FROM empleado
    WHERE cedula IN (
        SELECT cedula
        FROM trabajadorFinca
        WHERE finca = 45));
--Se requiere saber cuantos animales hay en los establos, que animales hay y el id de los establos 
SELECT e.IDestablo, e.tipo AS "Tipo_Establo", a.Tipo_Animal, a.Numero_Animales
FROM establo e
JOIN (
    SELECT establo, MIN(tipo) AS "Tipo_Animal", COUNT(*) AS "Numero_Animales"
    FROM animal
    GROUP BY establo
) a ON e.IDestablo = a.establo;
--Se necesita consultar la cantidad de compras que ha hecho cada cliente 
SELECT cedula, clasificacion, IFNULL(cantidad_compras, 0) AS cantidad_compras
FROM cliente
LEFT JOIN (
    SELECT cedula_cliente, COUNT(*) AS cantidad_compras
    FROM compra
    GROUP BY cedula_cliente
) AS compras_por_cliente ON cliente.cedula = compras_por_cliente.cedula_cliente;
--consultar cantidad disponible de huevos por su clasificacion y tipo 
SELECT cf.clasificacion AS "Clasificacion",
    cf.tipoHuevo AS "Tipo_Huevo",
    SUM(cf.unidades) AS "Cantidad_Disponible"
FROM CartonHuevo cf
LEFT JOIN loteProduccion lp ON cf.IDalimento = lp.IDlote
WHERE lp.estado IS NULL OR lp.estado = "En punto de venta"
GROUP BY cf.clasificacion, cf.tipoHuevo;
--la consulta muestra la informacion del vendedor y las tiendas a las que va como el id de la tienda junto con la Horaentrada y HoraSalida
SELECT vendedor.cedula, vendedor.HoraEntrada, vendedor.HoraSalida, 
    (SELECT direccion FROM puntoVenta WHERE IDtienda = vendedor.tienda) AS direccion_tienda
FROM vendedor;
--Consultar los tipos de carnes junto con su corte que tiene cada lote de produccion (si es que tienen)
SELECT la.IDlote AS ID_lote_produccion,
       (SELECT tipo FROM carne WHERE IDalimento = la.IDalimento) AS tipo_carne,
       (SELECT corte FROM carne WHERE IDalimento = la.IDalimento) AS tipo_corte
FROM lote_alimento la
WHERE EXISTS (SELECT * FROM carne WHERE IDalimento = la.IDalimento);