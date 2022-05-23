$(document).ready(function() {
    // menu [desktop]
    const navbar = $('.navbar-expand-lg');
    const logo = $('.brand-home');

    const animateNavbar = () => {
        if ($(this).scrollTop() > 120) {
            navbar.removeClass('pt-4').addClass('bg-white shadow-sm');
            logo.css('opacity', '1');
        }
        if ($(this).scrollTop() < 120) {
            navbar.removeClass('bg-white shadow-sm').addClass('pt-4');
            logo.css('opacity', '0');
        }
    }

    if ($(window).innerWidth() > 991) {
        // at the beginning
        animateNavbar();

        // when scroll
        $(window).scroll(function () {
            animateNavbar();
        })
    }

    $('#goBack').click(() => {
        window.history.back();
    });
});