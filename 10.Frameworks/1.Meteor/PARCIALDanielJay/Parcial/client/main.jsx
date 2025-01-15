import React, { useState } from 'react';
import { Meteor } from 'meteor/meteor';
import { createRoot } from 'react-dom/client'; 

const FormularioPaciente = () => {
  const [metodo, setMetodo] = useState('');
  const [formularioHTML, setFormularioHTML] = useState('');

  const procesarMetodo = () => {
    const metodoNum = parseInt(metodo);
    let nuevoFormularioHTML = '';

    switch (metodoNum) {
//REGISTRAR PACIENTE
      case 1:
        nuevoFormularioHTML = (
          <form
          onSubmit={(e) => {
            e.preventDefault();
            const cedula = e.target.cedula.value;
            const nombre = e.target.nombre.value;
            const fechaNac = e.target.fechaNac.value;
            const genero = e.target.genero.value;
            Meteor.call('paciente.crear', cedula, nombre, fechaNac, genero, (err, res) => {
              if (err) {
                alert(`Error: ${err.reason}`); 
              } else {
                alert(res.message); 
                e.target.reset();
              }
            });
          }}
        >
            <input type="hidden" name="metodo" value="1" />
            <p>Ingrese Cédula</p>
            <input type="text" name="cedula" placeholder="Cédula" required /><br />
            <p>Ingrese Nombre</p>
            <input type="text" name="nombre" placeholder="Nombre" required/><br />
            <p>Ingrese Fecha Nacimiento</p>
            <input type="date" name="fechaNac" placeholder="Fecha nacimiento" required/><br />
            <p>Ingrese Género (M o F)</p>
            <input type="text" name="genero" placeholder="Género" required/><br />
            <br />
            <input type="submit" value="Enviar" />
          </form>
        );
        break;


//BUSCAR PACIENTE
      case 2:
        nuevoFormularioHTML = (
          <form onSubmit={(e) => {
            e.preventDefault();
            const cedula = e.target.cedula.value;
            Meteor.call('paciente.buscar', cedula, (err, res) => {
              if (err) {
                alert(`Error: ${err.message}`);
              } else {
                if (res && res.success && res.data) {
                  const paciente = res.data; 
                  const fechaNac = new Date(paciente.fechaNac).toLocaleDateString('es-ES');
                  alert(
                    `Paciente encontrado:\nCédula: ${paciente.cedula}\nNombre: ${paciente.nombre}\nFecha de Nacimiento: ${fechaNac}\nGénero: ${paciente.genero}`);
                     e.target.reset();
                } else {
                  alert(res.message); 
                  e.target.reset();
                }
              }
            });
          }}>
            <input type="hidden" name="metodo" value="2" />
            <p>Ingrese Cédula del paciente a ver</p>
            <input type="text" name="cedula" placeholder="Cédula" required /><br />
            <input type="submit" value="Buscar" />
          </form>
        );
        break;


//EDITAR PACIENTE
      case 3:
        nuevoFormularioHTML = (
          <form  onSubmit={(e) => {
            e.preventDefault();
            const cedula = e.target.cedula.value;
            const cedulaN = e.target.cedulaNueva.value;
            const nombre = e.target.nombre.value;
            const fechaNac = e.target.fechaNac.value;
            const genero = e.target.genero.value;
            Meteor.call('paciente.editar', cedula, cedulaN, nombre, fechaNac, genero, (err, res) => {
              if (err) {
                alert(`Error: ${err.reason}`); 
              } else {
                alert(res.message); 
                e.target.reset();
              }
            });
          }}>
            <input type="hidden" name="metodo" value="3" />
            <p>Ingrese Cédula del paciente a modificar</p>
            <input type="text" name="cedula" placeholder="Cédula" required /><br />
            <p>Ingrese nueva cédula</p>
            <input type="text" name="cedulaNueva" placeholder="Nueva cédula" /><br />
            <p>Ingrese nuevo nombre</p>
            <input type="text" name="nombre" placeholder="Nuevo nombre" /><br />
            <p>Ingrese nueva fecha de nacimiento</p>
            <input type="date" name="fechaNac" placeholder="Nueva fecha nacimiento" /><br />
            <p>Ingrese nuevo género (M o F)</p>
            <input type="text" name="genero" placeholder="Nuevo género" /><br />
            <br />
            <input type="submit" value="Enviar" /><br />
            <b>NOTA: Si no desea modificar algún dato, deje el campo vacío.</b>
          </form>
        );
        break;


//CALCULAR EDAD
      case 4:
        nuevoFormularioHTML = (
          <form onSubmit={(e) => {
            e.preventDefault();
            const cedula = e.target.cedula.value;
            const fechaActual = new Date(e.target.fechaActual.value); 
            const anioActual = fechaActual.getFullYear(); 
            Meteor.call('Paciente.calcular.edad', cedula, anioActual, (err, res) => {
              if (err) {
                alert(`Error: ${err.message}`);
              } else {
                if (res && res.success) {
                  alert(`Paciente: ${res.data.nombre}\nEdad: ${res.data.edad} años`);
                  e.target.reset();
                } else {
                  alert(res.message); 
                  e.target.reset();
                }
              }
            });
          }}>
            <input type="hidden" name="metodo" value="4" />
            <p>Ingrese Cédula del paciente para calcular la edad</p>
            <input type="text" name="cedula" placeholder="Cédula" required /><br />
            <p>Ingrese la fecha actual</p>
            <input type="date" name="fechaActual" placeholder="Fecha actual" required /><br />
            <br />
            <input type="submit" value="Calcular" />
          </form>
        );
        break;


//ELIMINAR PACIENTE
      case 5:
        nuevoFormularioHTML = (
          <form onSubmit={(e) => {
            e.preventDefault();
            const cedula = e.target.cedulaBorrar.value;
            Meteor.call('paciente.eliminar', cedula, (err, res) => {
              if (err) {
                alert(`Error: ${err.message}`);
              } else {
                if (res && res.success) {
                  alert(res.message); 
                  e.target.reset();
                } else {
                  alert(res.message); 
                  e.target.reset();
                }
              }
            });
          }}>
            <input type="hidden" name="metodo" value="5" />
            <p>Ingrese Cédula del paciente a eliminar</p>
            <input type="text" name="cedulaBorrar" placeholder="Cédula" required /><br />
            <input type="submit" value="Eliminar" />
          </form>
        );
        break;
//ver citas del paciente
        case 6:
            nuevoFormularioHTML = (
              <form onSubmit={(e) => {
                e.preventDefault();
                const cedula = e.target.cedula.value;
                Meteor.call('paciente.citas', cedula, (err, res) => {
                  if (err) {
                    alert(`Error: ${err.message}`);
                  } else {
                    if (res && res.success) {
                      alert(res.message); 
                      e.target.reset();
                    } else {
                      alert(`citas: ${res}`); 
                      e.target.reset();
                    }
                  }
                });
              }}>
              <input type="hidden" name="metodo" value="2" />
              <p>Ingrese cedula paciente a ver citas</p>
              <input type="text" name="cedula" placeholder="Cédula" required /><br />
              <input type="submit" value="Buscar" />
              </form>
            );
            break;
//crear cita
        case 7:
          nuevoFormularioHTML = (
            <form onSubmit={(e) => {
              e.preventDefault();
              const fecha = e.target.fecha.value;
              const nombreDoctor = e.target.nmed.value;
              const MedicamentosGenerados = e.target.medsn.value;
              const cedulaPaciente = e.target.cedp.value;
              Meteor.call('cita.crear', fecha, nombreDoctor, MedicamentosGenerados, cedulaPaciente, (err, res) => {
                if (err) {
                  alert(`Error: ${err.reason}`); 
                } else {
                  alert(res.message); 
                  e.target.reset();
                }
              });
            }}>
              <input type="hidden" name="metodo" value="7" />
              <p>Fecha cita</p>
              <input type="date" name="fecha" placeholder="Fecha cita" required /><br />
              <p>Nombre medico</p>
              <input type="text" name="nmed" placeholder="Nombre medico" required /><br />
              <p>¿Se crearon medicamentos?</p>
              <input type="text" name="medsn" placeholder="responder si o no" required /><br />
              <p>Cedula del paciente</p>
              <input type="text" name="cedp" placeholder="Cedula del Paciente" required /><br />
              <input type="submit" value="crear cita" />
            </form>
          );
          break;
        case 8:
            nuevoFormularioHTML = (
              <form >
              <input type="hidden" name="metodo" value="2" />
              <p>Ingrese cedula paciente a listar citas</p>
              <input type="text" name="cedula" placeholder="Cédula" required /><br />
              <input type="submit" value="Buscar" />
              </form>
            );
            break;
      default:
        nuevoFormularioHTML = <p>¡¡¡ERROR!!! Opción no válida</p>;



    }

    setFormularioHTML(nuevoFormularioHTML);
  };

  return (
    <div>
      <form>
        <ol>
        <p>Paciente:</p>
          <li>Crear Paciente</li>
          <li>Ver Paciente</li>
          <li>Editar Paciente</li>
          <li>Calcular edad</li>
          <li>Eliminar Paciente</li>
          <li>ver citas del Paciente</li>
          <br />
        <p id="texto">Citas:</p>
          <li>Crear cita</li>
          <li>Listar cita del paciente por fecha</li>
        </ol>
        <br />
        <br />

        <label htmlFor="metodo">Método:</label>
        <input type="text" id="metodo" name="metodo" value={metodo} onChange={(e) => setMetodo(e.target.value)}/>
        <br />
        <br />
        <button type="button" onClick={procesarMetodo}>Ejecutar</button>
      </form>
      <div id="formularioPaciente">{formularioHTML}</div>
    </div>
  );
};

Meteor.startup(() => {
  const container = document.getElementById('react-target');
  const root = createRoot(container);  
  root.render(<FormularioPaciente />);  
});