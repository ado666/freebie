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
	$('#imgupload').change(function(){
		if (this.files && this.files[0]) {
			var reader = new FileReader();
			reader.onload = function (e) {
				$('#preview').attr('src', e.target.result);
			}
			reader.readAsDataURL(this.files[0]);
		}
	})
	$('#save_company').click(function(e){
		var name	= $('#comp_name').val();
		var desc	= $('#comp_desc').val();
		var img		= $('#imgupload')[0].files[0];
		var cid		= $('#save_company').attr('cid');

		var fd		= new FormData();
		fd.append('name', name);
		fd.append('desc', desc);
		if (img) fd.append('file', img);
		if (cid) fd.append('cid', cid)

		$.ajax({
			url: "/company/save",
			method: "POST",
			data: fd,
			//Options to tell jQuery not to process data or worry about content-type.
			cache: false,
			contentType: false,
			processData: false,
			success: function(msg){
				window.location = msg;
			}
		});
	})

	$('#createcompanymodal').on('show.bs.modal', function (event) {
		var sender	= $(event.relatedTarget);
		var name	= sender.data('name');
		var desc	= sender.data('desc');
		var icon	= sender.data('icon');
		var id		= sender.data('id');
		$(this).data('compid', id);
		$('#comp_name').val(name)
		$('#comp_desc').val(desc)
		if (name){
			$('#save_company').text('Save');
			$('#save_company').attr('cid', id);
		}
		if (!name){
			$('#save_company').text('Create');
			$('#save_company').attr('cid', null);
		}
		if (icon){
			$('#preview').attr('src', 'img/companies/'+icon+'.png');
		}else{
			$('#preview').attr('src', 'img/icons/image_upload_icon.png');
		}
	})
	$('#createoffermodal').on('show.bs.modal', function (event) {
		var sender	= $(event.relatedTarget);
		var compid	= $('#createcompanymodal').data('compid');

		console.log(compid)
	})

})