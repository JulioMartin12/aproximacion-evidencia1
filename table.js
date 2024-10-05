function cargarTabla(projectId) {
    let url;
  console.log("Entro")
    // Determinar la URL en función del proyecto
    switch (projectId) {
        
      case 1:
        url = "URL_API_DEL_PROYECTO_1"; 
        break;
      case 2:
        url = "URL_API_DEL_PROYECTO_2";
        break;
      case 3:
        url = "https://aproximacion-evidencia1.onrender.com/api/monitor_sonido";
        break;
      default:
        console.error("Proyecto no encontrado");
        return;
    }
  
    // Realizar la solicitud fetch
    fetch(url)
      .then(response => {
        if (!response.ok) {
          throw new Error('Error en la red: ' + response.statusText);
        }
        return response.json();
      })
      .then(data => {
        console.log("Datos recibidos:", data); // Agregado para depuración
        mostrarDatosEnTabla(data); // Llamada a la función que muestra los datos
      })
      .catch(error => {
        console.error('Error al cargar los datos:', error);
      });
  }
  
  function mostrarDatosEnTabla(data) {
    const tablaDatos = document.getElementById('tabla-datos').getElementsByTagName('tbody')[0];
    
    // Limpiar la tabla antes de agregar nuevos datos
    tablaDatos.innerHTML = '';
  
    // Verificar que los datos no estén vacíos
    if (!data || data.length === 0) {
      const nuevaFila = tablaDatos.insertRow();
      const celda = nuevaFila.insertCell(0);
      celda.colSpan = 3; // Número de columnas en la tabla
      celda.textContent = 'No hay datos disponibles';
      document.getElementById('tabla-datos').style.display = 'table'; // Asegúrate de que la tabla se muestre
      return;
    }
  
    // Iterar sobre los datos y agregarlos a la tabla
    data.forEach(item => {
      const nuevaFila = tablaDatos.insertRow();
      const celda1 = nuevaFila.insertCell(0);
      const celda2 = nuevaFila.insertCell(1);
      const celda3 = nuevaFila.insertCell(2);
      
      // Asignar valores a las celdas (ajusta los nombres de las propiedades según el API)
      celda1.textContent = item.campo1 || 'Sin datos'; 
      celda2.textContent = item.campo2 || 'Sin datos'; 
      celda3.textContent = item.campo3 || 'Sin datos';
    });
  
    // Mostrar la tabla después de cargar los datos
    document.getElementById('tabla-datos').style.display = 'table';
  }
