document.addEventListener('DOMContentLoaded', function() {
    cargarResenas();

    document.getElementById('resenaForm').addEventListener('submit', function(e) {
        e.preventDefault();

        const nombre = document.getElementById('nombre').value;
        const usuario = document.getElementById('usuario').value;
        const calificacion = document.getElementById('calificacion').value;
        const comentario = document.getElementById('comentario').value;

        const nuevaResena = {
            nombre,
            usuario,
            calificacion,
            comentario
        };

        guardarResena(nuevaResena);
        document.getElementById('resenaForm').reset();
    });
});

function guardarResena(resena) {
    let resenas = JSON.parse(localStorage.getItem('resenas')) || [];
    resenas.push(resena);
    localStorage.setItem('resenas', JSON.stringify(resenas));
    agregarResenaDOM(resena);
}

function cargarResenas() {
    const resenas = JSON.parse(localStorage.getItem('resenas')) || [];
    resenas.forEach(resena => {
        agregarResenaDOM(resena);
    });
}

function agregarResenaDOM(resena) {
    const nuevaResena = document.createElement('div');
    nuevaResena.classList.add('caja-resenas');

    nuevaResena.innerHTML = `
        <div class="top">
            <div class="perfil">
                <div class="imagen-perfil">
                    <img src="../asset/Perfil_SinFoto.jpg" alt="Imagen de Perfil">
                </div>
                <div class="nombre">
                    <strong>${resena.nombre}</strong>
                    <span>@${resena.usuario}</span>
                </div>
            </div>
            <div class="opiniones"> 
                ${'★'.repeat(resena.calificacion)}${'☆'.repeat(5 - resena.calificacion)}
            </div>
        </div>
        <div class="comentarios">
            <p>${resena.comentario}</p>
        </div>
        <button class="eliminar-btn">Eliminar</button>
    `;

    document.getElementById('contenedorResenas').appendChild(nuevaResena);

    nuevaResena.querySelector('.eliminar-btn').addEventListener('click', function() {
        eliminarResena(resena, nuevaResena);
    });
}

function eliminarResena(resena, reseñaDOM) {
    let resenas = JSON.parse(localStorage.getItem('resenas')) || [];
    resenas = resenas.filter(r => r.nombre !== resena.nombre || r.usuario !== resena.usuario || r.comentario !== resena.comentario);
    localStorage.setItem('resenas', JSON.stringify(resenas));

    reseñaDOM.remove();
}
