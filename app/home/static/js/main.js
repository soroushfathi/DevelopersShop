jQuery(document).ready(function($) {
    "use strict";
    // Ajax search
    $('.ajax-search input[type="text"]').on('blur',function(){
        $('.list-product-search').removeClass('active');
    });
    $('.ajax-search input[type="text"]').on('keydown',function(){
        if($(this).val()==""){
            $('.list-product-search').removeClass('active');
        }else{
            $('.list-product-search').addClass('active');
        }
    });
    // close quickview
    
    $(".quickview-close").on("click", function() {
        $('.quickview-wrapper').hide();
        $('.quickview-wrapper').removeClass('open');
        $('.quick-modal').removeClass('show');
    });
    // open Vertical menu 
    $(".js-vertical-menu").on("click", function() {
        $('.vertical-wrapper').slideToggle(200);
        $(this).toggleClass('active');
    });
    //menu change icon and dropdown
    $(".icon-mobile").on("click", function() {
        $(this).toggleClass('active');
    });
    //menu change icon and dropdown
    $(".js-menubar li .js-plus-icon").on("click", function() {
        $(this).toggleClass('minus');
        $(this).parent().find(".dropdown-menu").slideToggle(function() {
            $(this).next().stop(true).toggleClass('open', $(this).is(":visible"));
        });
    });

    $(".js-filter-menu li .js-plus-icon").on("click", function() {
        $(this).toggleClass('minus');
        $(this).parent().find(".filter-menu").slideToggle(function() {
            $(this).next().stop(true).toggleClass('open', $(this).is(":visible"));
        });
    });

    $(".filter .js-drop").on("click", function() {
        $(this).parent().find(".ion-ios-arrow-down").toggleClass('ion-ios-arrow-up');
        $(this).parent().find("ul").slideToggle(function() {
            $(this).next().stop(true).toggleClass('open', $(this).is(":visible"));
        });
        $(this).parent().find(".sidebar-product-list").slideToggle(function() {
            $(this).next().stop(true).toggleClass('open', $(this).is(":visible"));
        });
    });

    $(".checkout-page .js-drop").on("click", function() {
        $(this).toggleClass('active');

        $(this).parent().find(".filter-content").slideToggle(function() {
            $(this).next().stop(true).toggleClass('open', $(this).is(":visible"));
        });
    });
    // Product detail
    $(".js-close-tab").on("click", function() {
        $(this).removeClass('open')
        $('.detail-content').removeClass('active');
        $('.detail-tab').removeClass('open');

    });
    $('.js-tabs a').on("click", function() {
        $(".js-close-tab").addClass('open');
        $('.detail-tab').addClass('open');
        $('.detail-content').addClass('active');

    })
    if ($('.js-tabs > li').hasClass('active')) {
        $(".js-close-tab").addClass('open');
        $('.detail-tab').addClass('open');
        $('.detail-content').addClass('active');
    }

    // Product Grid
    $(".js-filter-menu li .js-plus-icon").on("click", function() {
        $(".js-filter-menu > li > a").toggleClass('active');
        $(this).toggleClass('minus');
        $(this).parent().find(".filter-menu").slideToggle(function() {
            $(this).next().stop(true).toggleClass('open', $(this).is(":visible"));
        });
    });
    // Open menu dropdown home 5
    $(".js-menubar li .icon-sub-menu").on("click", function() {

        $(this).toggleClass('up-icon');
        $(this).parent().find(".js-open-menu").slideToggle('fast', function() {
            $(this).next().stop(true).toggleClass('open', $(this).is(":visible"));
        });
    });
    // Open menu other page. Header-v2
    $(".js-menu").on("click", function() {
        $(this).toggleClass('active');
        $('.js-open-menu').toggleClass('open');
    });


    // Push menu home 5
    var menuLeft = $('.pushmenu-left');
    var menuHome6 = $('.menu-home5');
    var nav_list = $('.open-cart');
    var nav_click = $('.icon-pushmenu');
    nav_list.on("click", function(event) {
        event.stopPropagation();
        $(this).toggleClass('active');
        $('body').toggleClass('pushmenu-push-toright-cart');
        menuLeft.toggleClass('pushmenu-open');
        $(".container").toggleClass("canvas-container");
    });
    nav_click.on("click", function(event) {
        event.stopPropagation();
        $(this).toggleClass('active');
        $('body').toggleClass('pushmenu-push-toleft');
        menuHome6.toggleClass('pushmenu-open');
    });
    $(".wrappage").on("click", function() {
        $(this).removeClass('active');
        $('body').removeClass('pushmenu-push-toright-cart').removeClass('pushmenu-push-toleft');
        menuLeft.removeClass('pushmenu-open');
        menuHome6.removeClass('pushmenu-open');
    });
    $(".close-left").on("click", function() {
        $(this).removeClass('active');
        $('body').removeClass('pushmenu-push-toright-cart');
        menuLeft.removeClass('pushmenu-open');
    });
    $(".close-left").on("click", function() {
        $('body').removeClass('pushmenu-push-toleft');
        menuHome6.removeClass('pushmenu-open');
    });
    // SHOPPING CART Quantity increment buttons

    var quantitiy = 0;
    $('.js-plus').on("click", function(e) {

        // Stop acting like a button
        e.preventDefault();
        // Get the field name
        var quantity = parseInt($('.js-number').val(), 10);

        // If is not undefined

        $('.js-number').val(quantity + 1);


        // Increment    
    });

    $('.js-minus').on("click", function(e) {
        // Stop acting like a button
        e.preventDefault();
        // Get the field name
        var quantity = parseInt($('.js-number').val(), 10);

        // If is not undefined

        // Increment
        if (quantity > 0) {
            $('.js-number').val(quantity - 1);
        }
    });
    // Js product single slider
    $('.js-click-product').slick({
        slidesToShow: 4,
        slidesToScroll: 1,
        asNavFor: '.js-product-slider',
        dots: false,
        focusOnSelect: true,
        infinite: true,
        arrows: false,
        vertical: true,
        responsive: [

            {
                breakpoint: 1367,
                settings: {
                    vertical: false
                }
            }
        ]
    });
    $('.js-product-slider').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: false,
        asNavFor: '.js-click-product'
    });
    //SHOP LISTING FILTER
    // Price Slider
    if ($('.price-slider').length > 0) {
        $('.price-slider').slider({
            min: 100,
            max: 700,
            step: 10,
            value: [100, 400],


        });
    }
    //SHOP GRID
    $(".view-mode > a").on("click", function() {
        $(this).addClass('active').siblings().removeClass('active');;

        if ($(this).hasClass('col2')) {
            $(".product-grid").addClass("product-grid-v2");
            $(".product-grid").removeClass("product-list");
        }
        if ($(this).hasClass('col')) {
            $(".product-grid").removeClass("product-grid-v2 product-list");
        }
        if ($(this).hasClass('list')) {
            $(".product-grid").addClass("product-list product-grid-v2");
        }
    });
    // Open zipcode
    $(".calculate").on('click', function() {
        $(this).next().slideToggle();
        $(this).toggleClass("active");
    });
    // Checkout : open login box
    $(".js-showlogin").on('click', function() {
        $(".js-openlogin").slideToggle();
        $(this).toggleClass("active");
    });
    // Checkout : open coupon
    $(".js-showcp").on('click', function() {
        $(".js-opencp").slideToggle();
        $(this).toggleClass("active");

    });
    //Open filter menu mobile
    $('.filter-collection-left > a').on('click', function() {
        $('.wrappage').addClass('show-filter');
    });
    $(document).bind("mouseup touchend", function(e) {
        var container = jQuery("#filter-sidebar");
        if (!container.is(e.target) // if the target of the click isn't the container...
            &&
            container.has(e.target).length === 0) // ... nor a descendant of the container
        {
            $('.wrappage').removeClass('show-filter');
        }
    });
    $('.close-sidebar-collection').click(function() {
        $('.wrappage').removeClass('show-filter');
    });

    // Scroll slider

    $('.scroll-down').on('click', function() {
        $('html, body').animate({ scrollTop: $('section#main-content').offset().top }, 'slow');
        return false;
    });
    // Scroll to TOP
    $(window).scroll(function() {
        if ($(this).scrollTop() > 100) {
            $('.scroll_top').fadeIn();
        } else {
            $('.scroll_top').fadeOut();
        }
    });

    $('.scroll_top').on('click', function() {
        $("html, body").animate({
            scrollTop: 0
        }, 600);
        return false;
    });
    $(window).scroll(function() {
        var scroll = $(window).scrollTop();

        if (scroll > 500) {
            $(".intro").hide();
            $(".scroll_down").hide();
        }
    });
    // scroll down
    $(".scroll_down").on('click', function(e) {
        e.preventDefault();
        $(".intro").hide();
        $(this).hide();
        return false;
    });

    // owl category
    $('.js-owl-cate').owlCarousel({
        margin: 30,
        autoplay: false,
        autoplayTimeout: 3000,
        loop: true,
        dots: false,
        nav: true,
        navText: ["<span class='fa fa-angle-right'></span>", "<span class='fa fa-angle-left'></span>"],
        responsive: {
            0: {
                items: 1
            },
            480: {
                items: 2
            },
            1024: {
                items: 3,

            },
            1200: {
                items: 4,
                nav: false,
                dots:true
            },
            1600: {
                items: 4,
                margin: 40,
                nav: false,
                dots:true
            }
        }
    });
    $('.js-owl-team').owlCarousel({
        margin: 30,
        autoplay: false,
        autoplayTimeout: 3000,
        loop: true,
        dots: false,
        nav: true,
        navText: ["<span class='fa fa-angle-right'></span>", "<span class='fa fa-angle-left'></span>"],
        responsive: {
            0: {
                items: 1
            },
            480: {
                items: 2
            },
            1024: {
                items: 3
            },
            1200: {
                items: 4,
                margin: 40
            }
        }
    });
    $('.js-owl-cate2').owlCarousel({
        margin: 30,
        autoplay: false,
        autoplayTimeout: 3000,
        loop: true,
        dots: true,
        nav: false,
        responsive: {
            0: {
                items: 1
            },
            480: {
                items: 2
            },
            1024: {
                items: 3
            },
            1200: {
                items: 3
            },
            1600: {
                items: 3,
                margin: 40
            }
        }
    });


    // owl brand
    $('.js-owl-brand').owlCarousel({
        margin: 30,
        autoplay: false,
        autoplayTimeout: 3000,
        loop: true,
        dots: false,
        nav: true,
        navText: ["<span class='fa fa-angle-right'></span>", "<span class='fa fa-angle-left'></span>"],
        responsive: {
            0: {
                items: 1
            },
            480: {
                items: 3
            },
            1024: {
                items: 5
            },
            1200: {
                items: 7
            }
        }
    });
    $('.js-owl-brand2').owlCarousel({
        margin: 30,
        autoplay: false,
        autoplayTimeout: 3000,
        loop: true,
        dots: false,
        nav: true,
        navText: ["<span class='fa fa-angle-right'></span>", "<span class='fa fa-angle-left'></span>"],
        responsive: {
            0: {
                items: 1
            },
            480: {
                items: 3
            },
            1024: {
                items: 4
            },
            1200: {
                items: 6
            }
        }
    });
    $(".js-owl-brand2 .owl-nav > div").on("click", function() {
        $(this).addClass('active').siblings().removeClass('active');
    });
    // product carousel
    $('.js-owl-product').owlCarousel({
        margin: 30,
        autoplay: true,
        autoplayTimeout: 3000,
        loop: true,
        dots: false,
        nav: true,
        navText: ["<span class='fa fa-angle-left'></span>", "<span class='fa fa-angle-right'></span>"],
        responsive: {
            0: {
                items: 1
            },
            480: {
                items: 2
            },
            1024: {
                items: 2
            },
            1200: {
                items: 3
            }
        }
    });
    $('.js-owl-product2').owlCarousel({

        margin: 30,
        autoplay: false,
        autoplayTimeout: 3000,
        loop: true,
        dots: false,
        nav: true,
        navText: ["<span class='fa fa-angle-right'></span>", "<span class='fa fa-angle-left'></span>"],
        responsive: {
            0: {
                items: 1
            },
            480: {
                items: 2
            },
            1200: {
                items: 3
            },
            1600: {
                items: 3,
                margin: 40
            }
        }
    });
    $(".js-owl-product2 .owl-nav > div").on("click", function() {
        $(this).addClass('active').siblings().removeClass('active');
    });
    $('.js-owl-blog').owlCarousel({

        margin: 30,
        autoplay: false,
        autoplayTimeout: 3000,
        loop: true,
        dots: true,
        nav: true,
        navText: ["<span class='fa fa-angle-right'></span>", "<span class='fa fa-angle-left'></span>"],
        responsive: {
            0: {
                items: 1
            },
            480: {
                items: 2
            },
            1200: {
                items: 3
            },
            1600: {
                items: 3,
                margin: 40
            }
        }
    });
    $(".js-owl-blog .owl-nav > div").on("click", function() {
        $(this).addClass('active').siblings().removeClass('active');
    });
    $(".js-quickview-slide  .slick-arrow").on("click", function() {
        $(this).addClass('active');
    });
    $('.js-owl-post').owlCarousel({
        nav: true,
        navText: ["<span class='fa fa-angle-right'></span>", "<span class='fa fa-angle-left'></span>"],
        items: 1,
        dots: false
    });
    $('.js-owl-quote').owlCarousel({
        nav: false,
        items: 1,
        dots: true,
        singleItem: true,
    });
    $('.js-oneitem').owlCarousel({
        nav: false,
        items: 1,
        dots: true,
        singleItem: true,
    });
    $('.js-oneitem2').owlCarousel({
        nav: false,
        items: 1,
        singleItem: true,
        dots         : true,
    });
    // Instagram carousel
    $('.js-owl-instagram').owlCarousel({
        margin: 0,
        autoplay: true,
        autoplayTimeout: 3000,
        loop: true,
        nav: false,
        navText: ["", ""],
        dots: false,
        responsive: {
            0: {
                items: 1
            },
            480: {
                items: 2
            },
            1000: {
                items: 5
            }
        }
    });

    $('.js-multiple-row2').slick({
        dots: true,
        arrows: false,
        slidesPerRow: 4,
        rows: 2,
        responsive: [{
                breakpoint: 1025,
                settings: {
                    slidesPerRow: 3,
                }
            },
            {
                breakpoint: 813,
                settings: {
                    slidesPerRow: 2,
                }
            },
            {
                breakpoint: 480,
                settings: {
                    arrows: true,
                    prevArrow: '<span class="prev"><i class="fa fa-angle-right" aria-hidden="true"></i></span>',
                    nextArrow: '<span class="next"><i class="fa fa-angle-left" aria-hidden="true"></i></span>',
                    infinite: true,
                    dots: false,
                    slidesPerRow: 1,
                    rows: 1,
                }
            }
        ]
    });

    $('.js-multiple-row').slick({
        dots: true,
        arrows: false,
        slidesPerRow: 3,
        rows: 2,
        responsive: [{
                breakpoint: 1025,
                settings: {
                    slidesPerRow: 3,
                }
            },
            {
                breakpoint: 813,
                settings: {
                    slidesPerRow: 2,
                }
            },
            {
                breakpoint: 480,
                settings: {
                    arrows: true,
                    prevArrow: '<span class="prev"><i class="fa fa-angle-right" aria-hidden="true"></i></span>',
                    nextArrow: '<span class="next"><i class="fa fa-angle-left" aria-hidden="true"></i></span>',
                    infinite: true,
                    dots: false,
                    slidesPerRow: 1,
                    rows: 1,
                }
            }
        ]
    });
    $('.js-multiple-row3').slick({
        dots: true,
        arrows: false,
        slidesPerRow: 2,
        rows: 2,
        responsive: [{
                breakpoint: 1025,
                settings: {
                    slidesPerRow: 2,
                }
            },
            {
                breakpoint: 813,
                settings: {
                    slidesPerRow: 1,
                }
            },
            {
                breakpoint: 480,
                settings: {
                    arrows: true,
                    prevArrow: '<span class="prev"><i class="fa fa-angle-right" aria-hidden="true"></i></span>',
                    nextArrow: '<span class="next"><i class="fa fa-angle-left" aria-hidden="true"></i></span>',
                    infinite: true,
                    dots: false,
                    slidesPerRow: 1,
                    rows: 1,
                }
            }
        ]
    });




    // js slick one item homepage 3

    // Slider collectiion full
    var $status = $('.pagingInfo');
    var $slickElement = $('.js-slider-collectionf');
    $slickElement.on('init reInit afterChange', function(event, slick, currentSlide, nextSlide) {
        //currentSlide is undefined on init -- set it to 0 in this case (currentSlide is 0 based)
        var i = (currentSlide ? currentSlide : 0) + 1;
        $status.text('0' + i);
    });
    $('.js-slider-collectionf').on('afterChange', function(event, slick, currentSlide) {
        $('.slick-active').append('<div class="pagingInfo"');
    });
    $('.js-slider-collectionf').slick({
        autoplay: true,
        dots: true,
        // centerMode: true,
        infinite: true,
        // centerMode: true,
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: false,
        appendDots: $('.post-fade'),
        dotsClass: 'custom_paging',
        customPaging: function(slider, i) {
            var thumb = $(slider.$slides[i]).data();
            return '<a class="dots"></a>';
        },

    });

    // Slider collectiion full
    var $status = $('.pagingInfo');
    var $slickElement = $('.js-slider-home4');
    $slickElement.on('init reInit afterChange', function(event, slick, currentSlide, nextSlide) {
        //currentSlide is undefined on init -- set it to 0 in this case (currentSlide is 0 based)
        var i = (currentSlide ? currentSlide : 0) + 1;
        $status.text('0' + i);
    });
    $('.js-slider-home4').on('afterChange', function(event, slick, currentSlide) {
        $('.slick-active').append('<div class="pagingInfo"');
    });
    $('.js-slider-home4').slick({
        autoplay: true,
        dots: true,
        infinite: true,
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: false,
        appendDots: $('.post-fade'),
        dotsClass: 'custom_paging',
        customPaging: function(slider, i) {
            var thumb = $(slider.$slides[i]).data();
            return '<a class="dots"></a>';
        },
    });
    // Slider collection detail
    $('.js-slider-collectiond').slick({
        autoplay: true,
        dots: true,
        infinite: true,
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: false,
        appendDots: $('.post-fade'),
        dotsClass: 'custom_paging',
        customPaging: function(slider, i) {
            var thumb = $(slider.$slides[i]).data();
            return '<a class="dots"></a>';
        },

    });
    //  Show more

    // slider home 3 and home 2
    $('.js-slider-3items').slick({
        autoplay: false,
        infinite: false,
        arrows: false,
        dots: true
    });
    // js blogpost
    $('.js-single-post').slick({
        autoplay: false,
        slidesToShow: 1,
        slidesToScroll: 1,
        infinite: true,
        arrows:false,
        dots: true
    });
    // js quickview
    $('.js-quickview-slide').slick({
        autoplay: false,
        slidesToShow: 1,
        slidesToScroll: 1,
        infinite: true,
        arrows: true,
        prevArrow: '<span class="prev"><i class="fa fa-angle-right" aria-hidden="true"></i></span>',
        nextArrow: '<span class="next"><i class="fa fa-angle-left" aria-hidden="true"></i></span>',
        dots: true
    });
    // slider home 1
    $('.js-slider-home2').slick({
        autoplay: false,
        slidesToShow: 1,
        slidesToScroll: 1,
        infinite: false,
        arrows: true,
        prevArrow: '<span class="prev"><i class="fa fa-angle-right" aria-hidden="true"></i></span>',
        nextArrow: '<span class="next"><i class="fa fa-angle-left" aria-hidden="true"></i></span>',
    });

    // JS owl team Carousel 
    $('.js-owl-test').owlCarousel({
        items: 1,
        singleItem: true,
        nav: true,
        navText: ["<span class='fa fa-angle-right'></span>", "<span class='fa fa-angle-left'></span>"],
        dots: false,
    });
    // Scroll slide homepage 2

    $('.slide-scroll').on('click', function() {
        $('html, body').animate({ scrollTop: $('section#contenthome2').offset().top }, 'slow');
        return false;
    });
    var handleScrollTop = function(e) {
        e.preventDefault();
        $('html, body').animate({ scrollTop: 0 }, 250);
    };
    // Footer to top
    $('footer > .scroll-top').on('click', function(e) {
        handleScrollTop(e);
    });

    $('.backto.vow-top').on('click', function(e) {
        handleScrollTop(e);
    });
    // Read more
    $(function() {
        var $header = $('.entry-content');
        var $half = parseInt($(".img-cal").height()) / 2;
        var $window = $(window).on('resize', function() {
            var height = $header.height() - $half;
            $header.height(height);
        }).trigger('resize'); //on page load


    });
    $(function() {

        var $el, $ps, $up, $p, totalHeight;

        $(".entry-content .btn-show").click(function() {

            // IE 7 doesn't even get this far. I didn't feel like dicking with it.

            totalHeight = 0

            $el = $(this);
            $p = $el.parent();
            $up = $p.parent();
            $ps = $up.find(".e-text");

            // measure how tall inside should be by adding together heights of all inside paragraphs (except read-more paragraph)
            $ps.each(function() {
                totalHeight += $(this).outerHeight();
                // FAIL totalHeight += $(this).css("margin-bottom");
            });

            $up
                .css({
                    // Set height to prevent instant jumpdown when max height is removed
                    "height": $up.height(),
                    "max-height": 9999,
                    "margin-bottom": 30
                })
                .animate({
                    "height": totalHeight
                });

            // fade out read-more
            $up.removeClass('active');
            $p.fadeOut();

            // prevent jump-down
            return false;

        });

    });
});