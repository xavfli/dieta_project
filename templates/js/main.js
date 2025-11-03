(function ($) {
    "use strict";

    // Spinner
    var spinner = function () {
        setTimeout(function () {
            if ($('#spinner').length > 0) {
                $('#spinner').removeClass('show');
            }
        }, 1);
    };
    spinner();
    
    
    // Initiate the wowjs
    new WOW().init();


    // Fixed Navbar
    $(window).scroll(function () {
        if ($(window).width() < 992) {
            if ($(this).scrollTop() > 45) {
                $('.fixed-top').addClass('bg-white shadow');
            } else {
                $('.fixed-top').removeClass('bg-white shadow');
            }
        } else {
            if ($(this).scrollTop() > 45) {
                $('.fixed-top').addClass('bg-white shadow').css('top', -45);
            } else {
                $('.fixed-top').removeClass('bg-white shadow').css('top', 0);
            }
        }
    });
    
    
    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });


    // Testimonials carousel
    $(".testimonial-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1000,
        margin: 25,
        loop: true,
        center: true,
        dots: false,
        nav: true,
        navText : [
            '<i class="bi bi-chevron-left"></i>',
            '<i class="bi bi-chevron-right"></i>'
        ],
        responsive: {
            0:{
                items:1
            },
            768:{
                items:2
            },
            992:{
                items:3
            }
        }
    });

        // Contact form submit
    $('#contactForm').on('submit', function (e) {
        e.preventDefault();

        const formData = {
            first_name: $('#first_name').val(),
            last_name: $('#last_name').val(),
            phone: $('#phone').val(),
            telegram_profile: $('#telegram_profile').val(),
            message: $('#message').val()
        };

        $.ajax({
            url: "http://127.0.0.1:8000/api/submit/",
            type: "POST",
            data: JSON.stringify(formData),
            contentType: "application/json",
            success: function (response) {
                alert("✅ Ma'lumot yuborildi! Rahmat.");
                $('#contactForm')[0].reset();
            },
            error: function (xhr, status, error) {
                alert("❌ Xatolik: Ma'lumot yuborilmadi.");
                console.error(xhr.responseText);
            }
        });
    });

    
})(jQuery);

