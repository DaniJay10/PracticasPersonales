import { Meteor } from 'meteor/meteor';
import connection from './mysqlconexion';

Meteor.methods({
  //CREACION DE PACIENTES
  async 'paciente.crear'(cedula, nombre, fechaNac, genero) {
    try {
      if (genero !== 'M' && genero !== 'F') {
        throw new Meteor.Error('Género inválido', 'Digite un género válido (M o F)');
      }else{
      const query = `INSERT INTO Paciente VALUES (${cedula}, '${nombre}', '${fechaNac}', '${genero}')`;
      await connection.query(query);
      return { success: true, message: `Paciente con cedula ${cedula} registrado correctamente` };
      }
    } catch (error) {
      throw new Meteor.Error('Error al registrar paciente', error.message);
    }
  },



  //BUSCAR EL PACIENTE CON LA CEDULA
  async 'paciente.buscar'(cedula) {
    try{
      const query = `SELECT * FROM Paciente WHERE cedula = ${cedula}`;
      const [paciente] = await connection.query(query);
      if (paciente.length > 0) {
        const pac = paciente[0];
        return {
          success: true,
          data: pac
        };
        } else {
        return {
          success: false,
          message: `No se encontró paciente con cédula ${cedula}`
        };
      }
    } catch (error) {
      throw new Meteor.Error('Error al buscar el paciente', error.message);
    }
  },


  //EDITAR EL PACIENTE
  async 'paciente.editar'(cedula, cedulaN, nombre, fechaNac, genero){
    try{
      if (genero === 'M' || genero === 'F' || genero === '') {
        const query = `SELECT * FROM Paciente WHERE cedula = ${cedula}`;
        const [resultado] = await connection.query(query);
        if (resultado.length > 0){
          const paciente = resultado[0];
          const datosActualizados = [];
          if (cedulaN && cedulaN !== paciente.cedula) {
            datosActualizados.push(`cedula = ${cedulaN}`);
          }
          if (nombre && nombre !== paciente.nombre) {
            datosActualizados.push(`nombre = '${nombre}'`);
          }
          if (fechaNac && fechaNac !== paciente.fechaNac) {
            datosActualizados.push(`fechaNac = '${fechaNac}'`);
          }
          if (genero && genero !== paciente.genero) {
            datosActualizados.push(`genero = '${genero}'`);
          }
          if (datosActualizados.length > 0) {
            const updateQuery = `UPDATE Paciente SET ${datosActualizados.join(', ')} WHERE cedula = ${cedula}`;
            console.log(`Consulta SQL de actualización: ${updateQuery}`); 
            await connection.query(updateQuery);
            return {
              success: true,
              message: 'Paciente actualizado correctamente',
            };
          }else{
            return {
              success: false,
              message: 'No se realizaron cambios en los datos del paciente',
            };
          }
        }else{
          return {
            success: false,
            message: `No se encontró paciente con cédula ${cedula}`
          };
        }
      }else{
        throw new Meteor.Error('Género inválido', 'Digite un género válido (M o F)');
    }
    }catch (error) {
      throw new Meteor.Error('Error al editar el paciente', error.message);
    }
  },



  //CALCULAR FECHA NACIMIENTO
  async 'Paciente.calcular.edad'(cedula, anioActual){
   try{
    const query = `SELECT fechaNac,nombre FROM Paciente WHERE cedula = ${cedula}`;
    const [paciente] = await connection.query(query);
    if (paciente.length>0){
      const pac = paciente[0];
      const fechaNac = new Date(pac.fechaNac); 
      const anioNacimiento = fechaNac.getFullYear();
      const edad = anioActual - anioNacimiento;
      return {
        success: true,
        data: {
          nombre: pac.nombre,
          edad: edad
        }
      };
    }else{
      return {
        success: false,
        message: `No se encontro al paciente con cedula ${cedula}`
      };
    }
   }catch (error) {
     throw new Meteor.Error('Error al calcular la edad', error.message);
   }
  },


  //ELIMINAR PACIENTE
  async 'paciente.eliminar'(cedula){
    try{
      const query = `DELETE FROM Paciente WHERE cedula = ${cedula}`;
      const [pacienteEliminado] = await connection.query(query);
      if (pacienteEliminado.affectedRows  > 0){
        return {
          success: true,
          message: `Paciente con cedula ${cedula} ha sido eliminado`
        };
      }else{
        return{
        success: false,
        message: `No se encontro al paciente con cedula: ${cedula}`
        };
      }
    } catch (error){
      throw new Meteor.Error('Error al eliminar el paciente', error.message);
    }
  },

  //ver citas del paciente
  async 'paciente.citas'(cedula) {
    try{
      const query = `SELECT * FROM Paciente WHERE cedula = ${cedula}`;
      const [paciente] = await connection.query(query);
      if (paciente.length > 0) {
        const query = `SELECT p.cedula FROM paciente p LEFT JOIN cita c ON p.cedula = c.cedulaPaciente;`;
        const [resultado] = await connection.query(query);
        const res = resultado[0];
        return{
          success: true,
          data: res
        };
        } else {
        return {
          success: false,
          message: `No se encontró paciente con cédula ${cedula}`
        };
      }
    } catch (error) {
      throw new Meteor.Error('Error al buscar el paciente', error.message);
    }
  },

  //crear cita
  async 'cita.crear'(fecha, nombreDoctor, MedicamentosGenerados, cedulaPaciente) {
    try{
      const query = `SELECT * FROM Paciente WHERE cedula = ${cedulaPaciente}`;
      const [paciente] = await connection.query(query);
      if (paciente.length > 0) {
        const query = `INSERT INTO cita VALUES ('${fecha}', '${nombreDoctor}', '${MedicamentosGenerados}', '${cedulaPaciente}')`;
        await connection.query(query);
        return { success: true, message: `Cita creada correctamente` };
        } else {
        return {
          success: false,
          message: `No se encontró paciente con cédula ${cedulaPaciente}`
        };
      }
    } catch (error) {
      throw new Meteor.Error('Error al crear cita', error.message);
    }
  },

});



