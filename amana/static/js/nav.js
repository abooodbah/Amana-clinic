window.onscroll = function() {myFunction()};

// Get the header
var mynav = document.getElementById("mynav");
var sitebrand = $(".site-branding")[0];

// Get the offset position of the navbar
var sticky = mynav.offsetTop;

// Add the sticky class to the header when you reach its scroll position. Remove "sticky" when you leave the scroll position
function myFunction() {
  if (window.pageYOffset > sticky) {
    mynav.classList.add("sticky");
    sitebrand.style["padding"] = "0px";
  } else {
    mynav.classList.remove("sticky");
    sitebrand.style["padding"] = "20px 0px";
  }
}


jQuery(document).ready(function($){
	
	$('a.scroll-link').click(function(e){
		e.preventDefault();
		$id = $(this).attr('href');
		$('body,html').animate({
			scrollTop: $($id).offset().top -75
		}, 750);
	});


});


(function($){
	$('.dropdown-menu a.dropdown-toggle').on('click', function(e) {
	  if (!$(this).next().hasClass('show')) {
		$(this).parents('.dropdown-menu').first().find('.show').removeClass("show");
	  }
	  var $subMenu = $(this).next(".dropdown-menu");
	  $subMenu.toggleClass('show');

	  $(this).parents('li.nav-item.dropdown.show').on('hidden.bs.dropdown', function(e) {
		$('.dropdown-submenu .show').removeClass("show");
	  });

	  return false;
	});
})(jQuery)