


const THEME_KEY = 'theme';

function setTheme(theme) {
    const isDark = theme === 'dark';
    document.documentElement.classList.toggle('dark', isDark);
    const toggleBtn = document.getElementById('theme-toggle-btn');
    if (toggleBtn) {
        toggleBtn.textContent = isDark ? 'light_mode' : 'dark_mode';
    }
    localStorage.setItem(THEME_KEY, theme);
}

function toggleTheme() {
    const current = localStorage.getItem(THEME_KEY) || 'light';
    setTheme(current === 'dark' ? 'light' : 'dark');
}

window.addEventListener('DOMContentLoaded', () => {
    const stored = localStorage.getItem(THEME_KEY);
    const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
    const initial = stored || (prefersDark ? 'dark' : 'light');
    setTheme(initial);
});


document.body.addEventListener('toggleTheme', toggleTheme);

function toggleMenu(event) {
    const menu = document.getElementById("menue-apps");
    const pageContent = document.getElementById("page-content");
    if (!menu) return;

    const isOpen = menu.classList.contains("active");
    if (isOpen) {
        menu.classList.remove("active");
        pageContent?.classList.remove("not-active");
    } else {
        menu.classList.add("active");
        pageContent?.classList.add("not-active");
    }
}

document.addEventListener("openNavbarMenu", toggleMenu);

const menuOverlay = document.getElementById("menue-apps");
if (menuOverlay) {
    menuOverlay.addEventListener("click", (event) => {
        if (event.target === menuOverlay) {
            menuOverlay.classList.remove("active");
            document.getElementById("page-content")?.classList.remove("not-active");
        }
    });
}



