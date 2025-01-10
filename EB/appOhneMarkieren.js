const menu = document.querySelector('#mobile-menu');
const menuLinks = document.querySelector('.navbar_menu');
const navLogo = document.querySelector('#navbar_logo');

// Menü anzeigen
const mobileMenu = () => {
    menu.classList.toggle('is-active');
    menuLinks.classList.toggle('active');
};

menu.addEventListener('click', mobileMenu);



// Close mobile Menu when clicking on a menu item
const hideMobileMenu = () => {
    const menuBars = document.querySelector('.is-active')
    console.log(innerWidth)
    console.log(menuBars)
    if(window.innerWidth <= 960 && menuBars){
        menu.classList.toggle('is-active')
        menuLinks.classList.remove('active')
        console.log(menuBars)
    }
}
    

menuLinks.addEventListener('click', hideMobileMenu)
navLogo.addEventListener('click', hideMobileMenu)