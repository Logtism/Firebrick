const currentTheme = localStorage.getItem('theme') ? localStorage.getItem('theme') : null;
const navbar = document.getElementById('navbar');


if (currentTheme) {
    document.documentElement.setAttribute('data-theme', currentTheme);

    if (currentTheme === 'dark') {
        
    }
}


function switchThemeDark() {
    document.documentElement.setAttribute('data-theme', 'dark');
    navbar.classList.replace('navbar-light', 'navbar-dark');
    localStorage.setItem('theme', 'dark');
}

function switchThemeLight() {
    document.documentElement.setAttribute('data-theme', 'light');
    navbar.classList.replace('navbar-dark', 'navbar-light');
    localStorage.setItem('theme', 'light'); //this will be set to light
}