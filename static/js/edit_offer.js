$(document).ready(function(){

	$('#imgupload1').change(function(){
		if (this.files && this.files[0]) {
			var reader = new FileReader();
			reader.onload = function (e) {
				$('#offer_icon').attr('src', e.target.result);
			}
			reader.readAsDataURL(this.files[0]);
		}
	})

	var start	= $('#offer_date_start').datepicker({format: 'dd-mm-yyyy'}).on('changeDate', function(){$('#offer_date_end').focus();start.hide();}).data('datepicker');
	var end		= $('#offer_date_end').datepicker({format: 'dd-mm-yyyy'}).on('changeDate', function(){end.hide()}).data('datepicker');

	$('#createoffermodal').on('show.bs.modal', function (event) {
		var compid	= $('#createcompanymodal').data('compid');

		if (!gmap['map-offer']){
			gmap.offerPin	= null;
			setTimeout(function(){
				gmap.init('offer');
				google.maps.event.addListener(gmap['map-offer'], 'click', function(event){
					if (!window.current_offer_is_my)	return;
					var pos	= event.latLng;
					var x	= pos.A;
					var y	= pos.F;
					if (gmap.offerPin)	gmap.removePin('offer', gmap.offerPin)
					gmap.offerPin	= gmap.addPin('offer', [x,y])[0]

					$('#offer_lat').text(x);
					$('#offer_lng').text(y);
				});
			}, 1000);

		}
	})

	$('#createoffermodal').on('hidden.bs.modal', function (event) {
		if (fb.current_company)	fb.opencompany(fb.current_company, false)
	})

	$('#save_offer').click(function(){
		var id		= $('#save_offer').attr('oid');
		var cid		= fb.current_company;
		var name	= $('#offer_name').val();
		var desc	= $('#offer_desc').val();
		var dist	= $('#offer_dist').val();
		var sdate	= $('#offer_date_start').val();
		var edate	= $('#offer_date_end').val();
		var img		= $('#imgupload1')[0].files[0];

		var mo		= $('#offer_mo').prop('checked');
		var tu		= $('#offer_tu').prop('checked');
		var we		= $('#offer_we').prop('checked');
		var th		= $('#offer_th').prop('checked');
		var fr		= $('#offer_fr').prop('checked');
		var sa		= $('#offer_sa').prop('checked');
		var su		= $('#offer_su').prop('checked');

		var stime	= $('#offer_time_start').val();
		var etime	= $('#offer_time_end').val();

		var lat		= $('#offer_lat').html();
		var lng		= $('#offer_lng').html();
		// тут типа проверки

		if (!sdate)	return alert('sdate');
		if (!edate)	return alert('edate');
		if (!stime)	return alert('stime');
		if (!etime)	return alert('etime');

		var fd		= new FormData();
		if (id)	fd.append('id', id);
		fd.append('cid', cid);
		fd.append('name', name);
		fd.append('desc', desc);
		fd.append('dist', dist);
		fd.append('sdate', sdate);
		fd.append('edate', edate);
		if (img) fd.append('file', img);

		fd.append('mo', mo ? 1 : 0);
		fd.append('tu', tu ? 1 : 0);
		fd.append('we', we ? 1 : 0);
		fd.append('th', th ? 1 : 0);
		fd.append('fr', fr ? 1 : 0);
		fd.append('sa', sa ? 1 : 0);
		fd.append('su', su ? 1 : 0);

		fd.append('stime', stime);
		fd.append('etime', etime);

		fd.append('lat', lat);
		fd.append('lng', lng);

		$.ajax({
			url: "/offer/save",
			method: "POST",
			data: fd,
			cache: false,
			contentType: false,
			processData: false,
			success: function(data){
				var offers	= $('#company_offers');

				var fd1	= new FormData();
				fd1.append('cid', fb.current_company);

				$.ajax({
					url: "/offer/getbycompany",
					method: "POST",
					data: fd1,
					cache: false,
					contentType: false,
					processData: false,
					success: function(data){
						var offers	= $('#company_offers');
						for (var i = 0, l = data.length; i < l; i++){
							offers.append('<tr><td>'+data[i].id+'</td><td>'+data[i].name+'</td></tr>');
						}

						$('#createoffermodal').modal('hide');
					}
				});
			}
		});
	})
})


fb.openoffer	= function(id, clear){
	if (id){
		var fd		= new FormData();
		fd.append('oid', id);
		$.ajax({
			url: "/offer/get",
			method: "POST",
			data: fd,
			cache: false,
			contentType: false,
			processData: false,
			success: function(data){
				$('#save_offer').attr('oid', data.id);
				$('#offer_name').val(data.name);
				$('#offer_desc').val(data.desc);
				$('#offer_icon').val(data.icon);
				$('#offer_dist').val(data.dist);

				$('#offer_date_start').datepicker('setValue', data.sdate);
				$('#offer_date_end').datepicker('setValue', data.edate);

				var shour		= data.stime.split('-')[0];
				var ehour		= data.etime.split('-')[0];

				$('#offer_time_start').val(shour);
				$('#offer_time_end').val(ehour);

				$('#offer_mo').prop('checked', data.mo);
				$('#offer_tu').prop('checked', data.tu);
				$('#offer_we').prop('checked', data.we);
				$('#offer_th').prop('checked', data.th);
				$('#offer_fr').prop('checked', data.fr);
				$('#offer_sa').prop('checked', data.sa);
				$('#offer_su').prop('checked', data.su);

				if (data.is_my){
					window.current_offer_is_my	= true;
					$('#offer_fields').prop('disabled', false);
					$('#imgupload1').prop('disabled', false);
					$('#pac-input').show();
				}else{
					window.current_offer_is_my	= false;
					$('#offer_fields').prop('disabled', true);
					$('#imgupload1').prop('disabled', true);
					$('#pac-input').hide();
				}

				if (data.icon){
					$('#offer_icon').attr('src', 'img/offers/'+data.icon+'.png');
				}else{
					$('#offer_icon').attr('src', 'img/blank.png');
				}
				$('#createoffermodal').modal('show');
				if (data.lat && data.lng){
					var x = data.lat;
					var y = data.lng;
					setTimeout(function(){
						if (gmap.offerPin)	gmap.removePin('offer', gmap.offerPin)
						gmap.offerPin	= gmap.addPin('offer', [x,y])[0]
					},1000)

					$('#offer_lat').text(x);
					$('#offer_lng').text(y);
				}
			}
		});
	}else{
		if (clear){
			window.current_offer_is_my	= true;
			$('#offer_fields').prop('disabled', false);
			$('#imgupload1').prop('disabled', false);
			$('#pac-input').show();
			$('#save_offer').attr('oid', null);
			$('#offer_name').val('');
			$('#offer_desc').val('');
			$('#offer_icon').val('');

			$('#offer_date_start').datepicker('setValue', new Date());
			$('#offer_date_end').datepicker('setValue', new Date());
			$('#offer_date_start').val('');
			$('#offer_date_end').val('');

			$('#offer_mo').prop('checked', false);
			$('#offer_tu').prop('checked', false);
			$('#offer_we').prop('checked', false);
			$('#offer_th').prop('checked', false);
			$('#offer_fr').prop('checked', false);
			$('#offer_sa').prop('checked', false);
			$('#offer_su').prop('checked', false);

			$('#offer_time_start').val('00');
			$('#offer_time_end').val('00');

			$('#offer_lat').text('');
			$('#offer_lng').text('');

			$('#offer_icon').attr('src', 'img/blank.png');

			if (gmap.offerPin)	gmap.removePin('offer', gmap.offerPin)
		}
		$('#createoffermodal').modal('show');
	}
}
