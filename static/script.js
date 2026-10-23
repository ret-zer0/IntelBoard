document.addEventListener("DOMContentLoaded", () => {
    const navLinks = document.querySelectorAll(".nav-link");
    const sections = document.querySelectorAll(".content-section");

    function showSection(sectionName) {
        sections.forEach((section) => {
            section.classList.toggle("hidden", section.id !== sectionName);
        });

        navLinks.forEach((link) => {
            const isActive = link.dataset.section === sectionName;
            link.classList.toggle("active", isActive);
        });
    }

    navLinks.forEach((link) => {
        link.addEventListener("click", () => {
            showSection(link.dataset.section);
        });
    });

    // Show Weather after the city form is submitted.
    if (document.body.dataset.weatherSubmitted === "true") {
        document.querySelector('[data-section="weather"]').click();
    }
    else {
        showSection("news");
    }
});