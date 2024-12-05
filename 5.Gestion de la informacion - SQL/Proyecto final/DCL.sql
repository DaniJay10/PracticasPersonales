CREATE ROLE Almacen_Datos;

grant all
on Proyecto.*
to Almacen_Datos 
with grant option;

grant all
on AuditoriaProyecto.*
to Almacen_Datos
with grant option;


CREATE ROLE Desarrollador;

grant ALTER, CREATE, DELETE, DROP, INDEX, INSERT, SELECT, UPDATE
 on Proyecto.* 
 to Desarrollador;

grant CREATE, SELECT
on AuditoriaProyecto.* 
to Desarrollador;


CREATE ROLE APP_Principal;

grant INSERT, UPDATE, DELETE, SELECT
on Proyecto.* 
to APP_Principal;


CREATE ROLE Auditor;

grant SELECT 
on Proyecto.* 
to Auditor;

grant SELECT 
on AuditoriaProyecto.* 
to Auditor;


CREATE USER 'Administrador'@'localhost' IDENTIFIED BY 'A1823m';
GRANT Almacen_Datos TO 'Administrador'@'localhost';
SET DEFAULT ROLE Almacen_Datos FOR 'Administrador'@'localhost';

CREATE USER 'Daniel'@'localhost' IDENTIFIED BY '1';
GRANT Desarrollador TO 'Daniel'@'localhost';
SET DEFAULT ROLE Desarrollador FOR 'Daniel'@'localhost';

CREATE USER 'Yeimy'@'localhost' IDENTIFIED BY '2';
GRANT Desarrollador TO 'Yeimy'@'localhost';
SET DEFAULT ROLE Desarrollador FOR 'Yeimy'@'localhost';

CREATE USER 'Gustavo'@'localhost' IDENTIFIED BY '3';
GRANT Desarrollador TO 'Gustavo'@'localhost';
SET DEFAULT ROLE Desarrollador FOR 'Gustavo'@'localhost';

CREATE USER 'Empleado'@'localhost' IDENTIFIED BY 'A12024';
GRANT APP_Principal TO 'Empleado'@'localhost';
SET DEFAULT ROLE APP_Principal FOR 'Empleado'@'localhost';

CREATE USER 'Auditor'@'localhost' IDENTIFIED BY '123';
GRANT Auditor TO 'Auditor'@'localhost';
SET DEFAULT ROLE Auditor FOR 'Auditor'@'localhost';


