function cargarTabla(projectId) {
    let url;
  console.log("Entro")

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
  
   
    fetch(url)
      .then(response => {
        if (!response.ok) {
          throw new Error('Error en la red: ' + response.statusText);
        }
        return response.json();
      })
      .then(data => {
        console.log("Datos recibidos:", data); 
        mostrarDatosEnTabla(data); 
      })
      .catch(error => {
        console.error('Error al cargar los datos:', error);
      });
  }
  
  function mostrarDatosEnTabla(data) {
    const tablaDatos = document.getElementById('tabla-datos').getElementsByTagName('tbody')[0];
    
 
    tablaDatos.innerHTML = '';
  
    
    if (!data || data.length === 0) {
      const nuevaFila = tablaDatos.insertRow();
      const celda = nuevaFila.insertCell(0);
      celda.colSpan = 3; 
      celda.textContent = 'No hay datos disponibles';
      document.getElementById('tabla-datos').style.display = 'table'; 
      return;
    }
  
   
    data.forEach(item => {
      const nuevaFila = tablaDatos.insertRow();
      const celda1 = nuevaFila.insertCell(0);
      const celda2 = nuevaFila.insertCell(1);
      const celda3 = nuevaFila.insertCell(2);
      
   
      celda1.textContent = item.campo1 || 'Sin datos'; 
      celda2.textContent = item.campo2 || 'Sin datos'; 
      celda3.textContent = item.campo3 || 'Sin datos';
    });
  
   
    document.getElementById('tabla-datos').style.display = 'table';
  }
