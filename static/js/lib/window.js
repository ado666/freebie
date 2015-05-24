fb.openwindow	= function(div){
	var blocker	= document.createElement('div');
	$(blocker).addClass('blocker')
	$(blocker).attr('id', 'blocker')
	$('body').append($(blocker))
	$(div).attr('id', 'temp_content');

	$(blocker).click(function(){fb.closewindow()})

	$('body').append($(div))
}

fb.closewindow	= function(){
	var content	= $('#temp_content');

	content.attr('id', null)
	content.remove();
	$('#blocker').remove();
}