$(document).ready(function(){
	$('.logout').click(function(){
		var request = $.ajax({
			url: "/logout",
			method: "GET",
			success: function(msg){
				window.location = msg;
			}
		});
	})
})