(function($){

	$.fn.slideshow = function(){
		$(this).each(function(){
			var imgs = $(this).find('img');
			var index = 0; 
			var self = this; 

			changePicture = function(){
				if(index >= imgs.length - 1) index = 0;
				$(self).css('background-image', 'url(' + imgs[index++].src + ')');
			}

			changePicture();
			setInterval(changePicture, 10000);

		});
	}

})(jQuery);
