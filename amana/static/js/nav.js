window.onscroll = function() {myFunction()};

// Get the header
var mynav = document.getElementById("mynav");

// Get the offset position of the navbar
var sticky = mynav.offsetTop;

// Add the sticky class to the header when you reach its scroll position. Remove "sticky" when you leave the scroll position
function myFunction() {
  if (window.pageYOffset > sticky) {
    mynav.classList.add("sticky");
  } else {
    mynav.classList.remove("sticky");
  }
}


$('.dropdown-submenu .dropdown-toggle').on("click", function(e) {
  e.stopPropagation();
  e.preventDefault();
  $(this).next('.dropdown-menu').toggle();
});