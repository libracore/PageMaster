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