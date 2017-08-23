$(document).ready(function(){

  /*
   * Styles
   */
	$('.to-top').on('click', function(e){
  	e.preventDefault();
  	$('html, body').animate({ scrollTop: 0 }, 'medium');
	});
	$('ul.message').delay(2000).fadeOut('slow');

});


