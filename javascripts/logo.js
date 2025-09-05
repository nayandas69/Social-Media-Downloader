// docs/javascripts/logo.js
window.addEventListener("DOMContentLoaded", () => {
    const logoContainer = document.querySelector(".md-header__button.md-logo");
    if (logoContainer) {
        logoContainer.innerHTML = '<span style="font-size: 20px; font-weight: bold;">SMD</span>';
    }
});
