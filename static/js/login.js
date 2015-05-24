$(document).ready(function(){
	$('#user_login').click(function(){
		var modal	= $("#mymodal");
		var name	= modal.find('.modal-title').attr('username');
		var pass	= modal.find('.form-control').val();

		$.ajax({
			url: "/login",
			method: "GET",
			data: { username : name, password: pass },
			success: function(msg){
				window.location = msg;
			}
		});
	})
	$('#mymodal').on('show.bs.modal', function (event) {
//		console.log('asddsa')
//		return;
		var button = $(event.relatedTarget) // Button that triggered the modal
		var recipient = button.data('whatever') // Extract info from data-* attributes
		// If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
		// Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
		var modal = $(this);
		var phrases = [
			'Сам дурак, ',
			'Люди в космос летают, а ты ... ',
			'Доколе, '
		];

		modal.find('.modal-title').attr('username', recipient);
		modal.find('.modal-title').text(phrases[Math.floor(Math.random()*phrases.length)] + recipient);
	})
})