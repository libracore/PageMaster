// start of slider js 
$('#myCarousel').carousel({
  interval: 10000
 })

$('#myCarousel.carousel .itemm').each(function(){
  var next = $(this).next();
  if (!next.length) {
    next = $(this).siblings(':first');
  }
  next.children(':first-child').clone().appendTo($(this));
  
  if (next.next().length>0) {
    next.next().children(':first-child').clone().appendTo($(this));
  }
  else {
    $(this).siblings(':first').children(':first-child').clone().appendTo($(this));
  }
});

(function ($) {
  $(document).ready(function(){
	
	// set "scroll to top"-Function
	$(function () {
        	$(window).scroll(function () {	
			// scroll to top
			scrollFunction();
		});
	});
	
	$( window ).resize(function() {
		setStartHeight();
	});
	setStartHeight();
	
	// add newest blog to frontpage
	$("#place_for_blog").load("/blog .web-list-item.blog-list-item:first");
	
	
	// Add smooth scrolling to all links in navbar + footer link
	$("#ToTopBtn").on('click', function(event) {
		// Using jQuery's animate() method to add smooth page scroll
		// The optional number (900) specifies the number of milliseconds it takes to scroll to the specified area
		$('html, body').animate({
			scrollTop: 0
		}, 900, function() {
			// Add hash (#) to URL when done scrolling (default click behavior)
			//window.location.hash = "#home";
		});
	});
	
  });
}(jQuery));


function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        document.getElementById("ToTopBtn").style.display = "block";
    } else {
        document.getElementById("ToTopBtn").style.display = "none";
    }
}

function setStartHeight() {
	var navBarHeight = $('#navbar').height();
	$(".start").css("height",(window.innerHeight-navBarHeight-30) + "px");
}