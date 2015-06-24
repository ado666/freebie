$(document).ready(function(){
	$('#imgupload').change(function(){
		if (this.files && this.files[0]) {
			var reader = new FileReader();
			reader.onload = function (e) {
				$('#comp_icon').attr('src', e.target.result);
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
		if (cid) fd.append('cid', cid);

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
})

fb.opencompany	= function(id, clear){
	if (id){
		fb.current_company	= id;
		var fd		= new FormData();
		fd.append('id', id);
		$.ajax({
			url: "/company/get",
			method: "POST",
			data: fd,
			cache: false,
			contentType: false,
			processData: false,
			success: function(data){
				console.log(data)
				$('#save_company').attr('cid', data.id);
				$('#cretate-offer').attr('cid', data.id);
				$('#comp_name').val(data.name);
				$('#comp_desc').val(data.desc);
				$('#comp_icon').val(data.icon);
				var offers	= $('#company_offers');
				offers.empty()
				for (var i = 0, l = data.offers.length; i < l; i++){
					var str	= '<tr class="pointer" onclick="fb.offerClick('+data.offers[i].id+')" offer_id='+data.offers[i].id+'><td>'+data.offers[i].id+'</td><td>'+data.offers[i].name+'</td></tr>';
					offers.append($(str));
				}

				if (data.icon){
					$('#comp_icon').attr('src', 'img/companies/'+data.icon+'.png');
				}else{
					$('#comp_icon').attr('src', 'img/icons/image_upload_icon.png');
				}

				$('#createcompanymodal').modal('show');
			}
		});
	}else{
		fb.current_company	= null;
		if (clear){
			$('#save_company').attr('cid', null);
			$('#comp_name').val('');
			$('#comp_desc').val('');
			$('#comp_icon').attr('src', 'img/icons/image_upload_icon.png');
			var offers	= $('#company_offers');
			offers.empty()
		}
		$('#createcompanymodal').modal('show');
	}
}

fb.closeCompany	= function(){
	$('#createcompanymodal').modal('hide');
}

