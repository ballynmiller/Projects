(function($){
	$.fn.slideshow = function(options){
		var settings = $.extend({
			"images": this.find("img"),
			"index": 0,
			"transition": 6000
		}, options);

		//add slideshow-navigation
		var parent = $("<div/>", {
			id:"slideshow-navigation"
		});
		parent.append($("<span/>", {
			id:"prev-icon",
			text:"<"
		}).on("click", function(){
			clearInterval(r);
			$(settings["images"][settings["index"]]).fadeOut(1950);
			(settings["index"] == 0)? settings["index"] = settings["images"].length -1 : settings["index"] -= 1; 
			$(settings["images"][settings["index"]]).fadeIn(2000);
		}));
		parent.append($("<span/>", {
			id:"next-icon",
			text:">"
		}).on("click", function(){
			$(settings["images"][settings["index"]]).fadeOut(1950);
			(settings["index"] == settings["images"].length - 1)? settings["index"] = 0 : settings["index"] += 1; 
			$(settings["images"][settings["index"]]).fadeIn(2000);

		}));
		this.append(parent);

		//initialize the first image
		$(settings["images"][0]).fadeIn();
		this.hover(
			function(){
				if($(this).width() >= 750){
					clearInterval(r);
					$("#slideshow-navigation").fadeIn(700);
				}
			},
			function(){
				$('#slideshow-navigation').fadeOut(700);
				r = setInterval(rotate, settings["transition"]);
			}
		);

		function rotate(){
			$(settings["images"][settings["index"]]).fadeOut(1950);
			(settings["index"] == settings["images"].length -1)? settings["index"] = 0 : settings["index"] += 1; 
			$(settings["images"][settings["index"]]).fadeIn(2000);
		}

		r = setInterval(rotate, settings["transition"]);
	}
})(jQuery);