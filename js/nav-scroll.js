// nav-scroll.js — Collapse navbar on scroll
// nav-wrapper is the fixed header containing both #site-nav (links) and .site-title
document.addEventListener('DOMContentLoaded', function() {
    var navWrapper = document.getElementById('nav-wrapper');
    if (!navWrapper) return;

    var scrollThreshold = 80;
    var isCollapsed = false;

    function onScroll() {
        var currentScroll = window.pageYOffset || document.documentElement.scrollTop;
        if (currentScroll > scrollThreshold && !isCollapsed) {
            navWrapper.classList.add('collapsed');
            isCollapsed = true;
        } else if (currentScroll <= scrollThreshold && isCollapsed) {
            navWrapper.classList.remove('collapsed');
            isCollapsed = false;
        }
    }

    window.addEventListener('scroll', onScroll, { passive: true });
    // Navbar starts expanded — don't check scroll on load
});