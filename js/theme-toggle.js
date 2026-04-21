// theme-toggle.js — Alternância de tema claro/escuro
// Respeita preferência do sistema e salva no localStorage
(function() {
    const THEME_KEY = 'theme';
    const DARK = '/css/dark-theme.css';
    const LIGHT = '/css/light-theme.css';

    function getPreferredTheme() {
        const stored = localStorage.getItem(THEME_KEY);
        if (stored === 'light' || stored === 'dark') return stored;
        return window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark';
    }

    function applyTheme(theme) {
        const link = document.getElementById('theme-css');
        if (!link) return;
        link.href = theme === 'light' ? LIGHT : DARK;
        localStorage.setItem(THEME_KEY, theme);
        updateIcon(theme);
    }

    function updateIcon(theme) {
        const btn = document.getElementById('theme-selector');
        if (!btn) return;
        btn.innerHTML = theme === 'light'
            ? '<i class="fa-solid fa-sun"></i>'
            : '<i class="fa-solid fa-moon"></i>';
        btn.setAttribute('aria-label',
            theme === 'light' ? 'Mudar para tema escuro' : 'Mudar para tema claro');
    }

    function toggleTheme() {
        const current = getPreferredTheme();
        applyTheme(current === 'dark' ? 'light' : 'dark');
    }

    // Expor globalmente pro onclick inline
    window.toggleTheme = toggleTheme;

    // Aplicar tema na carga da página (antes do paint pra evitar flash)
    applyTheme(getPreferredTheme());

    // Escutar mudança de preferência do sistema
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', function(e) {
        if (!localStorage.getItem(THEME_KEY)) {
            applyTheme(e.matches ? 'dark' : 'light');
        }
    });
})();