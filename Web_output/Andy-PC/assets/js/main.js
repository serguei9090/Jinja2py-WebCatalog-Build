/**
 * owl Carousel initialization
 */
$(document).ready(function() {
    var itemSlider = $('#owl-carousel');
    itemSlider.owlCarousel(
    {
    items:3,
    nav: true,
    navText: [
        '<i class="fa fa-angle-left" aria-hidden="true"></i>',
        '<i class="fa fa-angle-right" aria-hidden="true"></i>'
    ],
    autoplay:3000,
    autoplayHoverPause:true,
    loop:true,
    smartSpeed:1200,
    dots:true,
    margin:5,
    responsive:
    {
        0:{items:1,nav:false},
        450:{nav:false},
        768:{items:2},
        992:{items:3}
    }
    });
});

/**
 * page map
 */

var coordenadas=$("#mapAltLog").text();
var nombre_map=$("#mapName").text();
var direccion_map=$("#mapDireccion").text();
var telefono_map=$("#mapTelefono").text();
var mymap = L.map('map').setView([22.146051, -80.448427], 13);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(mymap);
// ===================================MapBox=======================
// L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
//     attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
//     maxZoom: 18,
//     id: 'mapbox/streets-v11',
//     tileSize: 512,
//     zoomOffset: -1,
//     accessToken: 'pk.eyJ1Ijoic2VyZ3VlaTkwOTAiLCJhIjoiY2syb3p1aGo5MTlhZTNucG5jZThqd2J0ZiJ9.LNEViu85CsodDft8O65LOw'
// }).addTo(mymap);
$('#map').on()
L.marker([22.146051, -80.448427]).addTo(mymap)
    .bindPopup(nombre_map + '.<br>' + direccion_map + '.<br>' + telefono_map + '.')
    .openPopup();


/**
 * Carousel random put info
 */
$(document).ready(function() {
        //	declare variables
        var div_item_n = []
        var img_path = []
        var caroucel_items = []
        var n = 0
            //	getting data from item list
            //	getting items list
        var container = document.querySelector('#myItems');
        //	making array of items
        var matches_button = container.querySelectorAll('li>button');
        var matches_img = container.querySelectorAll('div.card > img');
        //	making array id from div
        $.each(matches_button, function(ind, elem) {
                div_item_n.push($(elem).attr("data-target"))
            })
            //	making array src path from item
        $.each(matches_img, function(ind, elem) {
                img_path.push(elem.src)
            })
            //	carousel insert data
            //	getting carousel list
        var container_carosuels = document.querySelector('.owl-carousel');
        //	making array of items for buttom target and Img source
        var matches_img_carousels = container_carosuels.querySelectorAll('button.carousel_modal > img');
        var matches_d_target_carousels = container_carosuels.querySelectorAll('button.carousel_modal');
        //	put random source to carousel src
        $.each(matches_img_carousels, function(ind, elem) {
            var r_number = Math.floor(Math.random() * img_path.length);
            $(elem).attr('src', img_path[r_number])
            $(matches_d_target_carousels[n]).attr('data-target', div_item_n[r_number])
            n += 1
        })
    })
    /**
     * Pagination and search
     */
$(document).ready(function() {
    // scroll down
    $("body").animate({
        scrollTop: $(document).height()
    }, 9000)
});

$(function() {

    var flexiblePagination = $('#myItems').flexiblePagination({
        itemsPerPage: 12,
        itemSelector: 'div.result:visible',
        pagingControlsContainer: '#pagingControls',
        showingInfoSelector: '#showingInfo',

        css: {
            btnNumberingClass: 'btn btn-outline-primary',
            btnActiveClass: "btn btn-primary",
            btnFirstClass: 'btn btn-outline-primary',
            btnLastClass: 'btn btn-outline-primary',
            btnNextClass: 'btn btn-outline-primary',
            btnPreviousClass: 'btn btn-outline-primary',
        }
    });

    flexiblePagination.getController().onPageClick = function(pageNum, e) {
        console.log('You Clicked Page: ' + pageNum)
        $('html, body').animate({ scrollTop: 200 }, 'smooth');
    };


});





/**
 * Template Name: OnePage - v2.1.0
 * Template URL: https://bootstrapmade.com/onepage-multipurpose-bootstrap-template/
 * Author: BootstrapMade.com
 * License: https://bootstrapmade.com/license/
 */
!(function($) {
    "use strict";

    // Preloader
    $(window).on('load', function() {
        if ($('#preloader').length) {
            $('#preloader').delay(100).fadeOut('slow', function() {
                $(this).remove();
            });
        }
    });

    // Smooth scroll for the navigation menu and links with .scrollto classes
    var scrolltoOffset = $('#header').outerHeight() - 2;
    $(document).on('click', '.nav-menu a, .mobile-nav a, .scrollto', function(e) {
        if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
            var target = $(this.hash);
            if (target.length) {
                e.preventDefault();

                var scrollto = target.offset().top - scrolltoOffset;

                if ($(this).attr("href") == '#header') {
                    scrollto = 0;
                }

                $('html, body').animate({
                    scrollTop: scrollto
                }, 1500, 'easeInOutExpo');

                if ($(this).parents('.nav-menu, .mobile-nav').length) {
                    $('.nav-menu .active, .mobile-nav .active').removeClass('active');
                    $(this).closest('li').addClass('active');
                }

                if ($('body').hasClass('mobile-nav-active')) {
                    $('body').removeClass('mobile-nav-active');
                    $('.mobile-nav-toggle i').toggleClass('icofont-navigation-menu icofont-close');
                    $('.mobile-nav-overly').fadeOut();
                }
                return false;
            }
        }
    });

    // Activate smooth scroll on page load with hash links in the url
    $(document).ready(function() {
        if (window.location.hash) {
            var initial_nav = window.location.hash;
            if ($(initial_nav).length) {
                var scrollto = $(initial_nav).offset().top - scrolltoOffset;
                $('html, body').animate({
                    scrollTop: scrollto
                }, 1500, 'easeInOutExpo');
            }
        }
    });

    // Mobile Navigation
    if ($('.nav-menu').length) {
        var $mobile_nav = $('.nav-menu').clone().prop({
            class: 'mobile-nav d-lg-none'
        });
        $('body').append($mobile_nav);
        $('body').prepend('<button type="button" class="mobile-nav-toggle d-lg-none"><i class="icofont-navigation-menu"></i></button>');
        $('body').append('<div class="mobile-nav-overly"></div>');

        $(document).on('click', '.mobile-nav-toggle', function(e) {
            $('body').toggleClass('mobile-nav-active');
            $('.mobile-nav-toggle i').toggleClass('icofont-navigation-menu icofont-close');
            $('.mobile-nav-overly').toggle();
        });

        $(document).on('click', '.mobile-nav .drop-down > a', function(e) {
            e.preventDefault();
            $(this).next().slideToggle(300);
            $(this).parent().toggleClass('active');
        });

        $(document).click(function(e) {
            var container = $(".mobile-nav, .mobile-nav-toggle");
            if (!container.is(e.target) && container.has(e.target).length === 0) {
                if ($('body').hasClass('mobile-nav-active')) {
                    $('body').removeClass('mobile-nav-active');
                    $('.mobile-nav-toggle i').toggleClass('icofont-navigation-menu icofont-close');
                    $('.mobile-nav-overly').fadeOut();
                }
            }
        });
    } else if ($(".mobile-nav, .mobile-nav-toggle").length) {
        $(".mobile-nav, .mobile-nav-toggle").hide();
    }

    // Navigation active state on scroll
    var nav_sections = $('section');
    var main_nav = $('.nav-menu, #mobile-nav');

    $(window).on('scroll', function() {
        var cur_pos = $(this).scrollTop() + 200;

        nav_sections.each(function() {
            var top = $(this).offset().top,
                bottom = top + $(this).outerHeight();

            if (cur_pos >= top && cur_pos <= bottom) {
                if (cur_pos <= bottom) {
                    main_nav.find('li').removeClass('active');
                }
                main_nav.find('a[href="#' + $(this).attr('id') + '"]').parent('li').addClass('active');
            }
            if (cur_pos < 300) {
                $(".nav-menu ul:first li:first").addClass('active');
            }
        });
    });

    // Toggle .header-scrolled class to #header when page is scrolled
    $(window).scroll(function() {
        if ($(this).scrollTop() > 100) {
            $('#header').addClass('header-scrolled');
        } else {
            $('#header').removeClass('header-scrolled');
        }
    });

    if ($(window).scrollTop() > 100) {
        $('#header').addClass('header-scrolled');
    }

    // Back to top button
    $(window).scroll(function() {
        if ($(this).scrollTop() > 100) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });

    $('.back-to-top').click(function() {
        $('html, body').animate({
            scrollTop: 0
        }, 1500, 'easeInOutExpo');
        return false;
    });

    // jQuery counterUp
    $('[data-toggle="counter-up"]').counterUp({
        delay: 10,
        time: 1000
    });

    // Testimonials carousel (uses the Owl Carousel library)
    $(".testimonials-carousel").owlCarousel({
        autoplay: true,
        dots: true,
        loop: true,
        responsive: {
            0: {
                items: 1
            },
            768: {
                items: 2
            },
            900: {
                items: 3
            }
        }
    });

    // Porfolio isotope and filter
    $(window).on('load', function() {
        var portfolioIsotope = $('.portfolio-container').isotope({
            itemSelector: '.portfolio-item'
        });

        $('#portfolio-flters li').on('click', function() {
            $("#portfolio-flters li").removeClass('filter-active');
            $(this).addClass('filter-active');

            portfolioIsotope.isotope({
                filter: $(this).data('filter')
            });
            aos_init();
        });

        // Initiate venobox (lightbox feature used in portofilo)
        $(document).ready(function() {
            $('.venobox').venobox({
                'share': false
            });
        });
    });

    // Portfolio details carousel
    $(".portfolio-details-carousel").owlCarousel({
        autoplay: true,
        dots: true,
        loop: true,
        items: 1
    });

    // Init AOS
    function aos_init() {
        AOS.init({
            duration: 1000,
            once: true
        });
    }
    $(window).on('load', function() {
        aos_init();
    });

})(jQuery);