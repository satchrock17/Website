const menu = document.querySelector('#mobile-menu');
const menuLinks = document.querySelector('.navbar_menu');
const navLogo = document.querySelector('#navbar_logo');

// Menü anzeigen
const mobileMenu = () => {
    menu.classList.toggle('is-active');
    menuLinks.classList.toggle('active');
};

menu.addEventListener('click', mobileMenu);

// Show active menu when scrolling
const highlightMenu = () => {
    const elem = document.querySelector('.highlight')
    const homeMenu = document.querySelector('#home-page')
    const aboutMenu = document.querySelector('#about-page')
    const project = document.querySelector('#projekte-page')
    let scrollPos = window.scrollY
    // console.log(scrollPos)

    // adds 'highlight' class to my menu items
    if(window.innerWidth > 960 && scrollPos < 600){
        homeMenu.classList.add('highlight')
        aboutMenu.classList.remove('highlight')
        return
    } else if(window.innerWidth > 960 && scrollPos < 1400){
        aboutMenu.classList.add('highlight')
        homeMenu.classList.remove('highlight')
        project.classList.remove('highlight')
        return
    } else if(window.innerWidth > 960 && scrollPos < 2345){
        project.classList.add('highlight')
        aboutMenu.classList.remove('highlight')
        return
    }

    if(elem && window.innerWidth < 960 && scrollPos < 600 || elem){
        elem.classList.remove('highlight')
    }
}

window.addEventListener('scroll', highlightMenu)
window.addEventListener('click', highlightMenu)

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