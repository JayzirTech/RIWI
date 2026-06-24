const navLinks = document.querySelectorAll('nav a[href^="#"]');
const backToTopButton = document.getElementById("GoToTop");
const sideMenu = document.getElementById("sideMenu");

navLinks.forEach(link => {
    link.addEventListener('click', function (e) {
        e.preventDefault();

        const targetId = this.getAttribute('href');
        const targetSection = document.querySelector(targetId);

        if (targetSection) {
            targetSection.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

window.onscroll = function () {
    const scrollPos = document.body.scrollTop > 300 || document.documentElement.scrollTop > 300;

    if (scrollPos) {
        sideMenu.classList.add("visible");
        backToTopButton.classList.add("visible");
    } else {
        sideMenu.classList.remove("visible");
        backToTopButton.classList.remove("visible");
    }
};

backToTopButton.addEventListener("click", function () {
    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });
});