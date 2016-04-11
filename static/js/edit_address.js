$(document).ready(function(){
	$('#createaddressmodal').on('hidden.bs.modal', function (event) {
		if (fb.current_company)	fb.opencompany(fb.current_company, false)
	})
	$('#createaddressmodal').on('show.bs.modal', function (event) {
//		var compid	= $('#createcompanymodal').data('compid');

		if (!gmap['map-address']){
			gmap.addressPin	= null;
			setTimeout(function(){
				gmap.init('address');
				google.maps.event.addListener(gmap['map-address'], 'click', function(event){
//					if (!window.current_addresss_is_my)	return;
					var pos	= event.latLng;
					var x	= pos.lat();
					var y	= pos.lng();
					if (gmap.addressPin)	gmap.removePin('address', gmap.addressPin)
					gmap.addressPin	= gmap.addPin('address', [x,y])[0]
//					gmap['map-address'].setZoom(15);


					$('#address_lat').text(x);
					$('#address_lng').text(y);
					gmap.getAddress(x,y,function(geo){
						$('#pac-input-address').val(geo.formatted_address);
					})
				});
			}, 1000);

		}
	})
	$('#save_address').click(function(){
		var id		= $('#save_address').attr('aid');
		var cid		= fb.current_company;
		var name	= $('#address_name').val();
		var address = $('#pac-input-address').val();

		var lat		= $('#address_lat').html();
		var lng		= $('#address_lng').html();
		// тут типа проверки

		var fd		= new FormData();
		if (id)	fd.append('id', id);
		fd.append('cid', cid);
		fd.append('name', name);
		fd.append('address', address);

		fd.append('lat', lat);
		fd.append('lng', lng);

		$.ajax({
			url: "/address/save",
			method: "POST",
			data: fd,
			cache: false,
			contentType: false,
			processData: false,
			success: function(data){
				var addresses	= $('#company_addresses');

				var fd1	= new FormData();
				fd1.append('cid', fb.current_company);

				$.ajax({
					url: "/address/getbycompany",
					method: "POST",
					data: fd1,
					cache: false,
					contentType: false,
					processData: false,
					success: function(data){
						var addresses	= $('#company_addresses');
						for (var i = 0, l = data.length; i < l; i++){
							addresses.append('<tr><td>'+data[i].id+'</td><td>'+data[i].name+'</td></tr>');
						}

						$('#createaddressmodal').modal('hide');
					}
				});
			}
		});
	})
})

fb.openaddress = function(id, clear){
	fb.closeCompany()
	if (id){
		var fd		= new FormData();
		fd.append('aid', id);
		$.ajax({
			url: "/address/get",
			method: "POST",
			data: fd,
			cache: false,
			contentType: false,
			processData: false,
			success: function(data){
				$('#save_address').attr('aid', data.id);
				$('#address_name').val(data.name);

				if (data.is_my){
					window.current_address_is_my	= true;
//					$('#offer_fields').prop('disabled', false);
//					$('#imgupload1').prop('disabled', false);
//					$('#pac-input').show();
//					$('.my-controls').show();
				}else{
					window.current_address_is_my	= false;
//					$('#offer_fields').prop('disabled', true);
//					$('#imgupload1').prop('disabled', true);
//					$('#pac-input').hide();
//					$('.my-controls').hide();
				}

				$('#createaddressmodal').modal('show');
				if (data.lat && data.lng){
					var x = data.lat;
					var y = data.lng;
					setTimeout(function(){
						if (gmap.addressPin)	gmap.removePin('address', gmap.addressPin)
						gmap.addressPin	= gmap.addPin('address', [x,y])[0]
					},1000)

					$('#address_lat').text(x);
					$('#address_lng').text(y);
					gmap.getAddress(x,y,function(geo){
						$('#pac-input-address').val(geo.formatted_address);
					})
				}
			}
		});
	}else{
		if (clear){
			window.current_address_is_my	= true;
//			$('#offer_fields').prop('disabled', false);
//			$('#imgupload1').prop('disabled', false);
//			$('#pac-input').show();
			$('#save_address').attr('aid', null);
			$('#address_name').val('');
			$('#pac-input-address').val('');
//			$('#offer_desc').val('');
//			$('#offer_icon').val('');

//			$('#offer_date_start').datepicker('setValue', new Date());
//			$('#offer_date_end').datepicker('setValue', new Date());
//			$('#offer_date_start').val('');
//			$('#offer_date_end').val('');

//			$('#offer_mo').prop('checked', false);
//			$('#offer_tu').prop('checked', false);
//			$('#offer_we').prop('checked', false);
//			$('#offer_th').prop('checked', false);
//			$('#offer_fr').prop('checked', false);
//			$('#offer_sa').prop('checked', false);
//			$('#offer_su').prop('checked', false);
//
//			$('#offer_time_start').val('00');
//			$('#offer_time_end').val('00');

			$('#address_lat').text('');
			$('#address_lng').text('');

			if (gmap.addressPin)	gmap.removePin('address', gmap.addressPin)
		}
		$('#createaddressmodal').modal('show');
	}
}
