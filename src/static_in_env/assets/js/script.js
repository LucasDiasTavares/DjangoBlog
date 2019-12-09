const responsive = {
    // breakpoint from 0 up
    0: {
        items: 1,
        nav: false
    },
    // breakpoint from 560 up
    560: {
        items: 2
    },
    // breakpoint from 960 up
    960: {
        items: 3
    },
    // breakpoint from 1200 up
    1200: {
        items: 4
    }
}

$(document).ready(function () {
    $nav = $('.nav');

    $('.toggle-collapse').click(function () {
        $nav.toggleClass('collapse');
    })
    /* Owl Carousel Section */
    $('.owl-carousel').owlCarousel({
        loop: true,
        autoplay: false,
        autoplayTimeout: 3000,
        nav: true,
        navText: ['<i class="fas fa-long-arrow-alt-left"></i>', '<i class="fas fa-long-arrow-alt-right"></i>'],
        responsive: responsive
    });

    /* back to top btn */

    const toTop = document.querySelector(".back-to-top-btn");

    window.addEventListener("scroll", () => {
        if (window.pageYOffset > 100) {
            toTop.classList.add("active");
        }
        else {
            toTop.classList.remove("active");
        }
    })

});