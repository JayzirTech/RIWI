const menuBtn = document.getElementById('menuBtn');
const navOptions = document.getElementById('navOptions');
const internalLinks = document.querySelectorAll('a[href^="#"]');

menuBtn.addEventListener('click', () => {
    // La función toggle añade la clase si no está, y la quita si está.
    navOptions.classList.toggle('show');
    menuBtn.classList.toggle('active'); // Activa la animación del icono
});

// Función centralizada para cerrar el menú y resetear el botón
const closeMenu = () => {
    navOptions.classList.remove('show');
    menuBtn.classList.remove('active');
};

// Detectar el evento de scroll en la ventana
window.addEventListener('scroll', () => {
    // Si el menú tiene la clase 'show', se la quitamos
    if (navOptions.classList.contains('show')) {
        closeMenu();
    }
});

// NAVEGACIÓN INTELIGENTE (Smooth Scroll + No Historial)
internalLinks.forEach(link => {
    link.addEventListener('click', (e) => {
        // Detenemos el comportamiento nativo que recarga y crea historial
        e.preventDefault();

        const targetId = link.getAttribute('href');
        const targetElement = document.querySelector(targetId);

        if (targetElement) {
            // Desplazamiento suave manual
            targetElement.scrollIntoView({
                behavior: 'smooth'
            });

            // Cerramos el menú para limpiar la vista en móvil
            closeMenu();
            
            // Cambiamos la URL visualmente sin ensuciar el historial de "atrás"
            window.history.replaceState(null, null, targetId);
        }
    });
});