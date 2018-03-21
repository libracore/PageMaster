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
	
	libraModal();
	
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



function libraModal(){
	// Get the button that opens the modal
	var btns = document.getElementsByClassName("modal-btn");
	// When the user clicks on the button, open the modal
	for (var i = 0; i < btns.length; i++) {
		btns[i].onclick = function() {
			// Get the modal
			let modal = document.getElementsByClassName("x-"+this.id)[0];
			modal.style.display = "block";
			controlSpansForClose(this.id);
		}
	}
}

function controlSpansForClose(id) {
	// Get the <span> element that closes the modal
	var spans = document.getElementsByClassName("libra-modal-close");
	// When the user clicks on <span> (x), close the modal
	var modal = document.getElementsByClassName("x-"+id)[0];
	for (var i = 0; i < spans.length; i++) {
		spans[i].onclick = function() {
			modal.style.display = "none";
		}
	}
	// When the user clicks anywhere outside of the modal, close it
	window.onclick = function(event) {
		if (event.target == modal) {
			modal.style.display = "none";
		}
	}
}