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


	$('#createcompanymodal').on('show.bs.modal', function (event) {
		return;
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
//	$('#createoffermodal').on('show.bs.modal', function (event) {
//		var compid	= $('#createcompanymodal').data('compid');
//
//		if (!gmap['map-offer'])	gmap.init('offer');
//
//
//
//		console.log(compid)
//	})


	$('.edit-company').click(function(){
		var id	= id || $(this).attr('comp_id');

		fb.opencompany(id, true);
	})

	fb.offerClick	= function(id){
		if (typeof(id) != "number") id = null;
		var id	= id || $(this).attr('offer_id');

		if (!fb.current_company){
			alert('Для создания акции надо сохранить компанию.');
			return;
		}

		fb.closeCompany();
		fb.openoffer(id, id ? false : true);
	}

	$('.edit-offer').on('click', fb.offerClick)
})