// Handle fade-in effect on scroll
document.addEventListener("scroll", function () {
    let sections = document.querySelectorAll(".fade-section");
    sections.forEach((section) => {
        let rect = section.getBoundingClientRect();
        let fadePoint = window.innerHeight * 0.75; // Adjust for earlier fade-in
        if (rect.top < fadePoint) {
            let opacity = (fadePoint - rect.top) / fadePoint;
            section.style.opacity = Math.min(opacity, 1); // Ensure opacity doesn't exceed 1
        }
    });
});

let lastScrollTop = 0;
const navbar = document.getElementById("navbar");
const menuToggle = document.querySelector(".menu-toggle"); // Declare the variable once here
const navList = document.querySelector("nav ul");

// Change navbar background when scrolling up or down
window.addEventListener("scroll", function () {
    let currentScroll = window.scrollY;

    if (currentScroll > lastScrollTop) {
        navbar.classList.add("scrolled");
    } else {
        navbar.classList.remove("scrolled");
    }

    lastScrollTop = currentScroll;
});



// JavaScript for toggling the hamburger menu
document.getElementById("hamburger-toggle").addEventListener("click", function() {
    // Select the menu
    const menu = document.querySelector(".menu");

    // Toggle the 'display' property of the menu
    if (menu.style.display === "block") {
        menu.style.display = "none";  // Hide the menu if it's currently visible
    } else {
        menu.style.display = "block";  // Show the menu if it's currently hidden
    }
});
