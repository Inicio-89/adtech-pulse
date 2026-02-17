/* main.js — Minimal JavaScript for AdTech Pulse */
/* ============================================== */
/* We keep JavaScript minimal. Most of the work is done by Python on the server.
   This file handles small interactive features on the frontend. */

// Close dropdown menus when clicking outside
document.addEventListener('click', function(event) {
    const dropdowns = document.querySelectorAll('.dropdown-menu');
    dropdowns.forEach(function(menu) {
        if (!menu.parentElement.contains(event.target)) {
            menu.style.display = 'none';
        }
    });
});

// Re-show dropdown on hover (in case it was hidden by click handler)
document.querySelectorAll('.nav-dropdown').forEach(function(dropdown) {
    dropdown.addEventListener('mouseenter', function() {
        this.querySelector('.dropdown-menu').style.display = 'block';
    });
    dropdown.addEventListener('mouseleave', function() {
        this.querySelector('.dropdown-menu').style.display = 'none';
    });
});

console.log('AdTech Pulse loaded.');
