const date = new Date()
document.getElementById("year").innerText = date.getFullYear()

// Write your Js code here 

const navLinks = document.querySelectorAll('.nav__list a[href^="#"]');
const backToTopButton = document.getElementById("GoToTop");

const sideMenu = document.querySelector(".nav"); 
const menuToggle = document.querySelector(".menu-toggle");

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
    const scrollPos = document.documentElement.scrollTop > 300 || document.body.scrollTop > 300;

    if (backToTopButton) {
        if (scrollPos) {
            backToTopButton.style.display = "block";
        } else {
            backToTopButton.style.display = "none";
        }
    }
};

if (backToTopButton) {
    backToTopButton.addEventListener("click", function () {
        window.scrollTo({
            top: 0,
            behavior: "smooth"
        });
    });
}

if (menuToggle) {
    menuToggle.addEventListener("click", () => {
        sideMenu.classList.toggle("nav--active");
    });
}



