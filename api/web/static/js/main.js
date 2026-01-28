// Menú burger responsive
document.addEventListener('DOMContentLoaded', () => {
    const burger = document.querySelector('.navbar-burger');
    if (burger) {
        const menu = document.getElementById(burger.dataset.target);
        burger.addEventListener('click', () => {
            burger.classList.toggle('is-active');
            menu.classList.toggle('is-active');
        });
    }
});

// Cerrar sesión
function cerrarSesion() {
    var requestOptions = {
        method: 'POST',
        headers: myHeaders
    };
    fetch("/api/usuarios/logout", requestOptions)
        .then(response => response.json())
        .then(result => {
            if (result.status == "OK") {
                localStorage.removeItem("token")
                myHeaders.delete("Authorization");
                location.href = "index.html";
            } else {
                alert("No se ha podido cerrar sesión")
            }
        })
        .catch(error => {
            console.log('error', error);
            alert("Se ha producido un error y no se ha podido cerrar sesión")
        });

}
