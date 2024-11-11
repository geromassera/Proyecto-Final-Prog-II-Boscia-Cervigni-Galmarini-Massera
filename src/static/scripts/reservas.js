document.getElementById('reservationForm').addEventListener('submit', function(event) {
    event.preventDefault(); 


    const nombre = document.getElementById('nombre').value.trim();
    const comensales = document.getElementById('comensales').value;
    const fecha = document.getElementById('fecha').value;
    const hora = document.getElementById('hora').value;


    let isValid = true;


    if (nombre === "") {
      isValid = false;
      document.getElementById('errorNombre').innerText = "Por favor, ingrese un nombre.";
      document.getElementById('errorNombre').style.display = "block";
    } else {
      document.getElementById('errorNombre').style.display = "none";
    }


    if (comensales === "" || comensales <= 0) {
      isValid = false;
      document.getElementById('errorComensales').innerText = "Ingrese un número válido de comensales.";
      document.getElementById('errorComensales').style.display = "block";
    } else {
      document.getElementById('errorComensales').style.display = "none";
    }


    if (fecha === "") {
      isValid = false;
      document.getElementById('errorFecha').innerText = "Por favor, seleccione una fecha.";
      document.getElementById('errorFecha').style.display = "block";
    } else {
      document.getElementById('errorFecha').style.display = "none";
    }


    if (hora === "") {
      isValid = false;
      document.getElementById('errorHora').innerText = "Por favor, seleccione una hora.";
      document.getElementById('errorHora').style.display = "block";
    } else {
      document.getElementById('errorHora').style.display = "none";
    }


    if (isValid) {
      const reservationItem = document.createElement('div');
      reservationItem.classList.add('reservation-item');
      reservationItem.innerHTML = `
        <strong>Nombre:</strong> ${nombre} <br>
        <strong>Comensales:</strong> ${comensales} <br>
        <strong>Fecha:</strong> ${fecha} <br>
        <strong>Hora:</strong> ${hora}
      `;

      document.getElementById('reservationsList').appendChild(reservationItem);
      document.getElementById('reservationForm').reset();
    }
  });