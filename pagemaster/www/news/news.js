$(document).ready(function() {
	$('.previous').off("click").on("click", function() {
		$(".old").toggle(true);
		$(".new").toggle(false);
	});
	$('.next').off("click").on("click", function() {
		$(".old").toggle(false);
		$(".new").toggle(true);
	});
	$('.categories').off("click").on("click", function() {
		$(".post").toggle(false);
		var searchClass = this.innerHTML.replace(" ", ".");
		$(".post."+searchClass).toggle(true);
	});
	$('.categories-all').off("click").on("click", function() {
		$(".old").toggle(false);
		$(".new").toggle(true);
	});
});