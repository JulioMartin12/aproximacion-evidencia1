document.addEventListener('DOMContentLoaded', function() {
     function cargarTabla() {
        fetch('https://aproximacion-evidencia1.onrender.com/api/monitor_sonido')

            .then(response => {
                if (!response.ok) {
                    throw new Error('Error en la red: ' + response.statusText);
                }
                return response.json();
            })
            .then(data => {
                const table = document.getElementById('data-table');
                table.innerHTML = '';

                if (data.data.length > 0) {
                    const headerRow = document.createElement('tr');
                    const columns = Object.keys(data.data[0]); 
                    columns.forEach(col => {
                        const th = document.createElement('th');
                        th.textContent = col;
                        headerRow.appendChild(th);
                    });
                    table.appendChild(headerRow);

                  
                    data.data.forEach(row => {
                        const tableRow = document.createElement('tr');
                        columns.forEach(col => {
                            const td = document.createElement('td');
                            td.textContent = row[col];
                            tableRow.appendChild(td);
                        });
                        table.appendChild(tableRow);
                    });
                } else {
                    const noDataRow = document.createElement('tr');
                    const noDataCell = document.createElement('td');
                    noDataCell.colSpan = 3; 
                    noDataCell.textContent = 'No hay datos disponibles';
                    noDataRow.appendChild(noDataCell);
                    table.appendChild(noDataRow);
                }
            })
            .catch(error => {
                console.error('Error al cargar los datos:', error);
                alert('Error al cargar los datos: ' + error.message);
            });
    }

     const loadButton = document.getElementById('load-button');
    if (loadButton) {
        loadButton.addEventListener('click', cargarTabla);
    } else {
        console.error('No se encontró el botón de carga.');
    }
});
