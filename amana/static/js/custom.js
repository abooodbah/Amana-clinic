
(function($) {
    // 'use strict';

    // Main Navigation
    $( '.hamburger-menu' ).on( 'click', function() {
        $(this).toggleClass('open');
        $('.site-navigation').toggleClass('show');
    });

    // Hero Slider
    var mySwiper = new Swiper('.hero-slider', {
        slidesPerView: 1,
        spaceBetween: 0,
        // loop: true,
        pagination: {
            el: '.swiper-pagination',
            clickable: true,
            renderBullet: function (index, className) {
                return '<span class="' + className + '">0' + (index + 1) + '</span>';
            },
        },
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev'
        }
    });

    // Testimonial Slider
    var swiper = new Swiper('.testimonial-slider-wrap', {
        slidesPerView: 1,
        spaceBetween: 0,
        loop: true,
        effect: 'fade',
        speed: 800,
        pagination: {
            el: '.swiper-pagination',
            clickable: true
        }
    });

    // Accordion & Toggle
    $('.accordion-wrap.type-accordion').collapsible({
        accordion: true,
        contentOpen: 0,
        arrowRclass: 'arrow-r',
        arrowDclass: 'arrow-d'
    });

    $('.accordion-wrap .entry-title').on('click', function() {
        $('.accordion-wrap .entry-title').removeClass('active');
        $(this).addClass('active');
    });

    // Tabs
    $(function() {
        $('.tab-content:first-child').show();

        $('li.tab-nav').bind('click', function(e) {
            $this = $(this);
            $tabs = $this.parent().parent().next();
            $target = $($this.data("target"));
            $this.siblings().removeClass('active');
            $target.first().siblings().css("display", "none");
            $this.addClass('active');
            console.log($target.children());
            $target.each(function(){
                $(this).fadeIn("fast")
                $(this).css("display", "flow-root");

            });
        });
        var url_string = window.location.href
        var url = new URL(url_string);
        var param = url.searchParams.get("service");
        console.log(param);
        $('.tab-nav:nth-child(' + param + ')').trigger('click');
    });

    // Circular Progress Bar
    $('#loader_1').circleProgress({
        startAngle: -Math.PI / 4 * 2,
        value: 0.90,
        size: 156,
        thickness: 4,
        fill: {
            gradient: ["#5386e7", "#43a7f0"]
        }
    }).on('circle-animation-progress', function(event, progress) {
        $(this).find('strong').html(Math.round(90 * progress) + '<i>%</i>');
    });

    $('#loader_2').circleProgress({
        startAngle: -Math.PI / 4 * 2,
        value: 0.65,
        size: 156,
        thickness: 4,
        fill: {
            gradient: ["#5386e7", "#43a7f0"]
        }
    }).on('circle-animation-progress', function(event, progress) {
        $(this).find('strong').html(Math.round(65 * progress) + '<i>%</i>');
    });

    $('#loader_3').circleProgress({
        startAngle: -Math.PI / 4 * 2,
        value: 0.25,
        size: 156,
        thickness: 4,
        fill: {
            gradient: ["#5386e7", "#43a7f0"]
        }
    }).on('circle-animation-progress', function(event, progress) {
        $(this).find('strong').html(Math.round(25 * progress) + '<i>%</i>');
    });

    $('#loader_4').circleProgress({
        startAngle: -Math.PI / 4 * 2,
        value: 0.59 ,
        size: 156,
        thickness: 4,
        fill: {
            gradient: ["#5386e7", "#43a7f0"]
        }
    }).on('circle-animation-progress', function(event, progress) {
        $(this).find('strong').html(Math.round(59 * progress) + '<i>%</i>');
    });

    $('#loader_5').circleProgress({
        startAngle: -Math.PI / 4 * 2,
        value: 0.83 ,
        size: 156,
        thickness: 4,
        fill: {
            gradient: ["#5386e7", "#43a7f0"]
        }
    }).on('circle-animation-progress', function(event, progress) {
        $(this).find('strong').html(Math.round(83 * progress) + '<i>%</i>');
    });

    // Counter
    $(".start-counter").each(function () {
        var counter = $(this);

        counter.countTo({
            formatter: function (value, options) {
                return value.toFixed(options.decimals).replace(/\B(?=(?:\d{3})+(?!\d))/g, ',');
            }
        });
    });

    // Bar Filler
    $('.featured-fund-raised-bar').barfiller({ barColor: '#ff5a00', duration: 1500 });

    $('.fund-raised-bar-1').barfiller({ barColor: '#ff5a00', duration: 1500 });
    $('.fund-raised-bar-2').barfiller({ barColor: '#ff5a00', duration: 1500 });
    $('.fund-raised-bar-3').barfiller({ barColor: '#ff5a00', duration: 1500 });
    $('.fund-raised-bar-4').barfiller({ barColor: '#ff5a00', duration: 1500 });
    $('.fund-raised-bar-5').barfiller({ barColor: '#ff5a00', duration: 1500 });
    $('.fund-raised-bar-6').barfiller({ barColor: '#ff5a00', duration: 1500 });

    // Load more
    let $container      = $('.portfolio-container');
    let $item           = $('.portfolio-item');

    $item.slice(0, 9).addClass('visible');

    $('.load-more-btn').on('click', function (e) {
        e.preventDefault();

        $('.portfolio-item:hidden').slice(0, 9).addClass('visible');
    });



})(jQuery);




/* FadeIn Scroll */
$(document).ready(function() {
    
    /* Every time the window is scrolled ... */
    $(window).scroll( function(){
    
        /* Check the location of each desired element */
        $('.fade').each( function(i){
            
            var top_of_object = $(this).position().top + $(this).outerHeight();
            var bottom_of_window = $(window).scrollTop() + $(window).height();
            
            /* If the object is completely visible in the window, fade it it */
            if( bottom_of_window  > top_of_object ){
                
                $(this).animate({'opacity':'1'},500);
                    
            }
            
        }); 
    
    });
    
});

window.onload = (event) => {
    $('.fade').first().animate({'opacity':'1'},500);
  };




  function isScrolledIntoView(elem) {
    var docViewTop = $(window).scrollTop();
    var docViewBottom = docViewTop + $(window).height();

    var elemTop = $(elem).offset().top;
    var elemBottom = elemTop + $(elem).height();

    return ((elemBottom <= docViewBottom) && (elemTop >= docViewTop));
}

// Class counter
function Counter(data) {
    var _default = {
      fps: 20,
      from: 0,
      time: 2000,
    }
    
    for (var attr in _default) {
      if (typeof data[attr] === 'undefined') {
        data[attr] = _default[attr];
      }
    }
    
    if (typeof data.to === 'undefined')
      return;
    
    data.fps = typeof data.fps === 'undefined' ? 20 : parseInt(data.fps);
    data.from = typeof data.from === 'undefined' ? 0 : parseFloat(data.from);
    
    var frames = data.time / data.fps,
        inc = (data.to - data.from) / frames,
        val = data.from;
    
    if (typeof data.start === 'function') {
       
    data.start(data.from, data)
      
    }
    var interval = setInterval(function() {
      frames--;
      val += inc;
      
      if (val >= data.to) {
        if (typeof data.complete === 'function') {
          console.log('complete');
          data.complete(data.to, data)
        }
        console.log(interval);
        clearInterval(interval);
      } else if (typeof data.progress === 'function') {
        data.progress(val, data)
      }
    }, data.fps);
  }
  
  // Auto-counter from HTML API
  var counters = document.getElementsByClassName('counter'),
      print = function(val, data) {
        data.element.innerHTML = val;
      }
  
  for (var i = 0, l = counters.length; i < l; i++) {
    // Loads from HTML dataset
    var data = {};
    for (var attr in counters[i].dataset) {
      data[attr] = counters[i].dataset[attr];
    }
    
    // Save element and callbacks
    data.element = counters[i];
    data.start = print;
    data.progress = print;
    data.complete = print;
    
    // Creates the counter
    if (isScrolledIntoView(counters[i])) new Counter(data);
  }